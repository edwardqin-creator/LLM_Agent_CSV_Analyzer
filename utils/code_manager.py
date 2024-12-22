import logging
from typing import Optional, Dict, Any
import pandas as pd
import numpy as np
from datetime import datetime

class CodeManager:
    def __init__(self, log_file: str = "analysis.log"):
        # 设置日志
        self.setup_logging(log_file)
        
        # 存储当前执行的代码
        self.current_code: Optional[str] = None
        # 存储执行环境
        self.globals: Dict[str, Any] = {
            'pd': pd,
            'np': np
        }
        
    def setup_logging(self, log_file: str):
        """设置日志配置"""
        logging.basicConfig(
            filename=log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
    def set_dataframe(self, df: pd.DataFrame):
        """设置数据框到执行环境"""
        self.globals['df'] = df
        logging.info(f"DataFrame loaded with shape: {df.shape}")
        
    def update_code(self, code: str):
        """更新要执行的代码"""
        # 检查代码是否使用了正确的变量名
        if 'read_csv' in code or 'file_path' in code:
            logging.warning("Code attempts to read CSV file directly")
            # 修正代码，移除文件读取相关的代码
            import re
            code = re.sub(r'.*read_csv.*\n?', '', code)
            code = re.sub(r'.*file_path.*\n?', '', code)
        
        self.current_code = code
        logging.info("Code updated:")
        logging.info(code)
        
    def execute(self) -> tuple[bool, str, str]:
        """执行当前代码"""
        if not self.current_code:
            logging.error("No code to execute")
            return False, "", "No code available"
            
        print(f"执行分析中... {datetime.now().strftime('%H:%M:%S')}")
        
        try:
            # 捕获输出
            import io
            import sys
            output_buffer = io.StringIO()
            error_buffer = io.StringIO()
            
            # 重定向标准输出和错误
            sys.stdout = output_buffer
            sys.stderr = error_buffer
            
            # 执行代码
            exec(self.current_code, self.globals)
            
            # 恢复标准输出和错误
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            
            output = output_buffer.getvalue()
            error = error_buffer.getvalue()
            
            if error:
                logging.error(f"Execution error: {error}")
                print("执行出错，详细信息已记录到日志文件")
                return False, output, error
            else:
                logging.info("Code executed successfully")
                logging.info(f"Output: {output}")
                
                # 如果没有输出，尝试获取最后一个表达式的值
                if not output.strip():
                    last_line = self.current_code.strip().split('\n')[-1]
                    if not (last_line.startswith('print') or '=' in last_line):
                        try:
                            result = eval(last_line, self.globals)
                            output = str(result)
                        except:
                            pass
                
                print("分析完成")
                return True, output, ""
                
        except Exception as e:
            logging.exception("Execution failed")
            print("执行出错，详细信息已记录到日志文件")
            return False, "", str(e) 