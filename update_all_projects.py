#!/usr/bin/env python3
import os

PROJECTS = {
    2: {'title': '分组聚合分析', 'icon': '📊', 'level': '入门', 'dataset': 'retail_orders.csv'},
    3: {'title': '购物篮分析', 'icon': '🛒', 'level': '进阶', 'dataset': 'market_basket.csv'},
    4: {'title': '客户聚类分析', 'icon': '👥', 'level': '进阶', 'dataset': 'customer_features.csv'},
    5: {'title': '数据可视化', 'icon': '📈', 'level': '进阶', 'dataset': 'retail_orders.csv'},
    6: {'title': 'A/B测试分析', 'icon': '🔬', 'level': '进阶', 'dataset': 'ab_test.csv'},
    7: {'title': '时间序列分析', 'icon': '⏰', 'level': '进阶', 'dataset': 'time_series_sales.csv'},
    8: {'title': '特征工程', 'icon': '🔧', 'level': '高级', 'dataset': 'customer_features.csv'},
    9: {'title': '异常值检测', 'icon': '🎯', 'level': '高级', 'dataset': 'customer_features.csv'},
    10: {'title': '多数据集合并', 'icon': '🔗', 'level': '进阶', 'dataset': 'retail_orders.csv'},
}

def update_project(proj_num, config):
    file_path = f'/workspace/projects/project{proj_num}/index.html'
    if not os.path.exists(file_path):
        print(f'跳过: {file_path}')
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新标题和元数据
    content = content.replace('数据清洗实战', config['title'])
    content = content.replace('🧹', config['icon'])
    content = content.replace('retail_orders.csv', config['dataset'])
    
    # 更新难度标签
    if config['level'] == '入门':
        content = content.replace('badge-easy', 'badge-easy')
    elif config['level'] == '进阶':
        content = content.replace('badge-easy', 'badge-medium')
    else:
        content = content.replace('badge-easy', 'badge-hard')
    
    # 更新项目ID
    content = content.replace("const projectId = 'project1'", f"const projectId = 'project{proj_num}'")
    content = content.replace("localStorage.setItem('homework_project1'", f"localStorage.setItem('homework_project{proj_num}'")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'已更新: project{proj_num} - {config["title"]}')

def main():
    for num, cfg in PROJECTS.items():
        update_project(num, cfg)
    print('完成！')

if __name__ == '__main__':
    main()
