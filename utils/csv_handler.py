import pandas as pd
from typing import Optional

class CSVHandler:
    def __init__(self):
        self.current_df: Optional[pd.DataFrame] = None
        self.file_path: Optional[str] = None

    def load_csv(self, file_path: str) -> bool:
        """
        加载CSV文件
        
        Args:
            file_path: CSV文件路径
            
        Returns:
            bool: 是否成功加载
        """
        try:
            self.current_df = pd.read_csv(file_path)
            self.file_path = file_path
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
            "sample": self.current_df.head(3).to_dict()
        } 