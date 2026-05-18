#!/usr/bin/env python3
import os
import re

# 项目配置
PROJECTS = {
    1: {'title': '数据清洗实战', 'icon': '🧹', 'level': '入门', 'level_class': 'badge-easy', 'dataset': 'retail_orders.csv'},
    2: {'title': '分组聚合分析', 'icon': '📊', 'level': '入门', 'level_class': 'badge-easy', 'dataset': 'retail_orders.csv'},
    3: {'title': '购物篮分析', 'icon': '🛒', 'level': '进阶', 'level_class': 'badge-medium', 'dataset': 'market_basket.csv'},
    4: {'title': '客户聚类分析', 'icon': '👥', 'level': '进阶', 'level_class': 'badge-medium', 'dataset': 'customer_features.csv'},
    5: {'title': '数据可视化', 'icon': '📈', 'level': '进阶', 'level_class': 'badge-medium', 'dataset': 'retail_orders.csv'},
    6: {'title': 'A/B测试分析', 'icon': '🔬', 'level': '进阶', 'level_class': 'badge-medium', 'dataset': 'ab_test.csv'},
    7: {'title': '时间序列分析', 'icon': '⏰', 'level': '进阶', 'level_class': 'badge-medium', 'dataset': 'time_series_sales.csv'},
    8: {'title': '特征工程', 'icon': '🔧', 'level': '高级', 'level_class': 'badge-hard', 'dataset': 'customer_features.csv'},
    9: {'title': '异常值检测', 'icon': '🎯', 'level': '高级', 'level_class': 'badge-hard', 'dataset': 'customer_features.csv'},
    10: {'title': '多数据集合并', 'icon': '🔗', 'level': '进阶', 'level_class': 'badge-medium', 'dataset': 'retail_orders.csv'},
}

