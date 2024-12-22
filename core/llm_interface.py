import json
import requests
import time
import hashlib
import hmac
import base64
from typing import List, Dict
from config import ZHIPU_API_KEY, MODEL, API_URL, SYSTEM_PROMPT
import logging

class LLMInterface:
    def __init__(self):
        self.api_key = ZHIPU_API_KEY
        self.model = MODEL
        self.system_prompt = SYSTEM_PROMPT
        
    def _generate_signature(self, timestamp: int) -> str:
        """生成智谱AI API签名"""
        try:
            api_key_id, api_key_secret = self.api_key.split('.')
            
            # 使用正确的签名格式
            signature_raw = f"timestamp={timestamp}&api_key={api_key_id}"
            
            # 确保api_key_secret是正确的格式
            if not api_key_secret.endswith('=='):
                api_key_secret += '=' * (-len(api_key_secret) % 4)
                
            signature = base64.b64encode(
                hmac.new(
                    api_key_secret.encode('utf-8'),
                    signature_raw.encode('utf-8'),
                    digestmod=hashlib.sha256
                ).digest()
            ).decode('utf-8')
            
            return signature
        except Exception as e:
            print(f"签名生成错误: {str(e)}")
            return ""
        
    def generate_response(self, 
                         messages: List[Dict[str, str]], 
                         data_info: dict = None) -> str:
        """生成回复"""
        # 构建完整的上下文
        full_messages = [{"role": "system", "content": self.system_prompt}]
        
        # 如果有数据信息，添加到上下文
        if data_info:
            data_context = f"""当前数据信息:
- 形状: {data_info['shape']}
- 列: {data_info['columns']}
- 数据类型: {data_info['dtypes']}"""
            full_messages.append({"role": "system", "content": data_context})
            
        full_messages.extend(messages)
        
        try:
            response = requests.post(
                API_URL,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.api_key}'
                },
                json={
                    'model': self.model,
                    'messages': full_messages,
                    'temperature': 0.7,
                    'top_p': 0.7,
                    'request_id': f'csv_analyzer_{int(time.time())}'
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                
                # 记录模型的完整响应到日志
                logging.info("Model Response:")
                logging.info(content)
                
                return content
            else:
                error_msg = f"API调用失败: HTTP {response.status_code} - {response.text}"
                logging.error(error_msg)
                return f"Error generating response: {error_msg}"
                
        except Exception as e:
            error_msg = f"API调用异常: {str(e)}"
            logging.exception(error_msg)
            return f"Error generating response: {error_msg}" 