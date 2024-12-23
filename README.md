# CSV Data Analysis System

基于大模型的CSV数据分析系统，能够通过自然语言需求来执行代码分析CSV数据。

[English](./README_EN.md) | 简体中文

## 🌟 基础功能

- 🤖 基于智谱AI [GLM-4V-Flash](https://open.bigmodel.cn/dev/api/normal-model/glm-4v)（免费开放调用）的智能分析系统
- 📊 智能CSV数据读取和解析
- 💬 自然语言交互式数据分析
- 💻 基于大模型的Python代码生成
- 👨🏻‍💻 自动化代码检查、执行和错误处理
- 🔍 智能结果总结
  
## 🌟 特性
- 🔄 支持多轮对话分析
- 🛡️ 安全的代码执行环境
- 📝 详细的日志记录系统

## 🚀 快速开始

### 环境要求
- Python 3.8+
- 智谱AI API密钥

### 安装
1. 克隆仓库
```bash
git clone https://github.com/edwardqin-creator/CSV_Analyzer.git

cd CSV_Analyzer
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置环境变量
```bash
### 在根目录创建并编辑 .env 文件，添加你的智谱AI API密钥
ZHIPU_API_KEY=your_api_key_here
```

### 使用方法

1. 运行程序
```bash
python main.py ./data/test.csv
```

2. 开始分析
```bash
Query: 请分析数据的基本统计信息, 并输出前五行

Query: 分析 Clothing 随时间变化的总销售额趋势

Query: 对 Bikes类进行同样的分析

Query: 哪些年份 Components 比 Accessories 的总销售额高?

Query: exit # 退出程序
```

## 📖 项目架构

## 🔧 模块功能说明

### 核心模块
1. **main.py**
   - 程序入口点
   - 处理命令行参数
   - 实现交互式查询循环

2. **config.py**
   - 管理配置信息
   - 加载环境变量
   - 设置模型参数

3. **core/analyzer.py**
   - 实现核心分析逻辑
   - 协调数据处理、代码生成和执行
   - 处理分析结果

4. **core/llm_interface.py**
   - 封装智谱AI GLM-4V接口
   - 处理API认证和请求
   - 管理对话上下文

### 工具模块
1. **utils/csv_handler.py**
   - CSV文件读取和解析
   - 提供数据基本信息
   - 数据预处理功能

2. **utils/code_executor.py**
   - 提供安全的代码执行环境
   - 捕获和处理执行错误
   - 管理执行上下文

## 开发日志

### 2024-12-22
- 初始化项目结构
- 实现基础功能模块
- 集成智谱AI GLM-4V
- 实现代码生成和执行功能
- 添加错误处理机制

## 2024-12-23
- 实现会话历史记录功能
- 优化代码提取逻辑
- 优化错误处理机制
- 增强数据预处理能力
- 改进结果展示格式

## 🛠️ 开发计划

- [ ] 支持更多模型
- [ ] 支持图表数据分析（GPT-4V--Flash模型已经可以支持 需要完善）
- [ ] 优化执行效率

## 🔗 相关链接

- [智谱AI官方文档](https://open.bigmodel.cn/doc/api)

## 🙏 致谢

- 感谢智谱AI提供的模型支持