# 新的样式
NEW_CSS = '''
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body { 
            font-family: 'Noto Sans SC', sans-serif; 
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #e6e6e6; 
            line-height: 1.7; 
            min-height: 100vh;
        }
        
        .container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
        
        header { 
            background: rgba(0, 0, 0, 0.3); 
            border-bottom: 1px solid rgba(255, 255, 255, 0.08); 
            padding: 20px 0; 
            backdrop-filter: blur(10px);
        }
        header .container { display: flex; justify-content: space-between; align-items: center; }
        .header-left { display: flex; align-items: center; gap: 16px; }
        .logo-circle {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #00d4ff 0%, #8b5cf6 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }
        .logo-text {
            font-size: 18px;
            font-weight: 700;
            background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        header a { 
            color: #a0a0b8; 
            text-decoration: none; 
            font-size: 14px; 
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: color 0.2s;
        }
        header a:hover { color: #00d4ff; }
        
        .project-header { padding: 48px 0 32px; }
        .project-header .container { display: flex; justify-content: space-between; align-items: flex-start; gap: 32px; }
        .project-info { flex: 1; }
        .project-icon-large {
            width: 64px;
            height: 64px;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            margin-bottom: 20px;
        }
        .project-title { 
            font-size: 36px; 
            font-weight: 900; 
            color: #ffffff; 
            margin-bottom: 12px;
            line-height: 1.2;
        }
        .project-description { 
            color: #a0a0b8; 
            font-size: 16px; 
            margin-bottom: 20px;
        }
        .project-meta { display: flex; gap: 12px; flex-wrap: wrap; }
        .badge { 
            padding: 6px 14px; 
            border-radius: 20px; 
            font-size: 12px; 
            font-weight: 700; 
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .badge-easy { 
            background: rgba(34, 197, 94, 0.15); 
            color: #4ade80; 
            border: 1px solid rgba(34, 197, 94, 0.3); 
        }
        .badge-medium { 
            background: rgba(251, 191, 36, 0.15); 
            color: #fbbf24; 
            border: 1px solid rgba(251, 191, 36, 0.3); 
        }
        .badge-hard { 
            background: rgba(239, 68, 68, 0.15); 
            color: #f87171; 
            border: 1px solid rgba(239, 68, 68, 0.3); 
        }
        .badge-time { 
            background: rgba(255, 255, 255, 0.08); 
            color: #a0a0b8; 
            font-weight: 500; 
        }
        .badge-dataset { 
            background: rgba(139, 92, 246, 0.15); 
            color: #a78bfa; 
            font-family: 'Monaco', 'Consolas', monospace;
        }
        
        .progress-card {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.08) 0%, rgba(139, 92, 246, 0.08) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 24px;
            min-width: 280px;
        }
        .progress-title { font-size: 14px; color: #8080a0; margin-bottom: 12px; }
        .progress-circle {
            position: relative;
            width: 100px;
            height: 100px;
            margin: 0 auto 16px;
        }
        .progress-circle-svg {
            transform: rotate(-90deg);
        }
        .progress-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 24px;
            font-weight: 900;
            background: linear-gradient(135deg, #00d4ff 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .progress-stats {
            display: flex;
            justify-content: space-between;
            text-align: center;
        }
        .progress-stat { flex: 1; }
        .progress-stat-num { font-size: 20px; font-weight: 700; color: #ffffff; }
        .progress-stat-label { font-size: 12px; color: #707090; text-transform: uppercase; }
        
        .tabs-wrapper {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 6px;
            display: flex;
            gap: 6px;
            margin-bottom: 32px;
        }
        .tab { 
            flex: 1;
            padding: 14px 24px; 
            border-radius: 12px; 
            font-size: 15px; 
            font-weight: 600; 
            cursor: pointer; 
            border: none; 
            background: transparent; 
            color: #a0a0b8; 
            transition: all 0.25s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .tab:hover { color: #ffffff; }
        .tab.active { 
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%); 
            color: #ffffff;
            border: 1px solid rgba(0, 212, 255, 0.2);
        }
        
        .tab-content { display: none; }
        .tab-content.active { display: block; }
        
        .content-card { 
            background: rgba(255, 255, 255, 0.04); 
            border: 1px solid rgba(255, 255, 255, 0.08); 
            border-radius: 16px; 
            padding: 28px; 
            margin-bottom: 24px;
        }
        .content-card h3 { 
            font-size: 20px; 
            font-weight: 700; 
            color: #ffffff; 
            margin-bottom: 16px; 
        }
        .content-card p { 
            color: #c8c8d8; 
            line-height: 1.8; 
            margin-bottom: 12px; 
        }
        .content-card ul { 
            list-style: disc; 
            padding-left: 20px; 
            color: #c8c8d8; 
        }
        .content-card ul li { 
            margin-bottom: 8px; 
        }
        
        .code-box { 
            background: #0d0d1a; 
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px; 
            padding: 20px; 
            overflow-x: auto; 
            margin: 16px 0;
        }
        .code-box pre { 
            color: #d4d4d4; 
            font-family: 'Monaco', 'Consolas', monospace; 
            font-size: 14px; 
            line-height: 1.7; 
            white-space: pre;
        }
        
        .question-box { 
            background: rgba(255, 255, 255, 0.04); 
            border: 1px solid rgba(255, 255, 255, 0.08); 
            border-radius: 16px; 
            padding: 20px; 
            margin-bottom: 16px; 
        }
        .question-box h4 { 
            font-size: 16px; 
            font-weight: 600; 
            color: #ffffff; 
            margin-bottom: 12px; 
        }
        .question-box p { 
            color: #c8c8d8; 
            margin-bottom: 12px; 
        }
        
        .option-btn { 
            display: block; 
            width: 100%; 
            padding: 14px 16px; 
            margin-bottom: 10px; 
            border: 1px solid rgba(255, 255, 255, 0.1); 
            border-radius: 10px; 
            background: rgba(255, 255, 255, 0.02); 
            cursor: pointer; 
            text-align: left; 
            font-size: 14px; 
            color: #c8c8d8; 
            transition: all 0.2s; 
        }
        .option-btn:hover { 
            border-color: rgba(0, 212, 255, 0.4); 
            background: rgba(0, 212, 255, 0.08); 
        }
        .option-btn.selected { 
            border-color: rgba(0, 212, 255, 0.6); 
            background: rgba(0, 212, 255, 0.12); 
            color: #ffffff;
        }
        .option-btn.correct { 
            border-color: rgba(34, 197, 94, 0.6); 
            background: rgba(34, 197, 94, 0.15); 
            color: #86efac; 
        }
        .option-btn.wrong { 
            border-color: rgba(239, 68, 68, 0.6); 
            background: rgba(239, 68, 68, 0.15); 
            color: #fca5a5; 
        }
        
        .explanation { 
            background: rgba(251, 191, 36, 0.12); 
            border-left: 4px solid #fbbf24; 
            padding: 16px; 
            margin-top: 16px; 
            border-radius: 0 8px 8px 0; 
            display: none; 
        }
        .explanation p { color: #fef3c7; }
        .explanation strong { color: #fcd34d; }
        
        .btn { 
            padding: 12px 24px; 
            border-radius: 12px; 
            font-weight: 600; 
            font-size: 14px; 
            text-decoration: none; 
            transition: all 0.2s; 
            border: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .btn-primary { 
            background: linear-gradient(135deg, #00d4ff 0%, #8b5cf6 100%); 
            color: white; 
        }
        .btn-primary:hover { 
            transform: translateY(-2px); 
            box-shadow: 0 8px 24px rgba(0, 212, 255, 0.3); 
        }
        .btn-outline { 
            background: rgba(255, 255, 255, 0.06); 
            color: #ffffff; 
            border: 1px solid rgba(255, 255, 255, 0.12); 
        }
        .btn-outline:hover { 
            background: rgba(255, 255, 255, 0.1); 
            border-color: rgba(255, 255, 255, 0.2); 
        }
        
        .test-result { 
            background: rgba(255, 255, 255, 0.04); 
            border: 1px solid rgba(255, 255, 255, 0.08); 
            border-radius: 16px; 
            padding: 32px; 
            text-align: center; 
            margin-top: 24px; 
            display: none; 
        }
        .test-result h3 { 
            font-size: 24px; 
            font-weight: 900; 
            color: #ffffff;
            margin-bottom: 16px; 
        }
        .test-result .score { 
            font-size: 48px; 
            font-weight: 900; 
            background: linear-gradient(135deg, #00d4ff 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 24px; 
        }
        
        footer { 
            text-align: center; 
            padding: 40px 0; 
            border-top: 1px solid rgba(255, 255, 255, 0.08); 
            color: #505070; 
            font-size: 13px; 
            margin-top: 60px;
        }
        
        @media (max-width: 968px) {
            .project-header .container { flex-direction: column; }
            .progress-card { width: 100%; }
            .project-title { font-size: 28px; }
        }
        @media (max-width: 640px) {
            .tabs-wrapper { flex-wrap: wrap; }
            .tab { flex: 1 1 calc(50% - 3px); }
            .project-title { font-size: 24px; }
        }
    </style>
'''

