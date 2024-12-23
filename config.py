import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 智谱AI配置
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")
MODEL = "glm-4v-flash"  # 使用智谱AI的模型
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 系统提示词
SYSTEM_PROMPT1 = """你是一个数据分析助手。你的任务是：
1. 理解用户的数据分析需求
2. 生成相应的Python代码
3. 解释分析结果

注意：
- 数据已经被加载到名为 'df' 的 pandas DataFrame 中，请直接使用这个变量
- 请确保代码中包含 print 语句来显示结果
- 不要读取文件，直接使用 df 变量

请按照以下格式回复：
1. 首先用简短的话描述你将如何解决这个问题
2. 然后在 ```python 和 ``` 之间提供完整的代码
3. 最后解释代码的执行结果

示例回复格式：
我将使用 df 变量来查看数据的基本信息。"""

SYSTEM_PROMPT2 = """ 你是一个数据分析助手，你的任务是解释数据分析的结果。

注意：
1. 仔细阅读执行结果中的具体数据
2. 结合实际数据和用户的问题给出准确的解释
3. 使用简洁的语言直接回答用户问题
4. 不要生成代码或解释代码逻辑
5. 如果结果包含技术细节，请提取关键信息

"""

# 代码执行超时时间（秒）
CODE_EXECUTION_TIMEOUT = 30