import sys
from core.analyzer import DataAnalyzer

def main():
    # 创建分析器实例
    analyzer = DataAnalyzer()
    
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("Usage: python main.py <csv_file_path>")
        return
        
    # 加载CSV文件
    csv_path = sys.argv[1]
    if not analyzer.load_data(csv_path):
        print(f"Failed to load CSV file: {csv_path}")
        return
        
    print(f"Successfully loaded {csv_path}")
    print("Enter your analysis queries (type 'exit' to quit):")
    
    # 主循环
    while True:
        query = input("\nQuery: ").strip()
        if query.lower() == 'exit':
            break
            
        # 处理查询
        result = analyzer.process_query(query)
        print("\nResult:")
        print(result)

if __name__ == "__main__":
    main() 