def process_project(proj_num, config):
    file_path = f'/workspace/projects/project{proj_num}/index.html'
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换字体链接和样式
    link_end = content.find('</style>')
    link_start = content.find('<link href=')
    if link_start != -1 and link_end != -1:
        content = content[:link_start] + NEW_CSS + content[link_end + 8:]
    
    # 替换头部
    header_start = content.find('<header>')
    tabs_start = content.find('<div class="tabs">')
    if header_start != -1 and tabs_start != -1:
        # 新头部
        new_header = f'''
    <header>
        <div class="container">
            <div class="header-left">
                <div class="logo-circle">📊</div>
                <div class="logo-text">TT's Learning</div>
            </div>
            <a href="../../index.html">← 返回首页</a>
        </div>
    </header>

    <div class="project-header">
        <div class="container">
            <div class="project-info">
                <div class="project-icon-large">{config['icon']}</div>
                <h1 class="project-title">{config['title']}</h1>
                <div class="project-meta">
                    <span class="badge {config['level_class']}">{config['level']}</span>
                    <span class="badge badge-time">30分钟</span>
                    <span class="badge badge-dataset">📁 {config['dataset']}</span>
                </div>
            </div>
            <div class="progress-card">
                <div class="progress-title">学习进度</div>
                <div class="progress-circle">
                    <svg class="progress-circle-svg" width="100" height="100">
                        <circle cx="50" cy="50" r="45" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="8"/>
                        <circle cx="50" cy="50" r="45" fill="none" stroke="url(#gradient)" stroke-width="8" 
                                stroke-dasharray="283" stroke-dashoffset="283" stroke-linecap="round" id="progress-circle-inner"/>
                        <defs>
                            <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#00d4ff"/>
                                <stop offset="100%" stop-color="#8b5cf6"/>
                            </linearGradient>
                        </defs>
                    </svg>
                    <div class="progress-text">0%</div>
                </div>
                <div class="progress-stats">
                    <div class="progress-stat">
                        <div class="progress-stat-num">0/4</div>
                        <div class="progress-stat-label">已学习</div>
                    </div>
                    <div class="progress-stat">
                        <div class="progress-stat-num">0/3</div>
                        <div class="progress-stat-label">练习</div>
                    </div>
                    <div class="progress-stat">
                        <div class="progress-stat-num">0</div>
                        <div class="progress-stat-label">得分</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="tabs-wrapper">
'''
        content = content[:header_start] + new_header + content[tabs_start:]
    
    # 替换 tabs class
    content = content.replace('<div class="tabs">', '')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'已更新: project{proj_num}')
    return True

def main():
    for num, cfg in PROJECTS.items():
        process_project(num, cfg)
    print('全部完成！')

if __name__ == '__main__':
    main()
