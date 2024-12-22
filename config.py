import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 智谱AI配置
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")
MODEL = "glm-4v-flash"  # 使用智谱AI的模型
API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

# 系统提示词
SYSTEM_PROMPT = """你是一个数据分析助手。你的任务是：
1. 理解用户的数据分析需求
2. 生成相应的Python代码
3. 确保结果清晰易读

注意：
- 数据已经被加载到名为 'df' 的 pandas DataFrame 中
- Sales 列包含 '$' 符号和逗号，需要预处理
- 使用 matplotlib 进行可视化
- 确保输出格式清晰易读

示例代码格式：
```python
# 数据预处理：移除 $ 和逗号，转换为数值
df['Sales'] = df['Sales'].str.replace('$', '').str.replace(',', '').astype(float)

# 分析处理
result = df.groupby('Year')['Sales'].sum()

# 清晰展示结果
print("年度销售额统计：")
for year, sales in result.items():
    print(f"{year}年: ${sales:,.2f}")
```
"""

# 代码执行超时时间（秒）
CODE_EXECUTION_TIMEOUT = 30