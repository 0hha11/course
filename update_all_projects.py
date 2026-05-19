#!/usr/bin/env python3
import os

# 项目配置
projects = [
    {"id": 2, "name": "分组聚合分析", "emoji": "📊", "level": "入门", "time": "30分钟"},
    {"id": 3, "name": "购物篮分析", "emoji": "🛒", "level": "进阶", "time": "45分钟"},
    {"id": 4, "name": "客户聚类分析", "emoji": "👥", "level": "进阶", "time": "45分钟"},
    {"id": 5, "name": "数据可视化", "emoji": "📈", "level": "进阶", "time": "45分钟"},
    {"id": 6, "name": "A/B测试分析", "emoji": "🔬", "level": "进阶", "time": "45分钟"},
    {"id": 7, "name": "时间序列分析", "emoji": "⏰", "level": "进阶", "time": "45分钟"},
    {"id": 8, "name": "特征工程", "emoji": "🔧", "level": "高级", "time": "60分钟"},
    {"id": 9, "name": "异常值检测", "emoji": "🎯", "level": "高级", "time": "45分钟"},
    {"id": 10, "name": "多数据集合并", "emoji": "🔗", "level": "进阶", "time": "45分钟"}
]

# 读取项目1作为模板
with open('/workspace/projects/project1/index.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 为每个项目创建页面
for project in projects:
    project_id = project['id']
    project_name = project['name']
    project_emoji = project['emoji']
    project_level = project['level']
    project_time = project['time']
    
    content = template
    
    # 替换模板中的内容
    content = content.replace('数据清洗实战', project_name)
    content = content.replace('🧹', project_emoji)
    content = content.replace('入门', project_level)
    content = content.replace('30分钟', project_time)
    content = content.replace("projects['1']", f"projects['{project_id}']")
    
    # 更新默认数据
    new_default_data = f'''    const defaultProjectData = {{
            title: "{project_name}",
            exercises: [
                {{
                    id: 1,
                    question: "练习使用基本的 pandas 功能。",
                    code: "import pandas as pd\\nimport numpy as np\\n\\n# 创建一个简单的 DataFrame\\ndata = {{'col1': [1, 2, 3, 4, 5], 'col2': ['a', 'b', 'c', 'd', 'e']}}\\ndf = pd.DataFrame(data)\\nprint('DataFrame:')\\nprint(df)",
                    hint: "这是一个基础练习，先熟悉一下环境。",
                    answer: "你可以自由探索 pandas 的各种功能！"
                }}
            ],
            quiz: [
                {{
                    id: 1,
                    question: "这是一个示例问题。",
                    options: ["选项1", "选项2", "选项3", "选项4"],
                    correct: 0,
                    explanation: "这是一个示例解释。"
                }}
            ]
        }};'''
    
    # 替换默认数据部分
    start_marker = 'const defaultProjectData = {'
    end_marker = '};'
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx) + 2
    
    # 找到完整的 defaultProjectData 定义
    brace_count = 1
    pos = start_idx + len(start_marker)
    while brace_count > 0 and pos < len(content):
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
        pos += 1
    
    # 替换内容
    before = content[:start_idx]
    after = content[pos:]
    content = before + new_default_data + after
    
    # 确保替换了所有引用
    content = content.replace('allData.projects[\'1\']', f'allData.projects[\'{project_id}\']')
    
    # 写文件
    output_dir = f'/workspace/projects/project{project_id}'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ 更新: project{project_id} ({project_name})')

print('\n所有项目更新完成！')
