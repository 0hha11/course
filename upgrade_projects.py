#!/usr/bin/env python3
import os

projects = {
    "project2": {
        "title": "项目02：销售数据分组聚合",
        "project_num": "02",
        "primary_color": "#22c55e",
        "primary_rgb": "34, 197, 94",
        "gradient_start": "#22c55e",
        "gradient_end": "#00f5ff",
        "data_file": "retail_orders.csv",
        "description": "按产品、地区、时间进行分组，计算销售统计指标"
    },
    "project3": {
        "title": "项目03：数据可视化基础",
        "project_num": "03",
        "primary_color": "#f97316",
        "primary_rgb": "249, 115, 22",
        "gradient_start": "#f97316",
        "gradient_end": "#ec4899",
        "data_file": "retail_orders.csv",
        "description": "使用Matplotlib创建折线图、柱状图、饼图等常见图表"
    },
    "project4": {
        "title": "项目04：数据合并与连接",
        "project_num": "04",
        "primary_color": "#3b82f6",
        "primary_rgb": "59, 130, 246",
        "gradient_start": "#3b82f6",
        "gradient_end": "#8b5cf6",
        "data_file": "orders.csv, customers.csv, products.csv",
        "description": "使用merge、concat、join合并多个数据源"
    },
    "project5": {
        "title": "项目05：时间序列分析",
        "project_num": "05",
        "primary_color": "#a855f7",
        "primary_rgb": "168, 85, 247",
        "gradient_start": "#a855f7",
        "gradient_end": "#ec4899",
        "data_file": "retail_orders.csv",
        "description": "日期处理、时间重采样、移动窗口计算"
    },
    "project6": {
        "title": "项目06：文本数据处理",
        "project_num": "06",
        "primary_color": "#ec4899",
        "primary_rgb": "236, 72, 153",
        "gradient_start": "#ec4899",
        "gradient_end": "#f97316",
        "data_file": "customer_reviews.csv",
        "description": "字符串操作、正则表达式、文本分析"
    },
    "project7": {
        "title": "项目07：数据透视表",
        "project_num": "07",
        "primary_color": "#14b8a6",
        "primary_rgb": "20, 184, 166",
        "gradient_start": "#14b8a6",
        "gradient_end": "#3b82f6",
        "data_file": "retail_orders.csv",
        "description": "使用pivot_table创建多维数据分析报表"
    },
    "project8": {
        "title": "项目08：数据导出与报告",
        "project_num": "08",
        "primary_color": "#f59e0b",
        "primary_rgb": "245, 158, 11",
        "gradient_start": "#f59e0b",
        "gradient_end": "#ef4444",
        "data_file": "retail_orders.csv",
        "description": "导出CSV、Excel，生成分析报告"
    },
    "project9": {
        "title": "项目09：综合案例一：销售数据分析",
        "project_num": "09",
        "primary_color": "#22c55e",
        "primary_rgb": "34, 197, 94",
        "gradient_start": "#22c55e",
        "gradient_end": "#a855f7",
        "data_file": "retail_orders.csv",
        "description": "综合运用所学知识，完成完整的销售数据分析项目"
    },
    "project10": {
        "title": "项目10：综合案例二：客户价值分析",
        "project_num": "10",
        "primary_color": "#8b5cf6",
        "primary_rgb": "139, 92, 246",
        "gradient_start": "#8b5cf6",
        "gradient_end": "#ec4899",
        "data_file": "retail_orders.csv",
        "description": "RFM模型分析，客户分群与价值评估"
    }
}

def get_color_class(color):
    return color.replace('#', '')

