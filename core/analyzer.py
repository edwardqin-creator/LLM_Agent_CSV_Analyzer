import pandas as pd
import numpy as np
import re
from typing import List, Dict, Optional
from utils.csv_handler import CSVHandler
from utils.code_manager import CodeManager
from core.llm_interface import LLMInterface

class DataAnalyzer:
    def __init__(self):
        self.csv_handler = CSVHandler()
        self.code_manager = CodeManager()
        self.llm_interface = LLMInterface()
        self.conversation_history: List[Dict[str, str]] = []
        
    def load_data(self, file_path: str) -> bool:
        """加载CSV数据"""
        success = self.csv_handler.load_csv(file_path)
        if success:
            self.code_manager.set_dataframe(self.csv_handler.get_dataframe())
        return success
        
    def process_query(self, query: str) -> str:
        """处理用户查询"""
        print(f"\n处理查询: {query}")
        
        # 添加用户查询到对话历史
        self.conversation_history.append({"role": "user", "content": query})
        
        # 获取数据信息
        data_info = self.csv_handler.get_data_info()
        
        # 生成代码
        print("生成��析代码...")
        response = self.llm_interface.generate_response(
            self.conversation_history,
            data_info
        )
        
        # 提取代码并执行
        code_blocks = self._extract_code(response)
        if not code_blocks:
            return "无法生成有效的分析代码。"
            
        # 更新并执行代码
        self.code_manager.update_code(code_blocks[0])
        success, output, error = self.code_manager.execute()
        
        if not success:
            error_message = f"代码执行出错: {error}"
            self.conversation_history.append({"role": "assistant", "content": error_message})
            return self._handle_error(query, error)
            
        # 请求模型解释执行结果
        print("生成结果解释...")
        explanation_prompt = {
            "role": "system",
            "content": """你是一个数据分析助手，现在需要解释数据分析的结果。请注意：
1. 仔细阅读执行结果中的具体数据
2. 基于实际数据给出准确的解释
3. 使用简洁的语言直接回答用户问题
4. 不要生成代码或解释代码逻辑
5. 如果结果包含技术细节，请提取关键信息"""
        }
        
        result_prompt = {
            "role": "user",
            "content": f"""原始问题：{query}

分析结果：
{output}

请基于上述分析结果，直接回答原始问题。回答需要：
1. 准确：确保回答与数据结果一致
2. 相关：直接回应用户的问题
3. 简洁：只提供必要的信息"""
        }

        explanation = self.llm_interface.generate_response(
            [explanation_prompt, result_prompt],
            None  # 不需要再传递数据信息
        )
        
        # 返回结果和解释
        return f"""执行结果：
{output}

分析结论：
{explanation}"""
        
    def _extract_code(self, response: str) -> List[str]:
        """从回复中提取代码块"""
        code_blocks = []
        # 查找 ```python 和 ``` 之间的代码块
        import re
        pattern = r'```python\n(.*?)```'
        matches = re.findall(pattern, response, re.DOTALL)
        
        if matches:
            code_blocks.extend(matches)
        
        # 如果没有明确标记为Python的代码块，尝试提取任何代码块
        if not code_blocks:
            pattern = r'```(.*?)```'
            matches = re.findall(pattern, response, re.DOTALL)
            code_blocks.extend(matches)
        
        # 清理代码块（移除前后的空白字符）
        code_blocks = [block.strip() for block in code_blocks]
        
        return code_blocks
        
    def _handle_error(self, query: str, error: str) -> str:
        """处理代码执行错误"""
        error_prompt = f"""之前的代码执行出错。错误信息：
{error}

请修正代码并重试。"""
        self.conversation_history.append({"role": "user", "content": error_prompt})
        return self.process_query(query) 