import sys
import io
import contextlib
import traceback
from typing import Tuple

class CodeExecutor:
    def __init__(self, globals_dict: dict = None):
        self.globals_dict = globals_dict or {}
        
    def execute_code(self, code: str) -> Tuple[bool, str, str]:
        """
        执行Python代码
        
        Args:
            code: 要执行的代码字符串
            
        Returns:
            Tuple[bool, str, str]: (是否成功, 输出结果, 错误信息)
        """
        # 捕获标准输出和错误
        stdout = io.StringIO()
        stderr = io.StringIO()
        
        success = True
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                exec(code, self.globals_dict)
            except Exception as e:
                success = False
                print(f"Error: {str(e)}", file=stderr)
                traceback.print_exc(file=stderr)
                
        return success, stdout.getvalue(), stderr.getvalue() 