for project_id, info in projects.items():
    color_class = get_color_class(info['primary_color'])
    
    # Build HTML using string concatenation for JavaScript code
    html_parts = []
    
    # Use regular string formatting to avoid f-string issues with JS
    html_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Python训练营</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/prism.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-python.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/pyodide@0.24.1/dist/pyodide.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
        :root {
            --primary: {primary_color};
            --primary-rgb: {primary_rgb};
            --secondary: #8b5cf6;
            --accent: #00ff88;
            --bg-dark: #0a0a1a;
            --bg-panel: rgba(20, 20, 40, 0.8);
            --text: #e0e0e0;
            --text-muted: #9ca3af;
            --border: rgba({primary_rgb}, 0.2);
        }
        .light-theme { --bg-dark: #f3f4f6; --bg-panel: rgba(255, 255, 255, 0.95); --text: #1f2937; --text-muted: #6b7280; --border: rgba(0, 0, 0, 0.1); }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; background: var(--bg-dark); color: var(--text); min-height: 100vh; position: relative; overflow-x: hidden; transition: background 0.3s, color 0.3s; }
        body::before { content: ''; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: radial-gradient(circle at 20% 20%, rgba(var(--primary-rgb), 0.05) 0%, transparent 50%), radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.05) 0%, transparent 50%), linear-gradient(rgba(10, 10, 26, 0.95), rgba(10, 10, 26, 0.95)), repeating-linear-gradient(0deg, transparent, transparent 50px, rgba(var(--primary-rgb), 0.03) 50px, rgba(var(--primary-rgb), 0.03) 51px), repeating-linear-gradient(90deg, transparent, transparent 50px, rgba(var(--primary-rgb), 0.03) 50px, rgba(var(--primary-rgb), 0.03) 51px); pointer-events: none; z-index: -1; }
        .scanline { position: fixed; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, rgba(var(--primary-rgb), 0.5), transparent); animation: scanline 4s linear infinite; pointer-events: none; z-index: 9999; }
        @keyframes scanline { 0% { top: 0; opacity: 0; } 10% { opacity: 1; } 90% { opacity: 1; } 100% { top: 100%; opacity: 0; } }
        .glass-panel { background: var(--bg-panel); backdrop-filter: blur(10px); border: 1px solid var(--border); box-shadow: 0 0 20px rgba(var(--primary-rgb), 0.1), inset 0 0 20px rgba(var(--primary-rgb), 0.05); }
        .neon-border { border: 1px solid rgba(var(--primary-rgb), 0.5); box-shadow: 0 0 10px rgba(var(--primary-rgb), 0.3), inset 0 0 10px rgba(var(--primary-rgb), 0.1); }
        .neon-text { background: linear-gradient(135deg, {gradient_start}, {gradient_end}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; text-shadow: 0 0 30px rgba(var(--primary-rgb), 0.5); }
        .neon-button { background: linear-gradient(135deg, rgba(var(--primary-rgb), 0.2), rgba(139, 92, 246, 0.2)); border: 1px solid rgba(var(--primary-rgb), 0.5); color: var(--primary); transition: all 0.3s ease; position: relative; overflow: hidden; }
        .neon-button::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; background: linear-gradient(90deg, transparent, rgba(var(--primary-rgb), 0.3), transparent); transition: left 0.5s ease; }
        .neon-button:hover::before { left: 100%; }
        .neon-button:hover { box-shadow: 0 0 20px rgba(var(--primary-rgb), 0.5), 0 0 40px rgba(var(--primary-rgb), 0.3); border-color: var(--primary); }
        .run-button { background: linear-gradient(135deg, rgba(0, 255, 136, 0.2), rgba(0, 255, 136, 0.1)); border: 1px solid rgba(0, 255, 136, 0.5); color: #00ff88; }
        .run-button:hover { box-shadow: 0 0 20px rgba(0, 255, 136, 0.5), 0 0 40px rgba(0, 255, 136, 0.3); border-color: #00ff88; }
        .test-button { background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(139, 92, 246, 0.1)); border: 1px solid rgba(139, 92, 246, 0.5); color: #8b5cf6; }
        .test-button:hover { box-shadow: 0 0 20px rgba(139, 92, 246, 0.5), 0 0 40px rgba(139, 92, 246, 0.3); border-color: #8b5cf6; }
        .nav-tab { transition: all 0.3s ease; position: relative; }
        .nav-tab::after { content: ''; position: absolute; bottom: 0; left: 50%; width: 0; height: 2px; background: linear-gradient(90deg, {gradient_start}, {gradient_end}); transition: all 0.3s ease; transform: translateX(-50%); }
        .nav-tab:hover::after, .nav-tab.active::after { width: 80%; }
        .nav-tab.active { color: var(--primary); text-shadow: 0 0 10px rgba(var(--primary-rgb), 0.5); }
        .code-block { background: rgba(10, 10, 26, 0.9); border: 1px solid rgba(var(--primary-rgb), 0.3); color: var(--accent); padding: 1rem; border-radius: 0.5rem; overflow-x: auto; margin: 0.5rem 0; font-family: 'Courier New', monospace; }
        .practice-nav-btn { background: rgba(20, 20, 40, 0.6); border: 1px solid rgba(var(--primary-rgb), 0.2); color: var(--text); transition: all 0.3s ease; }
        .practice-nav-btn:hover { background: rgba(var(--primary-rgb), 0.1); border-color: rgba(var(--primary-rgb), 0.5); }
        .practice-nav-btn.active { background: rgba(var(--primary-rgb), 0.15); border-color: var(--primary); color: var(--primary); box-shadow: 0 0 15px rgba(var(--primary-rgb), 0.3); }
        .detail-card { background: rgba(20, 20, 40, 0.8); border: 1px solid rgba(255, 165, 0, 0.3); box-shadow: 0 0 15px rgba(255, 165, 0, 0.1); }
        .code-card { background: rgba(10, 10, 26, 0.95); border: 1px solid rgba(0, 255, 136, 0.3); box-shadow: 0 0 15px rgba(0, 255, 136, 0.1); }
        .tip-card { background: rgba(20, 20, 40, 0.8); border: 1px solid rgba(255, 215, 0, 0.3); box-shadow: 0 0 15px rgba(255, 215, 0, 0.1); }
        .code-editor { background: rgba(5, 5, 15, 0.95); color: var(--accent); font-family: 'Courier New', monospace; border: none; resize: none; outline: none; line-height: 1.6; tab-size: 4; }
        .code-editor::placeholder { color: rgba(0, 255, 136, 0.3); }
        .terminal-output { background: rgba(5, 5, 15, 0.95); color: var(--accent); font-family: 'Courier New', monospace; }
        .file-tab { background: rgba(30, 30, 50, 0.8); border-bottom: 1px solid rgba(var(--primary-rgb), 0.2); }
        .toolbar { background: rgba(20, 20, 40, 0.9); border: 1px solid rgba(var(--primary-rgb), 0.2); border-bottom: none; }
        .learning-card { background: var(--bg-panel); border: 1px solid var(--border); box-shadow: 0 0 20px rgba(var(--primary-rgb), 0.1); }
        .exam-card { background: var(--bg-panel); border: 1px solid rgba(139, 92, 246, 0.3); box-shadow: 0 0 20px rgba(139, 92, 246, 0.1); }
        input[type="radio"] { accent-color: var(--primary); }
        .score-circle { background: var(--bg-panel); border: 2px solid rgba(var(--primary-rgb), 0.5); box-shadow: 0 0 30px rgba(var(--primary-rgb), 0.3); }
        .theme-toggle { width: 50px; height: 26px; background: rgba(var(--primary-rgb), 0.2); border-radius: 13px; position: relative; cursor: pointer; transition: all 0.3s; }
        .theme-toggle::after { content: ''; position: absolute; width: 20px; height: 20px; background: var(--primary); border-radius: 50%; top: 3px; left: 3px; transition: all 0.3s; }
        .theme-toggle.active { background: rgba(var(--primary-rgb), 0.4); }
        .theme-toggle.active::after { left: 27px; }
        .modal { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.8); display: none; justify-content: center; align-items: center; z-index: 1000; }
        .modal.active { display: flex; }
        .modal-content { background: var(--bg-panel); border: 1px solid var(--border); border-radius: 1rem; max-width: 800px; max-height: 80vh; overflow-y: auto; padding: 2rem; }
        .tooltip { position: relative; }
        .tooltip::after { content: attr(data-tip); position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%); background: rgba(0, 0, 0, 0.9); color: white; padding: 0.5rem 1rem; border-radius: 0.25rem; font-size: 0.75rem; white-space: nowrap; opacity: 0; visibility: hidden; transition: all 0.3s; z-index: 100; }
        .tooltip:hover::after { opacity: 1; visibility: visible; }
        .status-badge { display: inline-flex; align-items: center; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 600; }
        .status-running { background: rgba(245, 158, 11, 0.2); color: #f59e0b; }
        .status-success { background: rgba(34, 197, 94, 0.2); color: #22c55e; }
        .status-error { background: rgba(239, 68, 68, 0.2); color: #ef4444; }
        .shortcut-key { background: rgba(0, 0, 0, 0.3); padding: 0.125rem 0.375rem; border-radius: 0.25rem; font-size: 0.75rem; border: 1px solid rgba(255, 255, 255, 0.1); }
        .history-item { padding: 0.5rem 1rem; border-bottom: 1px solid var(--border); cursor: pointer; transition: background 0.2s; }
        .history-item:hover { background: rgba(var(--primary-rgb), 0.1); }
        .difficulty-badge { padding: 0.125rem 0.5rem; border-radius: 0.25rem; font-size: 0.75rem; }
        .difficulty-easy { background: rgba(34, 197, 94, 0.2); color: #22c55e; }
        .difficulty-medium { background: rgba(245, 158, 11, 0.2); color: #f59e0b; }
        .difficulty-hard { background: rgba(239, 68, 68, 0.2); color: #ef4444; }
        .completion-animation { animation: completionPop 0.5s ease-out; }
        @keyframes completionPop { 0% { transform: scale(0); opacity: 0; } 50% { transform: scale(1.2); } 100% { transform: scale(1); opacity: 1; } }
        .autocomplete-dropdown { position: absolute; background: rgba(20, 20, 40, 0.98); border: 1px solid var(--border); border-radius: 0.5rem; max-height: 200px; overflow-y: auto; z-index: 1000; display: none; }
        .autocomplete-dropdown.active { display: block; }
        .autocomplete-item { padding: 0.5rem 1rem; cursor: pointer; transition: background 0.2s; }
        .autocomplete-item:hover { background: rgba(var(--primary-rgb), 0.2); }
        .loading-spinner { border: 3px solid rgba(var(--primary-rgb), 0.1); border-top-color: var(--primary); border-radius: 50%; width: 24px; height: 24px; animation: spin 1s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
        .toast { position: fixed; bottom: 2rem; right: 2rem; background: var(--bg-panel); border: 1px solid var(--border); border-radius: 0.5rem; padding: 1rem 1.5rem; z-index: 2000; transform: translateY(100px); opacity: 0; transition: all 0.3s; }
        .toast.show { transform: translateY(0); opacity: 1; }
        .kbd { display: inline-block; padding: 0.2em 0.5em; font: 80% sans-serif; color: var(--text); background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 3px; }
        .split-handle { background: rgba(var(--primary-rgb), 0.3); cursor: ns-resize; transition: background 0.2s; }
        .split-handle:hover { background: rgba(var(--primary-rgb), 0.5); }
    </style>
</head>
<body>
    <div class="scanline"></div>
    
    <nav class="glass-panel fixed w-full top-0 z-50">
        <div class="container mx-auto px-4 py-3">
            <div class="flex justify-between items-center">
                <div class="text-xl font-bold neon-text" style="font-family: 'Orbitron', sans-serif;">
                    <a href="../../index.html">Python训练营</a>
                </div>
                <div class="hidden md:flex items-center space-x-6">
                    <a href="../../index.html#home" class="text-gray-300 hover:text-{color_class}-400 font-medium transition-colors">首页</a>
                    <a href="../../index.html#projects" class="text-gray-300 hover:text-{color_class}-400 font-medium transition-colors">学习项目</a>
                    <a href="../../index.html#my-progress" class="text-gray-300 hover:text-{color_class}-400 font-medium transition-colors">学习进度</a>
                    <div class="flex items-center space-x-4 ml-4">
                        <div class="flex items-center space-x-2">
                            <i class="fa fa-moon-o text-gray-400"></i>
                            <div id="theme-toggle" class="theme-toggle" onclick="toggleTheme()"></div>
                            <i class="fa fa-sun-o text-yellow-400"></i>
                        </div>
                    </div>
                </div>
                <div class="md:hidden flex items-center space-x-2">
                    <div id="theme-toggle-mobile" class="theme-toggle" onclick="toggleTheme()"></div>
                    <button id="menu-toggle" class="text-{color_class}-400 focus:outline-none"><i class="fa fa-bars text-xl"></i></button>
                </div>
            </div>
            <div id="mobile-menu" class="md:hidden hidden mt-4 pb-2">
                <a href="../../index.html#home" class="block py-2 text-gray-300 hover:text-{color_class}-400">首页</a>
                <a href="../../index.html#projects" class="block py-2 text-gray-300 hover:text-{color_class}-400">学习项目</a>
                <a href="../../index.html#my-progress" class="block py-2 text-gray-300 hover:text-{color_class}-400">学习进度</a>
            </div>
        </div>
    </nav>

    <section class="pt-20 pb-8 relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-r from-{color_class}-900/30 to-purple-900/30"></div>
        <div class="container mx-auto px-4 relative z-10">
            <div class="flex items-center space-x-2 text-sm text-gray-400 mb-2">
                <a href="../../index.html" class="hover:text-{color_class}-400">首页</a>
                <i class="fa fa-chevron-right text-xs"></i>
                <a href="../../index.html#projects" class="hover:text-{color_class}-400">学习项目</a>
                <i class="fa fa-chevron-right text-xs"></i>
                <span class="text-{color_class}-400">{title}</span>
            </div>
            <div class="flex items-center">
                <span class="glass-panel text-{color_class}-400 px-4 py-1 rounded-full text-sm font-medium mr-4 neon-border" style="font-family: 'Orbitron', sans-serif;">PROJECT {project_num}</span>
                <h1 class="text-2xl md:text-3xl font-bold neon-text">{title}</h1>
                <button id="favorite-btn" class="ml-4 text-gray-400 hover:text-yellow-400 transition-colors" onclick="toggleFavorite()">
                    <i class="fa fa-star text-xl"></i>
                </button>
            </div>
            <p class="text-gray-400 mt-4">{description}</p>
            <div class="flex items-center mt-4 space-x-4">
                <span class="text-gray-500"><i class="fa fa-database mr-2 text-{color_class}-400"></i>数据文件: <span class="text-{color_class}-400">{data_file}</span></span>
                <span class="text-gray-500"><i class="fa fa-signal mr-2 text-green-400"></i>难度: <span class="difficulty-badge difficulty-medium">进阶</span></span>
                <span class="text-gray-500"><i class="fa fa-clock-o mr-2 text-yellow-400"></i>预计: <span class="text-yellow-400">45分钟</span></span>
            </div>
        </div>
    </section>

    <section class="glass-panel border-b border-{color_class}-500/20">
        <div class="container mx-auto px-4">
            <div class="flex overflow-x-auto">
                <button id="tab-learn" class="nav-tab active flex-shrink-0 px-6 py-4 text-{color_class}-400 font-medium">
                    <i class="fa fa-book mr-2"></i>学习
                </button>
                <button id="tab-practice" class="nav-tab flex-shrink-0 px-6 py-4 text-gray-400 hover:text-{color_class}-400 font-medium">
                    <i class="fa fa-code mr-2"></i>练习
                </button>
                <button id="tab-test" class="nav-tab flex-shrink-0 px-6 py-4 text-gray-400 hover:text-{color_class}-400 font-medium">
                    <i class="fa fa-file-text mr-2"></i>考试
                </button>
                <button id="tab-history" class="nav-tab flex-shrink-0 px-6 py-4 text-gray-400 hover:text-{color_class}-400 font-medium">
                    <i class="fa fa-history mr-2"></i>历史
                </button>
            </div>
        </div>
    </section>

    <section id="content-learn" class="py-8">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <div class="learning-card rounded-xl p-6 mb-8 neon-border">
                    <h2 class="text-xl font-bold neon-text mb-4">学习目标</h2>
                    <ul class="list-disc list-inside text-gray-400 space-y-2">
                        <li>掌握核心概念和基本操作方法</li>
                        <li>学会处理实际数据场景</li>
                        <li>能够独立完成相关分析任务</li>
                        <li>理解背后的原理和机制</li>
                        <li>为实际项目应用打下基础</li>
                    </ul>
                </div>

                <div class="learning-card rounded-xl p-6 mb-6">
                    <h3 class="text-lg font-bold text-{color_class}-400 mb-4">核心概念</h3>
                    <p class="text-gray-400 mb-4">本项目将带你深入学习相关知识，通过实际案例掌握核心技能。</p>
                    <div class="tip-card rounded-lg p-4">
                        <p class="text-yellow-400 text-sm"><i class="fa fa-lightbulb-o mr-2"></i><strong>提示：</strong>动手实践是最好的学习方式，建议边学边练。</p>
                    </div>
                </div>

                <div class="learning-card rounded-xl p-6 mb-6">
                    <h3 class="text-lg font-bold text-{color_class}-400 mb-4">代码示例</h3>
                    <div class="code-block">
                        <pre><code class="language-python">import pandas as pd
import numpy as np

data = {"column1": [1, 2, 3, 4, 5],
         "column2": ["A", "B", "C", "D", "E"]}
df = pd.DataFrame(data)

print(df)
print("数据形状:", df.shape)
print("数据统计:")
print(df.describe())</code></pre>
                    </div>
                    <button class="neon-button mt-3 px-4 py-2 rounded-lg text-sm" onclick="copyCode(this)">
                        <i class="fa fa-copy mr-2"></i>复制代码
                    </button>
                </div>

                <div class="text-center">
                    <button id="complete-learn" class="neon-button px-8 py-3 rounded-lg font-medium completion-animation">
                        <i class="fa fa-check-circle mr-2"></i>标记为已学习
                    </button>
                </div>
            </div>
        </div>
    </section>

    <section id="content-practice" class="py-8 hidden">
        <div class="container mx-auto px-4 h-[calc(100vh-220px)]">
            <div class="flex flex-col lg:flex-row h-full">
                <div class="lg:w-80 lg:h-full glass-panel rounded-xl overflow-hidden flex-shrink-0">
                    <div class="px-4 py-3 border-b border-{color_class}-500/30 flex justify-between items-center">
                        <h2 class="font-bold neon-text">练习导航</h2>
                        <button class="neon-button px-3 py-1 rounded text-xs">
                            <i class="fa fa-list mr-1"></i>全部
                        </button>
                    </div>
                    <div class="p-2 space-y-1">
                        <button id="practice-nav-1" class="practice-nav-btn active w-full text-left px-4 py-3 rounded-lg font-medium">
                            <i class="fa fa-code mr-2"></i>练习1：基础操作
                            <span class="difficulty-badge difficulty-easy text-xs ml-2">入门</span>
                        </button>
                        <button id="practice-nav-2" class="practice-nav-btn w-full text-left px-4 py-3 rounded-lg font-medium">
                            <i class="fa fa-code mr-2"></i>练习2：进阶应用
                            <span class="difficulty-badge difficulty-medium text-xs ml-2">进阶</span>
                        </button>
                        <button id="practice-nav-3" class="practice-nav-btn w-full text-left px-4 py-3 rounded-lg font-medium">
                            <i class="fa fa-code mr-2"></i>练习3：综合实战
                            <span class="difficulty-badge difficulty-hard text-xs ml-2">挑战</span>
                        </button>
                    </div>
                    
                    <div class="border-t border-{color_class}-500/20">
                        <div id="practice-detail-1" class="p-4">
                            <div class="detail-card rounded-lg p-3 mb-4">
                                <h3 class="font-bold text-orange-400 mb-2 flex items-center">
                                    <i class="fa fa-info-circle mr-2"></i>详细说明
                                </h3>
                                <p class="text-sm text-gray-400">掌握基本操作方法，完成基础练习任务。</p>
                            </div>
                            <div class="code-card rounded-lg p-3 mb-4">
                                <h3 class="font-bold text-green-400 mb-2 flex items-center">
                                    <i class="fa fa-lightbulb-o mr-2"></i>代码提示
                                </h3>
                                <pre class="text-xs text-green-400 overflow-x-auto"><code># 提示代码</code></pre>
                            </div>
                            <button class="neon-button w-full py-2 rounded-lg text-sm" onclick="showHint(1)">
                                <i class="fa fa-question-circle mr-2"></i>获取提示
                            </button>
                            <div id="hint-1" class="tip-card rounded-lg p-3 hidden">
                                <p class="text-sm text-gray-400">提示内容将显示在这里...</p>
                            </div>
                        </div>
                        
                        <div id="practice-detail-2" class="p-4 hidden">
                            <div class="detail-card rounded-lg p-3 mb-4">
                                <h3 class="font-bold text-orange-400 mb-2 flex items-center">
                                    <i class="fa fa-info-circle mr-2"></i>详细说明
                                </h3>
                                <p class="text-sm text-gray-400">运用所学知识完成进阶任务。</p>
                            </div>
                            <div class="code-card rounded-lg p-3 mb-4">
                                <h3 class="font-bold text-green-400 mb-2 flex items-center">
                                    <i class="fa fa-lightbulb-o mr-2"></i>代码提示
                                </h3>
                                <pre class="text-xs text-green-400 overflow-x-auto"><code># 进阶提示</code></pre>
                            </div>
                            <button class="neon-button w-full py-2 rounded-lg text-sm" onclick="showHint(2)">
                                <i class="fa fa-question-circle mr-2"></i>获取提示
                            </button>
                            <div id="hint-2" class="tip-card rounded-lg p-3 hidden">
                                <p class="text-sm text-gray-400">提示内容将显示在这里...</p>
                            </div>
                        </div>
                        
                        <div id="practice-detail-3" class="p-4 hidden">
                            <div class="detail-card rounded-lg p-3 mb-4">
                                <h3 class="font-bold text-orange-400 mb-2 flex items-center">
                                    <i class="fa fa-info-circle mr-2"></i>详细说明
                                </h3>
                                <p class="text-sm text-gray-400">综合运用所有技能完成挑战。</p>
                            </div>
                            <div class="code-card rounded-lg p-3 mb-4">
                                <h3 class="font-bold text-green-400 mb-2 flex items-center">
                                    <i class="fa fa-lightbulb-o mr-2"></i>代码提示
                                </h3>
                                <pre class="text-xs text-green-400 overflow-x-auto"><code># 综合提示</code></pre>
                            </div>
                            <button class="neon-button w-full py-2 rounded-lg text-sm" onclick="showHint(3)">
                                <i class="fa fa-question-circle mr-2"></i>获取提示
                            </button>
                            <div id="hint-3" class="tip-card rounded-lg p-3 hidden">
                                <p class="text-sm text-gray-400">提示内容将显示在这里...</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="flex-1 flex flex-col ml-0 lg:ml-4 mt-4 lg:mt-0 min-w-0">
                    <div class="toolbar rounded-t-xl px-4 py-3 flex flex-wrap items-center justify-between gap-2">
                        <div class="flex items-center space-x-2 flex-wrap">
                            <button id="run-code" class="run-button px-4 py-2 rounded-lg text-sm font-medium flex items-center tooltip" data-tip="Ctrl+Enter">
                                <i class="fa fa-play mr-2"></i>运行代码
                                <span class="shortcut-key ml-2">Ctrl+Enter</span>
                            </button>
                            <button id="reset-code" class="neon-button px-4 py-2 rounded-lg text-sm font-medium flex items-center">
                                <i class="fa fa-refresh mr-2"></i>重置
                            </button>
                            <button id="format-code" class="neon-button px-4 py-2 rounded-lg text-sm font-medium flex items-center">
                                <i class="fa fa-indent mr-2"></i>格式化
                            </button>
                            <button id="download-output" class="neon-button px-4 py-2 rounded-lg text-sm font-medium flex items-center">
                                <i class="fa fa-download mr-2"></i>下载
                            </button>
                        </div>
                        <div class="flex items-center space-x-2 flex-wrap">
                            <button class="neon-button px-4 py-2 rounded-lg text-sm font-medium flex items-center" onclick="showAnswer('basic')">
                                <i class="fa fa-eye mr-2"></i>基础答案
                            </button>
                            <button class="neon-button px-4 py-2 rounded-lg text-sm font-medium flex items-center" onclick="showAnswer('advanced')">
                                <i class="fa fa-star mr-2"></i>进阶答案
                            </button>
                            <button id="start-test" class="test-button px-4 py-2 rounded-lg text-sm font-medium flex items-center">
                                <i class="fa fa-file-text mr-2"></i>测试
                            </button>
                            <button id="auto-save" class="neon-button px-4 py-2 rounded-lg text-sm font-medium flex items-center">
                                <i class="fa fa-save mr-2"></i>保存
                            </button>
                        </div>
                    </div>
                    
                    <div class="flex-1 glass-panel rounded-b-xl overflow-hidden flex flex-col">
                        <div class="file-tab flex items-center justify-between px-4 py-2 text-gray-400 text-sm">
                            <div class="flex items-center">
                                <i class="fa fa-file-code-o mr-2 text-{color_class}-400"></i>
                                <span class="text-{color_class}-400">{project_id}/main.py</span>
                                <span id="unsaved-indicator" class="ml-2 text-yellow-400 hidden">●</span>
                            </div>
                            <div class="flex items-center space-x-3 text-xs">
                                <span id="cursor-position" class="text-gray-500">行 1, 列 1</span>
                                <span id="char-count" class="text-gray-500">0 字符</span>
                                <span id="execution-time" class="text-gray-500 hidden">执行: 0ms</span>
                            </div>
                        </div>
                        <div class="flex-1 relative">
                            <textarea id="code-editor" class="code-editor w-full h-full p-4 text-sm absolute inset-0" placeholder="在这里输入你的代码..."></textarea>
                            <div id="autocomplete-dropdown" class="autocomplete-dropdown"></div>
                        </div>
                        
                        <div class="split-handle h-2 cursor-ns-resize" id="output-splitter"></div>
                        
                        <div class="h-[40%]" id="output-panel">
                            <div class="file-tab flex items-center justify-between px-4 py-2 text-gray-400 text-sm">
                                <div class="flex items-center">
                                    <i class="fa fa-terminal mr-2 text-green-400"></i>
                                    <span class="text-green-400">执行结果</span>
                                    <span id="execution-status" class="status-badge ml-2 hidden"></span>
                                </div>
                                <div class="flex items-center space-x-2">
                                    <button class="text-gray-400 hover:text-white" onclick="clearOutput()">
                                        <i class="fa fa-trash"></i>
                                    </button>
                                    <button class="text-gray-400 hover:text-white" onclick="toggleFullscreen()">
                                        <i class="fa fa-expand"></i>
                                    </button>
                                </div>
                            </div>
                            <div id="code-output" class="terminal-output h-[calc(100%-40px)] p-4 overflow-auto text-sm">
                                <span class="text-{color_class}-400">&gt; 准备就绪，请输入代码后点击运行...</span>
                                <div class="mt-4 text-gray-500 text-xs">
                                    <p><span class="kbd">Ctrl</span> + <span class="kbd">Enter</span> 运行代码</p>
                                    <p><span class="kbd">Ctrl</span> + <span class="kbd">S</span> 保存代码</p>
                                    <p><span class="kbd">Ctrl</span> + <span class="kbd">F</span> 格式化代码</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="content-test" class="py-8 hidden">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <div class="exam-card rounded-xl p-6 mb-6">
                    <h2 class="text-2xl font-bold neon-text mb-2">项目考试</h2>
                    <p class="text-gray-400">共5道题目，每题20分，满分100分</p>
                    <div class="flex items-center mt-4 text-gray-500">
                        <i class="fa fa-clock-o mr-2 text-purple-400"></i>
                        <span>考试时间：<span class="text-purple-400">30分钟</span></span>
                    </div>
                </div>

                <div id="exam-questions">
                    <div class="exam-card rounded-xl p-6 mb-6">
                        <h3 class="font-bold text-gray-200 mb-4">1. 以下哪个选项是正确的？</h3>
                        <div class="space-y-2">
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q1" value="A" class="mr-2"><span>A) 选项A</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q1" value="B" class="mr-2"><span>B) 选项B</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q1" value="C" class="mr-2"><span>C) 选项C</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q1" value="D" class="mr-2"><span>D) 选项D</span></label>
                        </div>
                    </div>

                    <div class="exam-card rounded-xl p-6 mb-6">
                        <h3 class="font-bold text-gray-200 mb-4">2. 如何正确实现某个功能？</h3>
                        <div class="space-y-2">
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q2" value="A" class="mr-2"><span>A) 方法A</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q2" value="B" class="mr-2"><span>B) 方法B</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q2" value="C" class="mr-2"><span>C) 方法C</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q2" value="D" class="mr-2"><span>D) 方法D</span></label>
                        </div>
                    </div>

                    <div class="exam-card rounded-xl p-6 mb-6">
                        <h3 class="font-bold text-gray-200 mb-4">3. 以下代码的输出是什么？</h3>
                        <div class="code-block mb-4">
                            <pre><code class="language-python">print("Hello, World!")</code></pre>
                        </div>
                        <div class="space-y-2">
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q3" value="A" class="mr-2"><span>A) Hello</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q3" value="B" class="mr-2"><span>B) World</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q3" value="C" class="mr-2"><span>C) Hello, World!</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q3" value="D" class="mr-2"><span>D) 报错</span></label>
                        </div>
                    </div>

                    <div class="exam-card rounded-xl p-6 mb-6">
                        <h3 class="font-bold text-gray-200 mb-4">4. 哪个说法是正确的？</h3>
                        <div class="space-y-2">
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q4" value="A" class="mr-2"><span>A) 说法A</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q4" value="B" class="mr-2"><span>B) 说法B</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q4" value="C" class="mr-2"><span>C) 说法C</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q4" value="D" class="mr-2"><span>D) 说法D</span></label>
                        </div>
                    </div>

                    <div class="exam-card rounded-xl p-6 mb-6">
                        <h3 class="font-bold text-gray-200 mb-4">5. 如何优化这段代码？</h3>
                        <div class="space-y-2">
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q5" value="A" class="mr-2"><span>A) 方法A</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q5" value="B" class="mr-2"><span>B) 方法B</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q5" value="C" class="mr-2"><span>C) 方法C</span></label>
                            <label class="flex items-center text-gray-300 hover:text-{color_class}-400 cursor-pointer"><input type="radio" name="q5" value="D" class="mr-2"><span>D) 方法D</span></label>
                        </div>
                    </div>
                </div>

                <div class="text-center">
                    <button id="submit-exam" class="test-button px-8 py-3 rounded-lg font-medium">
                        <i class="fa fa-paper-plane mr-2"></i>提交考试
                    </button>
                </div>

                <div id="exam-result" class="mt-8 hidden">
                    <div class="exam-card rounded-xl p-6">
                        <div class="text-center">
                            <div id="score-circle" class="score-circle w-24 h-24 mx-auto rounded-full flex items-center justify-center mb-4"></div>
                            <h3 id="score-text" class="text-2xl font-bold neon-text mb-2"></h3>
                            <p id="result-text" class="text-gray-400"></p>
                        </div>
                        <div id="answer-details" class="mt-6"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="content-history" class="py-8 hidden">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <div class="glass-panel rounded-xl p-6 mb-6">
                    <h2 class="text-2xl font-bold neon-text mb-4">运行历史记录</h2>
                    <div id="code-history-list" class="space-y-2">
                        <p class="text-gray-400">暂无历史记录</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="glass-panel py-8 border-t border-{color_class}-500/20 mt-8">
        <div class="container mx-auto px-4 text-center">
            <p class="text-gray-500">© 2026 Python数据分析实战训练营 | {title}</p>
        </div>
    </footer>

    <div id="answer-modal" class="modal">
        <div class="modal-content">
            <div class="flex justify-between items-center mb-4">
                <h3 id="modal-title" class="text-xl font-bold neon-text">参考答案</h3>
                <button onclick="closeModal()" class="text-gray-400 hover:text-white">
                    <i class="fa fa-times text-xl"></i>
                </button>
            </div>
            <div id="modal-content" class="code-block"></div>
        </div>
    </div>

    <div id="toast" class="toast">
        <div class="flex items-center">
            <i id="toast-icon" class="fa fa-check-circle text-green-400 mr-3"></i>
            <span id="toast-message"></span>
        </div>
    </div>

    <div id="pyodide-loading" class="fixed inset-0 bg-black/50 flex items-center justify-center z-[1001]">
        <div class="text-center">
            <div class="loading-spinner mx-auto mb-4"></div>
            <p class="text-white">正在加载Python环境...</p>
        </div>
    </div>

    <script>
        let pyodide = null;
        let isLoading = true;
        let codeHistory = [];
        let favorites = JSON.parse(localStorage.getItem("favorites") || "[]");
        let codeVersions = JSON.parse(localStorage.getItem("codeVersions") || "{{}}");
        let currentPractice = 1;
        let isModified = false;
        let executionStartTime = 0;
        
        const pythonKeywords = ["import", "from", "def", "class", "if", "else", "for", "while", "return", "try", "except", "True", "False", "None"];
        const pandasFunctions = ["pd", "DataFrame", "read_csv", "to_csv", "merge", "concat", "groupby", "dropna", "fillna", "describe", "head", "tail", "loc", "iloc"];

        async function initPyodide() {
            try {
                pyodide = await loadPyodide({{ indexURL: "https://cdn.jsdelivr.net/npm/pyodide@0.24.1/" }});
                await pyodide.loadPackage(["pandas", "numpy", "pytz"]);
                document.getElementById("pyodide-loading").style.display = "none";
                isLoading = false;
                showToast("Python环境就绪", "success");
            }} catch (error) {{
                document.getElementById("pyodide-loading").innerHTML = '<div class="text-center"><p class="text-red-400 mb-4">Python环境加载失败</p><button onclick="location.reload()" class="neon-button px-4 py-2 rounded">重试</button></div>';
            }}
        }

        function showToast(message, type = "success") {{
            const toast = document.getElementById("toast");
            const icon = document.getElementById("toast-icon");
            const msg = document.getElementById("toast-message");
            msg.textContent = message;
            if (type === "success") icon.className = "fa fa-check-circle text-green-400 mr-3";
            else if (type === "error") icon.className = "fa fa-times-circle text-red-400 mr-3";
            else icon.className = "fa fa-exclamation-circle text-yellow-400 mr-3";
            toast.classList.add("show");
            setTimeout(() => toast.classList.remove("show"), 3000);
        }}

        function toggleTheme() {{
            document.body.classList.toggle("light-theme");
            document.querySelectorAll(".theme-toggle").forEach(t => t.classList.toggle("active"));
            localStorage.setItem("theme", document.body.classList.contains("light-theme") ? "light" : "dark");
        }}

        function toggleFavorite() {{
            const btn = document.getElementById("favorite-btn");
            const isFav = btn.classList.toggle("active");
            if (isFav) {{
                btn.innerHTML = '<i class="fa fa-star text-xl text-yellow-400"></i>';
                if (!favorites.includes("{project_id}")) {{
                    favorites.push("{project_id}");
                    localStorage.setItem("favorites", JSON.stringify(favorites));
                    showToast("已添加到收藏", "success");
                }}
            }} else {{
                btn.innerHTML = '<i class="fa fa-star text-xl"></i>';
                favorites = favorites.filter(f => f !== "{project_id}");
                localStorage.setItem("favorites", JSON.stringify(favorites));
            }}
        }}

        function showHint(practiceId) {{
            const hint = document.getElementById("hint-" + practiceId);
            hint.classList.toggle("hidden");
        }}

        function copyCode(btn) {{
            const code = btn.previousElementSibling.querySelector("code").textContent;
            navigator.clipboard.writeText(code);
            btn.innerHTML = '<i class="fa fa-check mr-2"></i>已复制';
            setTimeout(() => btn.innerHTML = '<i class="fa fa-copy mr-2"></i>复制代码', 2000);
        }}

        function showAnswer(type) {{
            const modal = document.getElementById("answer-modal");
            const title = document.getElementById("modal-title");
            const content = document.getElementById("modal-content");
            const answers = {{
                basic: {{
                    1: `import pandas as pd

data = {{"col1": [1, 2, 3], "col2": [4, 5, 6]}}
df = pd.DataFrame(data)
print(df)`,
                    2: `import pandas as pd

# 进阶示例
df = pd.DataFrame(...)
result = df.groupby("col").sum()
print(result)`,
                    3: `import pandas as pd

# 综合实战
# 完成所有步骤
print("完成")`
                }},
                advanced: {{
                    1: `import pandas as pd
import numpy as np

# 高效实现
df = pd.DataFrame(...)
print(df)`,
                    2: `import pandas as pd
import numpy as np

# 优化版本
df = pd.DataFrame(...)
result = df.agg({{"col": ["sum", "mean"]}})
print(result)`,
                    3: `import pandas as pd
import numpy as np

# 完整解决方案
print("所有功能实现")`
                }}
            }};
            title.textContent = type === "basic" ? "基础参考答案" : "进阶参考答案";
            content.innerHTML = "<pre><code class="language-python">" + answers[type][currentPractice] + "</code></pre>";
            modal.classList.add("active");
            Prism.highlightAll();
        }}

        function closeModal() {{
            document.getElementById("answer-modal").classList.remove("active");
        }}

        function clearOutput() {{
            document.getElementById("code-output").innerHTML = '<span class="text-{color_class}-400">&gt; 输出已清空</span>';
        }}

        function toggleFullscreen() {{
            const panel = document.getElementById("output-panel");
            panel.classList.toggle("h-full");
            panel.classList.toggle("h-[40%]");
        }}

        function updateCursorPosition() {{
            const editor = document.getElementById("code-editor");
            const cursorPos = editor.selectionStart;
            const text = editor.value.substring(0, cursorPos);
            const lines = text.split("\\n");
            const line = lines.length;
            const col = lines[lines.length - 1].length + 1;
            document.getElementById("cursor-position").textContent = "行 " + line + ", 列 " + col;
        }}

        async function runCode() {{
            const code = document.getElementById("code-editor").value;
            const output = document.getElementById("code-output");
            const status = document.getElementById("execution-status");
            
            if (!code.trim()) {{
                showToast("请输入代码", "warning");
                return;
            }}

            executionStartTime = performance.now();
            status.className = "status-badge ml-2 status-running";
            status.textContent = "运行中";
            status.classList.remove("hidden");
            
            output.innerHTML = '<span class="text-yellow-400">&gt; 正在执行...</span>\\n\\n';

            if (isLoading) {{
                output.innerHTML += '<span class="text-red-400">错误: Python环境未加载完成</span>';
                return;
            }}

            try {{
                const result = await pyodide.runPythonAsync(code);
                const executionTime = Math.round(performance.now() - executionStartTime);
                document.getElementById("execution-time").textContent = "执行: " + executionTime + "ms";
                document.getElementById("execution-time").classList.remove("hidden");
                status.className = "status-badge ml-2 status-success";
                status.textContent = "成功";
                let outputText = result ? String(result) : "";
                output.innerHTML = '<span class="text-green-400">&gt; 执行完成 (' + executionTime + 'ms)</span>\\n\\n';
                if (outputText) output.innerHTML += '<span class="text-green-400">' + outputText + "</span>";
                saveToHistory(code, outputText, executionTime, true);
            }} catch (error) {{
                const executionTime = Math.round(performance.now() - executionStartTime);
                status.className = "status-badge ml-2 status-error";
                status.textContent = "失败";
                output.innerHTML = '<span class="text-red-400">&gt; 执行错误 (' + executionTime + 'ms)</span>\\n\\n';
                output.innerHTML += '<span class="text-red-400">' + error.message + "</span>";
                saveToHistory(code, error.message, executionTime, false);
            }}
            output.scrollTop = output.scrollHeight;
        }}

        function saveToHistory(code, output, time, success) {{
            const entry = {{ id: Date.now(), code, output, time, success, timestamp: new Date().toLocaleString(), practice: currentPractice }};
            codeHistory.unshift(entry);
            if (codeHistory.length > 50) codeHistory.pop();
            localStorage.setItem("codeHistory_{project_id}", JSON.stringify(codeHistory));
            updateHistoryDisplay();
        }}

        function updateHistoryDisplay() {{
            const list = document.getElementById("code-history-list");
            if (codeHistory.length === 0) {{
                list.innerHTML = '<p class="text-gray-400">暂无历史记录</p>';
                return;
            }}
            list.innerHTML = codeHistory.slice(0, 10).map(entry => '<div class="history-item" onclick="loadHistory(' + entry.id + ')"><div class="flex justify-between items-start"><div class="flex-1"><div class="flex items-center space-x-2"><span class="status-badge ' + (entry.success ? "status-success" : "status-error") + '">' + (entry.success ? "成功" : "失败") + '</span><span class="text-gray-500 text-xs">' + entry.timestamp + '</span></div><p class="text-sm text-gray-300 mt-1 truncate">' + entry.code.substring(0, 50) + '...</p></div></div></div>').join("");
        }}

        function loadHistory(id) {{
            const entry = codeHistory.find(e => e.id === id);
            if (entry) {{
                document.getElementById("code-editor").value = entry.code;
                document.getElementById("code-output").innerHTML = '<span class="text-green-400">&gt; 已加载历史代码</span>\\n\\n' + entry.output;
                showToast("已加载历史代码", "success");
            }}
        }}

        function formatCode() {{
            const editor = document.getElementById("code-editor");
            let code = editor.value;
            code = code.replace(/\\t/g, "    ");
            const lines = code.split("\\n");
            let indent = 0;
            const formattedLines = lines.map(line => {{
                const trimmed = line.trim();
                if (!trimmed) return "";
                if (trimmed.charAt(0) === "}" || trimmed.charAt(0) === ")" || trimmed.charAt(0) === "]") indent = Math.max(0, indent - 1);
                const formatted = " ".repeat(indent * 4) + trimmed;
                if (trimmed.endsWith("{{") || trimmed.endsWith("(") || trimmed.endsWith("[") || trimmed.endsWith(":")) indent++;
                return formatted;
            }});
            editor.value = formattedLines.join("\\n");
            showToast("代码已格式化", "success");
        }}

        function downloadOutput() {{
            const output = document.getElementById("code-output").textContent;
            const blob = new Blob([output], {{ type: "text/plain" }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "output_" + Date.now() + ".txt";
            a.click();
            URL.revokeObjectURL(url);
            showToast("输出已下载", "success");
        }}

        const codeTemplates = {{
            1: `import pandas as pd
import numpy as np

data = {{
    "product": ["A", "B", "C", "D"],
    "sales": [100, 200, 150, 300]
}}
df = pd.DataFrame(data)

print("原始数据:")
print(df)

# 请完成练习任务`,
            2: `import pandas as pd
import numpy as np

data = {{
    "region": ["华北", "华东", "华南", "华北", "华东"],
    "sales": [100, 200, 150, 300, 250]
}}
df = pd.DataFrame(data)

print("原始数据:")
print(df)

# 请完成进阶任务`,
            3: `import pandas as pd
import numpy as np

# 综合实战数据
df = pd.DataFrame(...)

# 请完成综合任务
print("请开始练习")`
        }};

        function updateCodeEditor(practiceNum) {{
            currentPractice = practiceNum;
            const editor = document.getElementById("code-editor");
            const key = "{project_id}_practice" + practiceNum;
            if (!codeVersions[key]) {{
                editor.value = codeTemplates[practiceNum];
            }} else {{
                editor.value = codeVersions[key];
            }}
            document.getElementById("code-output").innerHTML = '<span class="text-{color_class}-400">&gt; 准备就绪，请输入代码后点击运行...</span>';
            document.getElementById("unsaved-indicator").classList.add("hidden");
            isModified = false;
        }}

        function autoSave() {{
            const editor = document.getElementById("code-editor");
            const key = "{project_id}_practice" + currentPractice;
            codeVersions[key] = editor.value;
            localStorage.setItem("codeVersions", JSON.stringify(codeVersions));
            document.getElementById("unsaved-indicator").classList.add("hidden");
            isModified = false;
            showToast("代码已保存", "success");
        }}

        document.getElementById("menu-toggle").addEventListener("click", function() {{
            document.getElementById("mobile-menu").classList.toggle("hidden");
        }});

        const tabs = ["learn", "practice", "test", "history"];
        tabs.forEach(tab => {{
            document.getElementById("tab-" + tab).addEventListener("click", function() {{
                tabs.forEach(t => {{
                    document.getElementById("content-" + t).classList.add("hidden");
                    document.getElementById("tab-" + t).classList.remove("active");
                }});
                document.getElementById("content-" + tab).classList.remove("hidden");
                document.getElementById("tab-" + tab).classList.add("active");
                if (tab === "history") updateHistoryDisplay();
            }});
        }});

        document.getElementById("complete-learn").addEventListener("click", function() {{
            saveProgress("{project_id}", "learned");
            showToast("已标记为已学习", "success");
            this.classList.add("completion-animation");
        }});

        function saveProgress(projectId, type) {{
            const progress = JSON.parse(localStorage.getItem("learningProgress") || "{{}}");
            if (!progress[projectId]) progress[projectId] = {{ learned: false, practiced: false, tested: false }};
            progress[projectId][type] = true;
            localStorage.setItem("learningProgress", JSON.stringify(progress));
        }}

        const practiceNavButtons = ["practice-nav-1", "practice-nav-2", "practice-nav-3"];
        const practiceDetails = ["practice-detail-1", "practice-detail-2", "practice-detail-3"];
        
        practiceNavButtons.forEach((btn, index) => {{
            document.getElementById(btn).addEventListener("click", function() {{
                practiceNavButtons.forEach((b, i) => {{
                    document.getElementById(b).classList.remove("active");
                    document.getElementById(practiceDetails[i]).classList.add("hidden");
                }});
                this.classList.add("active");
                document.getElementById(practiceDetails[index]).classList.remove("hidden");
                updateCodeEditor(index + 1);
            }});
        }});

        document.getElementById("run-code").addEventListener("click", runCode);
        document.getElementById("reset-code").addEventListener("click", function() {{ updateCodeEditor(currentPractice); showToast("代码已重置", "success"); }});
        document.getElementById("format-code").addEventListener("click", formatCode);
        document.getElementById("download-output").addEventListener("click", downloadOutput);
        document.getElementById("auto-save").addEventListener("click", autoSave);
        
        document.getElementById("start-test").addEventListener("click", function() {{
            document.getElementById("content-practice").classList.add("hidden");
            document.getElementById("content-test").classList.remove("hidden");
            document.getElementById("tab-practice").classList.remove("active");
            document.getElementById("tab-test").classList.add("active");
        }});

        document.getElementById("code-editor").addEventListener("input", function() {{
            document.getElementById("unsaved-indicator").classList.remove("hidden");
            isModified = true;
            document.getElementById("char-count").textContent = this.value.length + " 字符";
        }});

        document.getElementById("code-editor").addEventListener("keyup", updateCursorPosition);
        document.getElementById("code-editor").addEventListener("click", updateCursorPosition);

        document.getElementById("code-editor").addEventListener("keydown", function(e) {{
            if (e.ctrlKey && e.key === "Enter") {{ e.preventDefault(); runCode(); }}
            else if (e.ctrlKey && e.key === "s") {{ e.preventDefault(); autoSave(); }}
            else if (e.ctrlKey && e.key === "f") {{ e.preventDefault(); formatCode(); }}
            else if (e.key === "Tab") {{ e.preventDefault(); const start = this.selectionStart; const end = this.selectionEnd; this.value = this.value.substring(0, start) + "    " + this.value.substring(end); this.selectionStart = this.selectionEnd = start + 4; }}
            updateCursorPosition();
        }});

        const correctAnswers = {{ q1: "C", q2: "B", q3: "C", q4: "B", q5: "C" }};

        document.getElementById("submit-exam").addEventListener("click", function() {{
            let score = 0;
            const answers = {{}};
            Object.keys(correctAnswers).forEach(q => {{
                const selected = document.querySelector("input[name="" + q + ""]:checked");
                answers[q] = selected ? selected.value : null;
                if (answers[q] === correctAnswers[q]) score += 20;
            }});
            document.getElementById("exam-questions").classList.add("hidden");
            document.getElementById("submit-exam").classList.add("hidden");
            document.getElementById("exam-result").classList.remove("hidden");
            const scoreCircle = document.getElementById("score-circle");
            const scoreText = document.getElementById("score-text");
            const resultText = document.getElementById("result-text");
            const answerDetails = document.getElementById("answer-details");
            scoreText.textContent = "得分：" + score + "/100";
            if (score >= 80) {{ scoreCircle.innerHTML = "<span class="text-4xl">🎉</span>"; resultText.textContent = "优秀！"; resultText.className = "text-green-400"; saveProgress("{project_id}", "tested"); }}
            else if (score >= 60) {{ scoreCircle.innerHTML = "<span class="text-4xl">👍</span>"; resultText.textContent = "良好！"; resultText.className = "text-yellow-400"; }}
            else {{ scoreCircle.innerHTML = "<span class="text-4xl">📚</span>"; resultText.textContent = "继续加油！"; resultText.className = "text-orange-400"; }}
            let details = '<h4 class="font-bold text-gray-300 mb-4">答案详情</h4><div class="space-y-2">';
            Object.keys(correctAnswers).forEach((q, i) => {{ const isCorrect = answers[q] === correctAnswers[q]; details += '<p class="' + (isCorrect ? "text-green-400" : "text-red-400") + '">' + (i+1) + ". " + (answers[q] || "未作答") + " / " + correctAnswers[q] + " " + (isCorrect ? "✓" : "✗") + "</p>"; }});
            details += "</div>";
            answerDetails.innerHTML = details;
        }});

        document.getElementById("answer-modal").addEventListener("click", function(e) {{ if (e.target === this) closeModal(); }});
        document.addEventListener("keydown", function(e) {{ if (e.key === "Escape") closeModal(); }});

        setInterval(() => {{ if (isModified) autoSave(); }}, 30000);

        if (localStorage.getItem("theme") === "light") {{
            document.body.classList.add("light-theme");
            document.querySelectorAll(".theme-toggle").forEach(t => t.classList.add("active"));
        }}

        if (favorites.includes("{project_id}")) {{
            document.getElementById("favorite-btn").classList.add("active");
            document.getElementById("favorite-btn").innerHTML = '<i class="fa fa-star text-xl text-yellow-400"></i>';
        }}

        const savedHistory = localStorage.getItem("codeHistory_{project_id}");
        if (savedHistory) codeHistory = JSON.parse(savedHistory);

        initPyodide();
        updateCodeEditor(1);
        Prism.highlightAll();
    </script>
</body>
</html>'''
    
    html_content = html_template.format(
        title=info['title'],
        project_num=info['project_num'],
        primary_color=info['primary_color'],
        primary_rgb=info['primary_rgb'],
        gradient_start=info['gradient_start'],
        gradient_end=info['gradient_end'],
        data_file=info['data_file'],
        description=info['description'],
        color_class=color_class,
        project_id=project_id
    )

    with open(f'/workspace/projects/{project_id}/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated: {project_id}")

print("\n✓ All 9 projects upgraded successfully!")
