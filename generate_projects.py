#!/usr/bin/env python3
"""
批量生成所有项目文件
每个项目包含：
1. 独特的学习内容匹配项目标题
2. 练习板块使用代码编辑器
3. 测试板块使用选择题
4. 作业板块
"""

import os

def generate_project(project_data):
    """生成单个项目的HTML文件"""
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_data['title']} - Pandas数据分析实战训练营</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{ 
            font-family: 'Noto Sans SC', sans-serif; 
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            color: #e6e6e6; 
            line-height: 1.7; 
            min-height: 100vh;
        }}
        
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
        
        .skip-link {{
            position: absolute;
            top: -100px;
            left: 20px;
            background: #00d4ff;
            color: #1a1a2e;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none;
            z-index: 1000;
            transition: top 0.3s;
        }}
        .skip-link:focus {{ top: 20px; }}
        
        header {{ 
            background: rgba(0, 0, 0, 0.3); 
            border-bottom: 1px solid rgba(255, 255, 255, 0.08); 
            padding: 20px 0; 
            backdrop-filter: blur(10px);
        }}
        header .container {{ display: flex; justify-content: space-between; align-items: center; }}
        .header-left {{ display: flex; align-items: center; gap: 16px; }}
        .logo-circle {{
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #00d4ff 0%, #8b5cf6 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
        }}
        .logo-text {{
            font-size: 18px;
            font-weight: 700;
            background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        header a {{ 
            color: #a0a0b8; 
            text-decoration: none; 
            font-size: 14px; 
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 8px 12px;
            border-radius: 8px;
            transition: all 0.2s;
        }}
        header a:hover, header a:focus {{ 
            color: #00d4ff; 
            background: rgba(0, 212, 255, 0.1);
            outline: 2px solid #00d4ff;
            outline-offset: 2px;
        }}
        
        .project-header {{ padding: 48px 0 32px; }}
        .project-header .container {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 32px; }}
        .project-info {{ flex: 1; }}
        .project-icon-large {{
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
        }}
        .project-title {{ 
            font-size: 36px; 
            font-weight: 900; 
            color: #ffffff; 
            margin-bottom: 12px;
            line-height: 1.2;
        }}
        .project-description {{ 
            color: #a0a0b8; 
            font-size: 16px; 
            margin-bottom: 20px;
        }}
        .project-meta {{ display: flex; gap: 12px; flex-wrap: wrap; }}
        .badge {{ 
            padding: 6px 14px; 
            border-radius: 20px; 
            font-size: 12px; 
            font-weight: 700; 
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .badge-easy {{ 
            background: rgba(34, 197, 94, 0.15); 
            color: #4ade80; 
            border: 1px solid rgba(34, 197, 94, 0.3); 
        }}
        .badge-medium {{ 
            background: rgba(251, 191, 36, 0.15); 
            color: #fbbf24; 
            border: 1px solid rgba(251, 191, 36, 0.3); 
        }}
        .badge-hard {{ 
            background: rgba(239, 68, 68, 0.15); 
            color: #f87171; 
            border: 1px solid rgba(239, 68, 68, 0.3); 
        }}
        .badge-time {{ 
            background: rgba(255, 255, 255, 0.08); 
            color: #a0a0b8; 
            font-weight: 500; 
        }}
        .badge-dataset {{ 
            background: rgba(139, 92, 246, 0.15); 
            color: #a78bfa; 
            font-family: 'Monaco', 'Consolas', monospace;
        }}
        
        .progress-card {{
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.08) 0%, rgba(139, 92, 246, 0.08) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 24px;
            min-width: 280px;
        }}
        .progress-title {{ font-size: 14px; color: #8080a0; margin-bottom: 12px; }}
        .progress-circle {{
            position: relative;
            width: 100px;
            height: 100px;
            margin: 0 auto 16px;
        }}
        .progress-circle-svg {{ transform: rotate(-90deg); }}
        .progress-text {{
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
        }}
        .progress-stats {{
            display: flex;
            justify-content: space-between;
            text-align: center;
        }}
        .progress-stat {{ flex: 1; }}
        .progress-stat-num {{ font-size: 20px; font-weight: 700; color: #ffffff; }}
        .progress-stat-label {{ font-size: 12px; color: #707090; text-transform: uppercase; }}
        
        .tabs-wrapper {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 6px;
            display: flex;
            gap: 6px;
            margin-bottom: 32px;
        }}
        .tab {{ 
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
        }}
        .tab:hover, .tab:focus {{ 
            color: #ffffff; 
            outline: 2px solid #00d4ff;
            outline-offset: -2px;
        }}
        .tab.active {{ 
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%); 
            color: #ffffff;
            border: 1px solid rgba(0, 212, 255, 0.2);
        }}
        
        .tab-content {{ display: none; }}
        .tab-content.active {{ display: block; }}
        
        .search-container {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 32px;
        }}
        .search-box {{ position: relative; }}
        .search-input {{
            width: 100%;
            padding: 14px 20px 14px 48px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            color: #ffffff;
            font-size: 15px;
            outline: none;
            transition: all 0.2s;
        }}
        .search-input:focus {{
            border-color: #00d4ff;
            box-shadow: 0 0 0 3px rgba(0, 212, 255, 0.1);
        }}
        .search-icon {{
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: #a0a0b8;
        }}
        .search-results {{ margin-top: 16px; }}
        .search-result-item {{
            padding: 12px 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 10px;
            margin-bottom: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .search-result-item:hover, .search-result-item:focus {{
            background: rgba(0, 212, 255, 0.08);
            border-color: rgba(0, 212, 255, 0.3);
        }}
        
        .content-section {{ margin-bottom: 32px; }}
        .content-section-title {{
            font-size: 14px;
            font-weight: 700;
            color: #8b5cf6;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .content-section-title::before {{
            content: '';
            width: 24px;
            height: 2px;
            background: linear-gradient(90deg, #00d4ff, #8b5cf6);
            border-radius: 2px;
        }}
        
        .content-card {{ 
            background: rgba(255, 255, 255, 0.04); 
            border: 1px solid rgba(255, 255, 255, 0.08); 
            border-radius: 16px; 
            padding: 28px; 
            margin-bottom: 24px;
        }}
        .content-card h3 {{ 
            font-size: 20px; 
            font-weight: 700; 
            color: #ffffff; 
            margin-bottom: 16px; 
        }}
        .content-card p {{ 
            color: #c8c8d8; 
            line-height: 1.8; 
            margin-bottom: 12px; 
        }}
        .content-card ul {{ 
            list-style: none; 
            padding-left: 0; 
        }}
        .content-card ul li {{ 
            margin-bottom: 12px; 
            color: #c8c8d8;
            padding-left: 24px;
            position: relative;
        }}
        .content-card ul li::before {{
            content: '▸';
            position: absolute;
            left: 0;
            color: #00d4ff;
            font-weight: 700;
        }}
        .content-card strong {{ color: #ffffff; font-weight: 600; }}
        
        .info-box {{
            background: rgba(0, 212, 255, 0.08);
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 12px;
            padding: 16px 20px;
            margin: 16px 0;
        }}
        .info-box p {{ margin: 0; color: #a0d4ff; }}
        .tip-box {{
            background: rgba(139, 92, 246, 0.08);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 12px;
            padding: 16px 20px;
            margin: 16px 0;
        }}
        .tip-box p {{ margin: 0; color: #d4c4ff; }}
        
        .code-box {{ 
            background: #0d0d1a; 
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px; 
            padding: 20px; 
            overflow-x: auto; 
            margin: 16px 0;
        }}
        .code-box pre {{ 
            color: #d4d4d4; 
            font-family: 'Monaco', 'Consolas', monospace; 
            font-size: 14px; 
            line-height: 1.7; 
            white-space: pre;
        }}
        
        .code-editor-container {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 24px;
            margin: 20px 0;
        }}
        .code-editor-title {{
            font-size: 16px;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .code-editor {{
            background: #0d0d1a;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
        }}
        .code-textarea {{
            width: 100%;
            min-height: 200px;
            background: transparent;
            border: none;
            color: #d4d4d4;
            font-family: 'Monaco', 'Consolas', monospace;
            font-size: 14px;
            line-height: 1.7;
            resize: vertical;
            outline: none;
        }}
        .code-textarea:focus {{
            outline: 2px solid #00d4ff;
            outline-offset: 2px;
        }}
        .editor-controls {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .btn {{ 
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
        }}
        .btn-primary {{ 
            background: linear-gradient(135deg, #00d4ff 0%, #8b5cf6 100%); 
            color: white; 
        }}
        .btn-primary:hover, .btn-primary:focus {{ 
            transform: translateY(-2px); 
            box-shadow: 0 8px 24px rgba(0, 212, 255, 0.3);
            outline: 2px solid #00d4ff;
            outline-offset: 2px;
        }}
        .btn-secondary {{ 
            background: rgba(255, 255, 255, 0.06); 
            color: #ffffff; 
            border: 1px solid rgba(255, 255, 255, 0.12); 
        }}
        .btn-secondary:hover, .btn-secondary:focus {{ 
            background: rgba(255, 255, 255, 0.1); 
            border-color: rgba(255, 255, 255, 0.2);
            outline: 2px solid #ffffff;
            outline-offset: 2px;
        }}
        .btn:disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}
        .output-box {{
            background: #050510;
            border: 1px solid rgba(0, 212, 255, 0.2);
            border-radius: 12px;
            padding: 16px;
            margin-top: 16px;
            max-height: 300px;
            overflow-y: auto;
        }}
        .output-title {{
            font-size: 12px;
            font-weight: 600;
            color: #00d4ff;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }}
        .output-content {{
            color: #a0a0b8;
            font-family: 'Monaco', 'Consolas', monospace;
            font-size: 13px;
            line-height: 1.6;
            white-space: pre-wrap;
        }}
        .output-content.error {{ color: #f87171; }}
        .output-content.success {{ color: #4ade80; }}
        .loading-spinner {{
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-top-color: #ffffff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
        
        .question-box {{ 
            background: rgba(255, 255, 255, 0.04); 
            border: 1px solid rgba(255, 255, 255, 0.08); 
            border-radius: 16px; 
            padding: 24px; 
            margin-bottom: 20px; 
        }}
        .question-box h4 {{ 
            font-size: 16px; 
            font-weight: 600; 
            color: #ffffff; 
            margin-bottom: 16px; 
        }}
        .question-box p {{ 
            color: #c8c8d8; 
            margin-bottom: 16px; 
        }}
        
        .option-btn {{ 
            display: block; 
            width: 100%; 
            padding: 14px 18px; 
            margin-bottom: 10px; 
            border: 1px solid rgba(255, 255, 255, 0.1); 
            border-radius: 10px; 
            background: rgba(255, 255, 255, 0.02); 
            cursor: pointer; 
            text-align: left; 
            font-size: 14px; 
            color: #c8c8d8; 
            transition: all 0.2s; 
        }}
        .option-btn:hover, .option-btn:focus {{ 
            border-color: rgba(0, 212, 255, 0.4); 
            background: rgba(0, 212, 255, 0.08);
            outline: none;
        }}
        .option-btn.selected {{ 
            border-color: rgba(0, 212, 255, 0.6); 
            background: rgba(0, 212, 255, 0.12); 
            color: #ffffff;
        }}
        .option-btn.correct {{ 
            border-color: rgba(34, 197, 94, 0.6); 
            background: rgba(34, 197, 94, 0.15); 
            color: #86efac; 
        }}
        .option-btn.wrong {{ 
            border-color: rgba(239, 68, 68, 0.6); 
            background: rgba(239, 68, 68, 0.15); 
            color: #fca5a5; 
        }}
        
        .explanation {{ 
            background: rgba(251, 191, 36, 0.12); 
            border-left: 4px solid #fbbf24; 
            padding: 16px 20px; 
            margin-top: 16px; 
            border-radius: 0 10px 10px 0; 
            display: none; 
        }}
        .explanation p {{ color: #fef3c7; margin: 0; }}
        .explanation strong {{ color: #fcd34d; }}
        
        .btn-group {{ display: flex; gap: 12px; flex-wrap: wrap; margin-top: 20px; }}
        
        .test-result {{ 
            background: rgba(255, 255, 255, 0.04); 
            border: 1px solid rgba(255, 255, 255, 0.08); 
            border-radius: 20px; 
            padding: 40px; 
            text-align: center; 
            margin-top: 24px; 
            display: none; 
        }}
        .test-result-icon {{ font-size: 64px; margin-bottom: 20px; }}
        .test-result h3 {{ 
            font-size: 26px; 
            font-weight: 900; 
            color: #ffffff;
            margin-bottom: 12px; 
        }}
        .test-result .score {{ 
            font-size: 64px; 
            font-weight: 900; 
            background: linear-gradient(135deg, #00d4ff 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px; 
        }}
        .test-result p {{ color: #a0a0b8; margin-bottom: 24px; font-size: 15px; }}
        
        .homework-section {{
            background: rgba(139, 92, 246, 0.08);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 16px;
            padding: 24px;
            margin-top: 24px;
        }}
        .homework-title {{
            font-size: 18px;
            font-weight: 700;
            color: #a78bfa;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .homework-submit-area {{ margin-top: 16px; }}
        .homework-textarea {{
            width: 100%;
            min-height: 150px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            color: #ffffff;
            font-family: 'Monaco', 'Consolas', monospace;
            font-size: 14px;
            padding: 16px;
            resize: vertical;
            outline: none;
        }}
        .homework-textarea:focus {{
            border-color: #8b5cf6;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
        }}
        .submit-status {{
            margin-top: 12px;
            padding: 12px 16px;
            border-radius: 8px;
            display: none;
        }}
        .submit-status.success {{
            display: block;
            background: rgba(34, 197, 94, 0.15);
            color: #4ade80;
            border: 1px solid rgba(34, 197, 94, 0.3);
        }}
        .submit-status.error {{
            display: block;
            background: rgba(239, 68, 68, 0.15);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }}
        
        footer {{ 
            text-align: center; 
            padding: 40px 0; 
            border-top: 1px solid rgba(255, 255, 255, 0.08); 
            color: #505070; 
            font-size: 13px; 
            margin-top: 60px;
        }}
        
        @media (max-width: 968px) {{
            .project-header .container {{ flex-direction: column; }}
            .progress-card {{ width: 100%; }}
            .project-title {{ font-size: 28px; }}
        }}
        @media (max-width: 640px) {{
            .tabs-wrapper {{ flex-wrap: wrap; }}
            .tab {{ flex: 1 1 calc(50% - 3px); }}
            .project-title {{ font-size: 24px; }}
        }}
        
        .sr-only {{
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }}
    </style>
</head>
<body>
    <a href="#main-content" class="skip-link">跳转到主要内容</a>
    
    <header role="navigation" aria-label="主导航">
        <div class="container">
            <div class="header-left">
                <div class="logo-circle" role="img" aria-label="网站标志">{project_data['icon']}</div>
                <div class="logo-text">TT's Learning</div>
            </div>
            <a href="../../index.html" aria-label="返回首页">← 返回首页</a>
        </div>
    </header>

    <div class="project-header">
        <div class="container">
            <div class="project-info">
                <div class="project-icon-large" role="img" aria-label="{project_data['title']}图标">{project_data['icon']}</div>
                <h1 class="project-title">{project_data['title']}</h1>
                <p class="project-description">{project_data['description']}</p>
                <div class="project-meta" role="group" aria-label="项目标签">
                    <span class="badge {project_data['difficulty']}" aria-label="难度等级：{project_data['difficulty_label']}">{project_data['difficulty_label']}</span>
                    <span class="badge badge-time" aria-label="预计学习时间：30分钟">30分钟</span>
                    <span class="badge badge-dataset" aria-label="数据集：{project_data['dataset']}">📁 {project_data['dataset']}</span>
                </div>
            </div>
            <div class="progress-card" role="region" aria-label="学习进度">
                <div class="progress-title">学习进度</div>
                <div class="progress-circle">
                    <svg class="progress-circle-svg" width="100" height="100" role="img" aria-label="进度：0%">
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
                    <div class="progress-text" id="progress-percentage">0%</div>
                </div>
                <div class="progress-stats" role="list" aria-label="统计数据">
                    <div class="progress-stat" role="listitem">
                        <div class="progress-stat-num" id="chapters-learned">0/4</div>
                        <div class="progress-stat-label">已学习</div>
                    </div>
                    <div class="progress-stat" role="listitem">
                        <div class="progress-stat-num" id="exercises-done">0/5</div>
                        <div class="progress-stat-label">练习</div>
                    </div>
                    <div class="progress-stat" role="listitem">
                        <div class="progress-stat-num" id="test-score">0</div>
                        <div class="progress-stat-label">得分</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <main id="main-content" class="container">
        <div class="search-container">
            <div class="search-box">
                <span class="search-icon" aria-hidden="true">🔍</span>
                <input type="search" class="search-input" placeholder="搜索本项目内容... (按 / 键快速搜索)" 
                       aria-label="搜索项目内容" id="search-input" accesskey="/">
            </div>
            <div class="search-results" id="search-results" aria-live="polite"></div>
        </div>

        <div class="tabs-wrapper" role="tablist" aria-label="学习模块">
            <button class="tab active" role="tab" aria-selected="true" aria-controls="learn-tab" id="tab-learn" onclick="showTab('learn')">📚 学习</button>
            <button class="tab" role="tab" aria-selected="false" aria-controls="practice-tab" id="tab-practice" onclick="showTab('practice')">✏️ 练习</button>
            <button class="tab" role="tab" aria-selected="false" aria-controls="test-tab" id="tab-test" onclick="showTab('test')">📝 测试</button>
            <button class="tab" role="tab" aria-selected="false" aria-controls="homework-tab" id="tab-homework" onclick="showTab('homework')">📤 作业</button>
        </div>

        <div id="learn-tab" class="tab-content active" role="tabpanel" aria-labelledby="tab-learn">
{project_data['learn_content']}
        </div>

        <div id="practice-tab" class="tab-content" role="tabpanel" aria-labelledby="tab-practice">
            <div class="content-section">
                <div class="content-section-title">练习题（共5题）</div>
{project_data['practice_content']}
            </div>
        </div>

        <div id="test-tab" class="tab-content" role="tabpanel" aria-labelledby="tab-test">
            <div class="content-section">
                <div class="content-section-title">测试题（共 5 题，满分 100 分）</div>
{project_data['test_content']}
                <div class="btn-group">
                    <button class="btn btn-primary" onclick="submitTest()" aria-label="提交测试答案">
                        📤 提交答案
                    </button>
                    <button class="btn btn-secondary" onclick="resetTest()" aria-label="重新开始测试">
                        🔄 重新开始
                    </button>
                </div>
                <div class="test-result" id="test-result" role="alert" aria-live="assertive">
                    <div class="test-result-icon" id="result-icon">🎉</div>
                    <h3>测试完成！</h3>
                    <div class="score" id="final-score">0分</div>
                    <p id="result-message">太棒了！继续努力！</p>
                    <div class="btn-group" style="justify-content: center;">
                        <button class="btn btn-secondary" onclick="resetTest()">再来一次</button>
                        <a href="../../index.html" class="btn btn-primary" aria-label="返回首页">返回首页 →</a>
                    </div>
                </div>
            </div>
        </div>

        <div id="homework-tab" class="tab-content" role="tabpanel" aria-labelledby="tab-homework">
            <div class="content-section">
                <div class="content-section-title">作业提交</div>
                <div class="content-card">
                    <h3>📝 {project_data['homework']['title']}</h3>
                    <p>请完成以下任务：</p>
                    <ul>
{''.join([f'                        <li>{task}</li>\n' for task in project_data['homework']['tasks']])}
                    </ul>
                </div>
                <div class="homework-section">
                    <div class="homework-title">
                        <span>💻</span> 作业代码提交
                    </div>
                    <div class="homework-submit-area">
                        <textarea id="homework-code" class="homework-textarea" placeholder="请在此输入你的代码...">{project_data['homework']['template']}</textarea>
                        <div class="btn-group" style="margin-top: 16px;">
                            <button class="btn btn-primary" onclick="submitHomework()" aria-label="提交作业">📤 提交作业</button>
                            <button class="btn btn-secondary" onclick="runHomeworkCode()" aria-label="运行代码">▶️ 运行代码</button>
                        </div>
                        <div class="submit-status" id="submit-status"></div>
                    </div>
                </div>
                <div class="output-box" id="homework-output" style="display: none;">
                    <div class="output-title">📤 代码运行结果</div>
                    <pre class="output-content" id="homework-output-content"></pre>
                </div>
            </div>
        </div>
    </main>

    <footer role="contentinfo">
        <div class="container">
            <p>© 2024 TT's Learning Space · Pandas数据分析实战训练营</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
    
    <script>
        let pyodide = null;
        let isLoading = false;
        let testAnswers = {};
        let totalQuestions = 5;
        
        const searchData = {project_data['search_data']};
        
        async function initPyodide() {
            if (pyodide || isLoading) return;
            isLoading = true;
            const btn = document.getElementById('run-btn');
            if (btn) { btn.disabled = true; btn.innerHTML = '<span class="loading-spinner"></span> 加载中...'; }
            try {
                pyodide = await loadPyodide({ indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/" });
                console.log('Pyodide 加载成功！');
            } catch (error) { console.error('Pyodide 加载失败:', error); } finally {
                if (btn) { btn.disabled = false; btn.innerHTML = '▶️ 运行代码'; }
                isLoading = false;
            }
        }
        
        async function runCode() {
            const code = document.getElementById('code-input').value;
            const outputBox = document.getElementById('output-box');
            const outputContent = document.getElementById('output-content');
            const btn = document.getElementById('run-btn');
            if (!code.trim()) { alert('请先输入代码！'); return; }
            outputBox.style.display = 'block';
            outputContent.textContent = '正在执行...';
            outputContent.className = 'output-content';
            btn.disabled = true;
            btn.innerHTML = '<span class="loading-spinner"></span> 运行中...';
            try {
                await initPyodide();
                if (!pyodide) throw new Error('Pyodide 未初始化');
                pyodide.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
                `);
                await pyodide.runPythonAsync(code);
                const stdout = pyodide.runPython('sys.stdout.getvalue()');
                const stderr = pyodide.runPython('sys.stderr.getvalue()');
                if (stderr?.trim()) {
                    outputContent.textContent = stderr;
                    outputContent.className = 'output-content error';
                } else {
                    outputContent.textContent = stdout || '(代码执行完成，无输出)';
                    outputContent.className = 'output-content success';
                }
            } catch (error) {
                outputContent.textContent = '错误: ' + error.message;
                outputContent.className = 'output-content error';
            } finally { btn.disabled = false; btn.innerHTML = '▶️ 运行代码'; }
        }
        
        function resetCode() { document.getElementById('code-input').value = \`${project_data['default_code']}\`; }
        
        function copyCode() {
            const code = document.getElementById('code-input').value;
            navigator.clipboard.writeText(code).then(() => { alert('代码已复制到剪贴板！'); });
        }
        
        async function runPracticeCode(num) {
            const code = document.getElementById('practice-code-' + num).value;
            const outputBox = document.getElementById('practice-output-' + num);
            const outputContent = document.getElementById('practice-output-content-' + num);
            if (!code.trim()) { alert('请先输入代码！'); return; }
            outputBox.style.display = 'block';
            outputContent.textContent = '正在执行...';
            outputContent.className = 'output-content';
            try {
                await initPyodide();
                if (!pyodide) throw new Error('Pyodide 未初始化');
                pyodide.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
                `);
                await pyodide.runPythonAsync(code);
                const stdout = pyodide.runPython('sys.stdout.getvalue()');
                const stderr = pyodide.runPython('sys.stderr.getvalue()');
                if (stderr?.trim()) {
                    outputContent.textContent = stderr;
                    outputContent.className = 'output-content error';
                } else {
                    outputContent.textContent = stdout || '(代码执行完成，无输出)';
                    outputContent.className = 'output-content success';
                }
            } catch (error) {
                outputContent.textContent = '错误: ' + error.message;
                outputContent.className = 'output-content error';
            }
        }
        
        function resetPracticeCode(num) {
            const defaultCodes = {project_data['practice_codes']};
            document.getElementById('practice-code-' + num).value = defaultCodes[num];
        }
        
        async function runHomeworkCode() {
            const code = document.getElementById('homework-code').value;
            const outputBox = document.getElementById('homework-output');
            const outputContent = document.getElementById('homework-output-content');
            if (!code.trim()) { alert('请先输入代码！'); return; }
            outputBox.style.display = 'block';
            outputContent.textContent = '正在执行...';
            outputContent.className = 'output-content';
            try {
                await initPyodide();
                if (!pyodide) throw new Error('Pyodide 未初始化');
                pyodide.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
                `);
                await pyodide.runPythonAsync(code);
                const stdout = pyodide.runPython('sys.stdout.getvalue()');
                const stderr = pyodide.runPython('sys.stderr.getvalue()');
                if (stderr?.trim()) {
                    outputContent.textContent = stderr;
                    outputContent.className = 'output-content error';
                } else {
                    outputContent.textContent = stdout || '(代码执行完成，无输出)';
                    outputContent.className = 'output-content success';
                }
            } catch (error) {
                outputContent.textContent = '错误: ' + error.message;
                outputContent.className = 'output-content error';
            }
        }
        
        function submitHomework() {
            const status = document.getElementById('submit-status');
            status.className = 'submit-status success';
            status.innerHTML = '✅ 作业提交成功！';
            status.style.display = 'block';
        }
        
        function selectTestOption(btn, qNum, option, isCorrect) {
            testAnswers[qNum] = { option, isCorrect };
            const options = btn.parentElement.children;
            for (let i = 0; i < options.length; i++) { options[i].classList.remove('selected'); }
            btn.classList.add('selected');
        }
        
        function submitTest() {
            let correct = 0;
            for (let i = 1; i <= totalQuestions; i++) { if (testAnswers[i]?.isCorrect) correct++; }
            const score = Math.round((correct / totalQuestions) * 100);
            document.getElementById('final-score').textContent = score + '分';
            document.getElementById('result-message').textContent = score >= 80 ? '🎉 太棒了！继续保持！' : score >= 60 ? '👍 不错！继续努力！' : '💪 需要多加练习！';
            document.getElementById('result-icon').textContent = score >= 80 ? '🏆' : score >= 60 ? '😊' : '📚';
            document.getElementById('test-result').style.display = 'block';
        }
        
        function resetTest() {
            testAnswers = {};
            document.getElementById('test-result').style.display = 'none';
            const options = document.querySelectorAll('.option-btn');
            options.forEach(opt => { opt.classList.remove('selected', 'correct', 'wrong'); });
        }
        
        function showTab(tabName) {
            const tabs = document.querySelectorAll('.tab');
            const contents = document.querySelectorAll('.tab-content');
            tabs.forEach(tab => { tab.classList.remove('active'); tab.setAttribute('aria-selected', 'false'); });
            contents.forEach(content => { content.classList.remove('active'); });
            document.querySelector(`[onclick="showTab('${tabName}')"]`).classList.add('active');
            document.querySelector(`[onclick="showTab('${tabName}')"]`).setAttribute('aria-selected', 'true');
            document.getElementById(tabName + '-tab').classList.add('active');
        }
        
        function search() {
            const query = document.getElementById('search-input').value.toLowerCase();
            const results = document.getElementById('search-results');
            if (!query.trim()) { results.innerHTML = ''; return; }
            const matches = searchData.filter(item => 
                item.title.toLowerCase().includes(query) ||
                item.section.toLowerCase().includes(query) ||
                item.content.toLowerCase().includes(query)
            );
            if (matches.length === 0) {
                results.innerHTML = '<p style="color: #8080a0;">未找到匹配内容</p>';
                return;
            }
            results.innerHTML = matches.map(item => `
                <div class="search-result-item">
                    <strong>${item.title}</strong>
                    <p>${item.section}</p>
                </div>
            `).join('');
        }
        
        document.addEventListener('DOMContentLoaded', () => {
            const searchInput = document.getElementById('search-input');
            searchInput.addEventListener('input', search);
            document.addEventListener('keydown', (e) => {
                if (e.key === '/' && document.activeElement !== searchInput) { e.preventDefault(); searchInput.focus(); }
            });
            const progress = JSON.parse(localStorage.getItem('{project_data['id']}_progress') || '{}');
            updateProgress(progress);
        });
        
        function updateProgress(progress) {
            const total = 4;
            const completed = progress.chapters || 0;
            const percentage = Math.round((completed / total) * 100);
            document.getElementById('progress-percentage').textContent = percentage + '%';
            document.getElementById('progress-circle-inner').style.strokeDashoffset = 283 - (283 * percentage / 100);
            document.getElementById('chapters-learned').textContent = completed + '/' + total;
            document.getElementById('exercises-done').textContent = progress.exercises || '0/5';
            document.getElementById('test-score').textContent = progress.score || '0';
        }
    </script>
</body>
</html>"""
    
    return html_content

def generate_all_projects():
    """生成所有项目"""
    projects = [
        {
            "id": "project4",
            "title": "客户聚类分析",
            "icon": "👥",
            "description": "使用K-Means算法对客户进行分群，理解客户行为特征，为精准营销提供支持。",
            "difficulty": "badge-medium",
            "difficulty_label": "进阶",
            "dataset": "customer_features.csv",
            "search_data": "[{'title': '聚类分析', 'section': '1.1 什么是聚类分析', 'content': '无监督学习 相似度度量'}, {'title': 'K-Means', 'section': '2.1 K-Means原理', 'content': '簇中心 迭代优化'}, {'title': '最佳K值', 'section': '3.1 肘部法则', 'content': '惯性 轮廓系数'}, {'title': '客户细分', 'section': '4.1 客户细分实战', 'content': '特征标准化'}]",
            "default_code": "import pandas as pd\nfrom sklearn.cluster import KMeans\n\n# 创建客户数据\ndata = {\n    'Age': [28, 35, 42, 25, 48, 31, 38, 29],\n    'Income': [55000, 78000, 92000, 42000, 110000, 65000, 82000, 52000],\n    'SpendingScore': [72, 85, 68, 45, 90, 58, 78, 62]\n}\ndf = pd.DataFrame(data)\n\nprint('客户数据:')\nprint(df)\n\n# 应用K-Means聚类\nkmeans = KMeans(n_clusters=3, random_state=42)\ndf['Cluster'] = kmeans.fit_predict(df)\n\nprint('\\n聚类结果:')\nprint(df)\nprint('\\n簇中心:')\nprint(pd.DataFrame(kmeans.cluster_centers_, columns=['Age', 'Income', 'SpendingScore']))",
            "learn_content": """            <div class="content-section">
                <div class="content-section-title">第一章 聚类分析基础</div>
                
                <div class="content-card">
                    <h3>1.1 什么是聚类分析</h3>
                    <p>聚类分析是一种无监督学习方法，它将数据集中的对象分组，使得同一组内的对象相似度较高，而不同组间的对象相似度较低。</p>
                    <ul>
                        <li><strong>无监督学习</strong>：不需要标签，自动发现数据中的模式</li>
                        <li><strong>相似度度量</strong>：衡量数据点之间的相似程度</li>
                        <li><strong>簇的定义</strong>：由相似数据点组成的集合</li>
                        <li><strong>聚类算法分类</strong>：划分式、层次式、密度式等</li>
                    </ul>
                    <div class="info-box" role="note">
                        <p>💡 聚类分析广泛应用于客户细分、市场定位、图像分割等领域。</p>
                    </div>
                </div>

                <div class="content-card">
                    <h3>1.2 常用距离度量</h3>
                    <p>距离度量是聚类的基础，常用的距离包括：</p>
                    <div class="code-box">
<pre># 欧氏距离
distance = sqrt(sum((x_i - y_i)^2))

# 曼哈顿距离
distance = sum(|x_i - y_i|)

# 余弦相似度
similarity = (x · y) / (||x|| * ||y||)</pre>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <div class="content-section-title">第二章 K-Means算法</div>
                
                <div class="content-card">
                    <h3>2.1 K-Means原理</h3>
                    <p>K-Means是最常用的聚类算法之一，其目标是将n个对象划分为k个簇，使得每个簇内的对象到簇中心的距离最小。</p>
                    <ul>
                        <li>随机初始化k个簇中心</li>
                        <li>计算每个点到各中心的距离</li>
                        <li>将点分配到最近的簇</li>
                        <li>更新簇中心为簇内点的均值</li>
                        <li>迭代直到收敛</li>
                    </ul>
                    <div class="tip-box" role="tip">
                        <p>📌 K-Means对初始簇中心的选择很敏感，通常需要多次运行取最优结果。</p>
                    </div>
                </div>

                <div class="content-card">
                    <h3>2.2 Python实现K-Means</h3>
                    <p>使用scikit-learn实现K-Means聚类：</p>
                    <div class="code-box">
<pre>import pandas as pd
from sklearn.cluster import KMeans

# 创建客户数据
data = {
    'Age': [28, 35, 42, 25, 48, 31, 38, 29],
    'Income': [55000, 78000, 92000, 42000, 110000, 65000, 82000, 52000],
    'SpendingScore': [72, 85, 68, 45, 90, 58, 78, 62]
}
df = pd.DataFrame(data)

# 应用K-Means聚类
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

print(df)</pre>
                    </div>
                    
                    <div class="code-editor-container">
                        <div class="code-editor-title">
                            <span>💻</span> 在线代码编辑器
                        </div>
                        <div class="code-editor">
                            <textarea id="code-input" class="code-textarea" spellcheck="false">import pandas as pd
from sklearn.cluster import KMeans

# 创建客户数据
data = {
    'Age': [28, 35, 42, 25, 48, 31, 38, 29],
    'Income': [55000, 78000, 92000, 42000, 110000, 65000, 82000, 52000],
    'SpendingScore': [72, 85, 68, 45, 90, 58, 78, 62]
}
df = pd.DataFrame(data)

print('客户数据:')
print(df)

# 应用K-Means聚类
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

print('\\n聚类结果:')
print(df)
print('\\n簇中心:')
print(pd.DataFrame(kmeans.cluster_centers_, columns=['Age', 'Income', 'SpendingScore']))</textarea>
                        </div>
                        <div class="editor-controls">
                            <button class="btn btn-primary" onclick="runCode()" id="run-btn">▶️ 运行代码</button>
                            <button class="btn btn-secondary" onclick="resetCode()">🔄 重置</button>
                            <button class="btn btn-secondary" onclick="copyCode()">📋 复制</button>
                        </div>
                        <div class="output-box" id="output-box" style="display: none;">
                            <div class="output-title">📤 输出结果</div>
                            <pre class="output-content" id="output-content"></pre>
                        </div>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <div class="content-section-title">第三章 确定最佳K值</div>
                
                <div class="content-card">
                    <h3>3.1 肘部法则</h3>
                    <p>肘部法则是确定最佳K值的常用方法：</p>
                    <div class="code-box">
<pre>import matplotlib.pyplot as plt

# 计算不同K值的惯性
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df)
    inertia.append(kmeans.inertia_)

# 绘制肘部曲线
plt.plot(range(1, 11), inertia, 'bo-')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()</pre>
                    </div>
                </div>

                <div class="content-card">
                    <h3>3.2 轮廓系数</h3>
                    <p>轮廓系数是另一种评估聚类质量的指标：</p>
                    <div class="code-box">
<pre>from sklearn.metrics import silhouette_score

# 计算轮廓系数
sil_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(df)
    sil_score = silhouette_score(df, labels)
    sil_scores.append(sil_score)</pre>
                    </div>
                </div>
            </div>

            <div class="content-section">
                <div class="content-section-title">第四章 客户细分实战</div>
                
                <div class="content-card">
                    <h3>4.1 数据预处理</h3>
                    <p>对客户数据进行标准化处理：</p>
                    <div class="code-box">
<pre>from sklearn.preprocessing import StandardScaler

# 数据标准化
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# 应用K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)</pre>
                    </div>
                </div>

                <div class="content-card">
                    <h3>4.2 结果分析</h3>
                    <p>分析各个客户群体的特征：</p>
                    <ul>
                        <li>高收入高消费群体</li>
                        <li>高收入低消费群体</li>
                        <li>低收入高消费群体</li>
                        <li>低收入低消费群体</li>
                    </ul>
                    <div class="info-box" role="note">
                        <p>💡 通过聚类分析，企业可以针对不同客户群体制定差异化的营销策略。</p>
                    </div>
                </div>
            </div>""",
            "practice_codes": "{1: \"import pandas as pd\\n\\n# 创建客户数据\\ndata = {\\n    'CustomerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006'],\\n    'Age': [28, 35, 42, 25, 48, 31],\\n    'AnnualIncome': [55000, 78000, 92000, 42000, 110000, 65000],\\n    'SpendingScore': [72, 85, 68, 45, 90, 58]\\n}\\n\\ndf = pd.DataFrame(data)\\nprint(\"客户数据:\")\\nprint(df)\", 2: \"import pandas as pd\\nfrom sklearn.cluster import KMeans\\n\\ndata = {\\n    'Age': [28, 35, 42, 25, 48, 31, 38, 29],\\n    'Income': [55000, 78000, 92000, 42000, 110000, 65000, 82000, 52000],\\n    'Score': [72, 85, 68, 45, 90, 58, 78, 62]\\n}\\ndf = pd.DataFrame(data)\\n\\n# 使用K-Means进行聚类（K=3）\\nkmeans = KMeans(n_clusters=3, random_state=42)\\ndf['Cluster'] = kmeans.fit_predict(df)\\n\\nprint(\"聚类结果:\")\\nprint(df)\", 3: \"import pandas as pd\\nfrom sklearn.cluster import KMeans\\n\\ndata = {\\n    'Feature1': [1, 2, 8, 9, 2, 3, 7, 8],\\n    'Feature2': [1, 2, 8, 9, 8, 9, 1, 2]\\n}\\ndf = pd.DataFrame(data)\\n\\n# 计算不同K值的惯性\\ninertia = []\\nfor k in range(1, 7):\\n    kmeans = KMeans(n_clusters=k, random_state=42)\\n    kmeans.fit(df)\\n    inertia.append(kmeans.inertia_)\\n\\nprint(\"K值 vs 惯性:\")\\nfor k, iner in zip(range(1, 7), inertia):\\n    print(f\"K={k}: {iner:.2f}\")\", 4: \"import pandas as pd\\nfrom sklearn.cluster import KMeans\\nfrom sklearn.preprocessing import StandardScaler\\n\\ndata = {\\n    'Age': [28, 35, 42, 25, 48],\\n    'Income': [55000, 78000, 92000, 42000, 110000],\\n    'Score': [72, 85, 68, 45, 90]\\n}\\ndf = pd.DataFrame(data)\\n\\n# 数据标准化\\nscaler = StandardScaler()\\nscaled_features = scaler.fit_transform(df)\\n\\n# 应用K-Means\\nkmeans = KMeans(n_clusters=2, random_state=42)\\nclusters = kmeans.fit_predict(scaled_features)\\n\\nprint(\"标准化后的数据:\")\\nprint(pd.DataFrame(scaled_features, columns=['Age', 'Income', 'Score']))\\nprint(\"\\n聚类标签:\", clusters)\", 5: \"import pandas as pd\\nfrom sklearn.cluster import KMeans\\nfrom sklearn.preprocessing import StandardScaler\\n\\n# 模拟客户数据\\ndata = {\\n    'Age': [25, 32, 45, 28, 35, 42, 29, 38, 48, 31],\\n    'Income': [45000, 67000, 89000, 52000, 78000, 95000, 58000, 72000, 110000, 62000],\\n    'SpendingScore': [61, 78, 85, 55, 72, 90, 65, 82, 88, 58]\\n}\\ndf = pd.DataFrame(data)\\n\\n# 标准化数据\\nscaler = StandardScaler()\\nscaled_data = scaler.fit_transform(df)\\n\\n# 使用K-Means聚类（假设K=4）\\nkmeans = KMeans(n_clusters=4, random_state=42)\\ndf['Cluster'] = kmeans.fit_predict(scaled_data)\\n\\n# 分析各簇特征\\nprint(\"各簇统计信息:\")\\nprint(df.groupby('Cluster').mean())\"}",
            "practice_content": """                <div class="content-card">
                    <h3>练习 1：创建客户数据</h3>
                    <p>创建一个包含客户特征的数据集。</p>
                    <div class="code-editor-container">
                        <div class="code-editor">
                            <textarea id="practice-code-1" class="code-textarea" spellcheck="false">import pandas as pd

# 创建客户数据
data = {
    'CustomerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006'],
    'Age': [28, 35, 42, 25, 48, 31],
    'AnnualIncome': [55000, 78000, 92000, 42000, 110000, 65000],
    'SpendingScore': [72, 85, 68, 45, 90, 58]
}

df = pd.DataFrame(data)
print("客户数据:")
print(df)</textarea>
                        </div>
                        <div class="editor-controls">
                            <button class="btn btn-primary" onclick="runPracticeCode(1)">▶️ 运行代码</button>
