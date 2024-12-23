# CSV Data Analysis System

基于大模型的CSV数据分析系统，能够通过自然语言需求来执行代码分析CSV数据（参照OpenAI's Code Interpreter）。

## 功能特点

- ✅CSV文件读取和解析
- ✅自然语言输入数据分析请求
- ✅基于大模型的Python代码生成
- ✅代码检查、执行和错误处理
- ✅自然语言结果解释
- ✅支持多轮对话分析

## 项目结构

## 模块功能说明

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
- 集成智谱AI GLM-4V模型
- 实现代码生成和执行功能
- 添加错误处理机制

## 2024-12-23
- 实现会话历史记录功能
- 优化代码提取逻辑
- 优化错误处理机制
- 增强数据预处理能力
- 改进结果展示格式
