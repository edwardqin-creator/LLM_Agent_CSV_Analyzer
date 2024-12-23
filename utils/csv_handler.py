import pandas as pd
import numpy as np
from typing import Optional, Dict, Any
import re

class CSVHandler:
    def __init__(self):
        self.current_df: Optional[pd.DataFrame] = None
        self.file_path: Optional[str] = None
        self.units: Dict[str, str] = {}  # 存储每列的单位信息
        
    def _convert_currency(self, value: str) -> float:
        """转换货币字符串为数值"""
        if isinstance(value, (int, float)):
            return float(value)
        if pd.isna(value):
            return np.nan
        # 移除货币符号和逗号，转换为浮点数
        cleaned = str(value).replace('$', '').replace(',', '')
        try:
            return float(cleaned)
        except ValueError:
            return np.nan
            
    def _convert_percentage(self, value: str) -> float:
        """转换百分比字符串为数值"""
        if isinstance(value, (int, float)):
            return float(value)
        if pd.isna(value):
            return np.nan
        # 移除百分号并转换为小数
        cleaned = str(value).replace('%', '')
        try:
            return float(cleaned) / 100
        except ValueError:
            return np.nan
            
    def _detect_and_convert_column(self, series: pd.Series) -> tuple[pd.Series, str]:
        """检测列的数据类型并进行转换"""
        sample = series.dropna().iloc[0] if not series.empty else ""
        unit = ""
        
        # 检查是否是货币
        if isinstance(sample, str) and '$' in str(sample):
            unit = '$'
            return pd.Series([self._convert_currency(x) for x in series]), unit
            
        # 检查是否是百分比
        if isinstance(sample, str) and '%' in str(sample):
            unit = '%'
            return pd.Series([self._convert_percentage(x) for x in series]), unit
            
        # 尝试转换为数值类型
        try:
            numeric_series = pd.to_numeric(series)
            return numeric_series, unit
        except:
            # 如果转换失败，保持原样
            return series, unit

    def load_csv(self, file_path: str) -> bool:
        """
        加载CSV文件并智能转换数据类型
        
        Args:
            file_path: CSV文件路径
            
        Returns:
            bool: 是否成功加载
        """
        try:
            # 首先以字符串类型加载所有列
            df = pd.read_csv(file_path, dtype=str)
            
            # 对每列进行类型检测和转换
            for column in df.columns:
                df[column], unit = self._detect_and_convert_column(df[column])
                if unit:
                    self.units[column] = unit
            
            self.current_df = df
            self.file_path = file_path
            
            # 记录数据类型转换结果
            type_info = {col: {
                'dtype': str(df[col].dtype),
                'unit': self.units.get(col, 'N/A')
            } for col in df.columns}
            print("\n数据类型转换结果：")
            for col, info in type_info.items():
                if info['unit'] != 'N/A':
                    print(f"- {col}: {info['dtype']} (单位: {info['unit']})")
                
            return True
            
        except Exception as e:
            print(f"Error loading CSV file: {str(e)}")
            return False

    def get_dataframe(self) -> Optional[pd.DataFrame]:
        """获取当前数据框"""
        return self.current_df

    def get_data_info(self) -> dict:
        """获取数据基本信息"""
        if self.current_df is None:
            return {}
        
        return {
            "shape": self.current_df.shape,
            "columns": list(self.current_df.columns),
            "dtypes": self.current_df.dtypes.to_dict(),
            "units": self.units,  # 添加单位信息
            "sample": self.current_df.head(3).to_dict()
        } 