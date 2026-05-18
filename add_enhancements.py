#!/usr/bin/env python3
import os
import re

# 项目配置
PROJECTS = {
    1: {
        'title': '数据清洗实战',
        'icon': '🧹',
        'level': '入门',
        'level_class': 'badge-easy',
        'dataset': 'retail_orders.csv',
        'search_content': '''
                    { title: '数据清洗', section: '1.1 什么是数据清洗', content: '缺失值、重复值、异常值、格式不一致' },
                    { title: 'Pandas 读取数据', section: '1.2 Pandas 读取数据', content: 'pd.read_csv()' },
                    { title: '缺失值处理', section: '2.1 查找缺失值', content: 'isnull() isna() dropna() fillna()' },
                    { title: '重复值', section: '3.1 处理重复值', content: 'duplicated() drop_duplicates()' },
                    { title: '异常值', section: '3.2 检测异常值', content: 'IQR 四分位距 quantile()' }
        '''
    },
    2: {
        'title': '分组聚合分析',
        'icon': '📊',
        'level': '入门',
        'level_class': 'badge-easy',
        'dataset': 'retail_orders.csv',
        'search_content': '''
                    { title: '分组聚合', section: '分组聚合基础', content: 'groupby sum mean count' },
                    { title: '聚合函数', section: '常用聚合函数', content: 'agg pivot_table unstack' },
                    { title: '多维度分组', section: '多列分组', content: '多维度分析' }
        '''
    },
    3: {
        'title': '购物篮分析',
        'icon': '🛒',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'market_basket.csv',
        'search_content': '''
                    { title: '购物篮分析', section: '关联规则', content: 'Apriori 支持度 置信度' },
                    { title: '关联规则', section: '关联分析', content: '提升度 商品关联' }
        '''
    },
    4: {
        'title': '客户聚类分析',
        'icon': '👥',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'customer_features.csv',
        'search_content': '''
                    { title: '聚类分析', section: 'K-Means', content: 'KMeans 簇 聚类中心' },
                    { title: '客户分群', section: '客户细分', content: '特征工程 标准化' }
        '''
    },
    5: {
        'title': '数据可视化',
        'icon': '📈',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'retail_orders.csv',
        'search_content': '''
                    { title: '数据可视化', section: 'Matplotlib', content: 'plot bar chart' },
                    { title: '图表类型', section: '可视化', content: '折线图 柱状图 饼图' }
        '''
    },
    6: {
        'title': 'A/B测试分析',
        'icon': '🔬',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'ab_test.csv',
        'search_content': '''
                    { title: 'A/B测试', section: '实验设计', content: '对照组 实验组' },
                    { title: '统计分析', section: '假设检验', content: 't检验 p值 显著性' }
        '''
    },
    7: {
        'title': '时间序列分析',
        'icon': '⏰',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'time_series_sales.csv',
        'search_content': '''
                    { title: '时间序列', section: '趋势分析', content: '趋势 季节性 周期性' },
                    { title: '预测模型', section: ' forecasting', content: '移动平均 指数平滑' }
        '''
    },
    8: {
        'title': '特征工程',
        'icon': '🔧',
        'level': '高级',
        'level_class': 'badge-hard',
        'dataset': 'customer_features.csv',
        'search_content': '''
                    { title: '特征工程', section: '特征处理', content: '归一化 标准化 编码' },
                    { title: '特征选择', section: '特征提取', content: 'PCA 主成分分析' }
        '''
    },
    9: {
        'title': '异常值检测',
        'icon': '🎯',
        'level': '高级',
        'level_class': 'badge-hard',
        'dataset': 'customer_features.csv',
        'search_content': '''
                    { title: '异常值检测', section: '检测方法', content: 'IQR Z-score 孤立森林' },
                    { title: '数据质量', section: '异常处理', content: '删除 替换 保留' }
        '''
    },
    10: {
        'title': '多数据集合并',
        'icon': '🔗',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'retail_orders.csv',
        'search_content': '''
                    { title: '数据合并', section: 'Merge Join', content: 'merge concat join' },
                    { title: '数据整合', section: '表连接', content: '内连接 外连接 左连接 右连接' }
        '''
    }
}

# 需要添加的增强功能
SEARCH_HTML = '''
        <!-- 搜索功能 -->
        <div class="search-container">
            <div class="search-box">
                <span class="search-icon" aria-hidden="true">🔍</span>
                <input type="search" class="search-input" placeholder="搜索本项目内容... (按 / 键快速搜索)" 
                       aria-label="搜索项目内容" id="search-input" accesskey="/">
            </div>
            <div class="search-results" id="search-results" aria-live="polite"></div>
        </div>
'''

# Pyodide 和增强功能的 JavaScript
ENHANCED_JS = '''
    <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
    
    <script>
        // 全局变量
        let pyodide = null;
        let isLoading = false;
        let testAnswers = {};
        let totalQuestions = 5;
        let currentProgress = { chapters: 0, exercises: 0, score: 0 };
        
        // 初始化 Pyodide
        async function initPyodide() {
            if (pyodide || isLoading) return;
            isLoading = true;
            
            const btn = document.getElementById('run-btn');
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = '<span class="loading-spinner"></span> 加载中...';
            }
            
            try {
                pyodide = await loadPyodide({
                    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"
                });
                console.log('Pyodide 加载成功！');
            } catch (error) {
                console.error('Pyodide 加载失败:', error);
            } finally {
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = '▶️ 运行代码';
                }
                isLoading = false;
            }
        }
        
        // 运行代码
        async function runCode() {
            const code = document.getElementById('code-input')?.value || document.querySelector('.code-textarea')?.value;
            if (!code) return;
            
            const outputBox = document.getElementById('output-box') || document.querySelector('.output-box');
            const outputContent = document.getElementById('output-content') || document.querySelector('.output-content');
            const btn = document.getElementById('run-btn');
            
            if (outputBox) outputBox.style.display = 'block';
            if (outputContent) {
                outputContent.textContent = '正在执行...';
                outputContent.className = 'output-content';
            }
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = '<span class="loading-spinner"></span> 运行中...';
            }
            
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
                    if (outputContent) {
                        outputContent.textContent = stderr;
                        outputContent.className = 'output-content error';
                    }
                } else {
                    if (outputContent) {
                        outputContent.textContent = stdout || '(代码执行完成，无输出)';
                        outputContent.className = 'output-content success';
                    }
                }
            } catch (error) {
                if (outputContent) {
                    outputContent.textContent = '错误: ' + error.message;
                    outputContent.className = 'output-content error';
                }
            } finally {
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = '▶️ 运行代码';
                }
            }
        }
        
        // 重置代码
        function resetCode() {
            const textarea = document.getElementById('code-input') || document.querySelector('.code-textarea');
            if (textarea && textarea.dataset.original) {
                textarea.value = textarea.dataset.original;
            }
            const outputBox = document.getElementById('output-box') || document.querySelector('.output-box');
            if (outputBox) outputBox.style.display = 'none';
        }
        
        // 复制代码
        function copyCode() {
            const code = document.getElementById('code-input')?.value || document.querySelector('.code-textarea')?.value;
            if (code) {
                navigator.clipboard.writeText(code).then(() => {
                    alert('代码已复制到剪贴板！');
                });
            }
        }
        
        // 标签切换
        function showTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
                tab.setAttribute('aria-selected', 'false');
            });
            
            const targetTab = document.getElementById(tabName + '-tab');
            const targetBtn = document.getElementById('tab-' + tabName);
            
            if (targetTab) targetTab.classList.add('active');
            if (targetBtn) {
                targetBtn.classList.add('active');
                targetBtn.setAttribute('aria-selected', 'true');
            }
        }
        
        // 选择练习选项
        function selectOption(btn, questionId, option, isCorrect) {
            const questionBox = btn.closest('.question-box');
            const allOptions = questionBox.querySelectorAll('.option-btn');
            allOptions.forEach(opt => opt.classList.remove('selected'));
            btn.classList.add('selected');
            
            const explanation = document.getElementById('explanation-' + questionId);
            if (explanation) {
                explanation.style.display = 'block';
                if (isCorrect) {
                    btn.classList.add('correct');
                    saveProgress('exercise', questionId);
                } else {
                    btn.classList.add('wrong');
                }
            }
        }
        
        // 测试选项
        function selectTestOption(btn, questionId, option, isCorrect) {
            const questionBox = btn.closest('.question-box');
            const allOptions = questionBox.querySelectorAll('.option-btn');
            allOptions.forEach(opt => opt.classList.remove('selected'));
            btn.classList.add('selected');
            testAnswers[questionId] = isCorrect;
        }
        
        // 提交测试
        function submitTest() {
            if (Object.keys(testAnswers).length < totalQuestions) {
                alert('请先回答所有问题！');
                return;
            }
            
            const questionBoxes = document.querySelectorAll('#test-tab .question-box');
            questionBoxes.forEach((box, i) => {
                const options = box.querySelectorAll('.option-btn');
                options.forEach(opt => {
                    if (opt.classList.contains('selected')) {
                        const questionNum = i + 1;
                        const isCorrect = testAnswers[questionNum];
                        if (isCorrect) {
                            opt.classList.remove('selected');
                            opt.classList.add('correct');
                        } else {
                            opt.classList.remove('selected');
                            opt.classList.add('wrong');
                        }
                    }
                });
            });
            
            let correctCount = Object.values(testAnswers).filter(v => v).length;
            let score = Math.round((correctCount / totalQuestions) * 100);
            
            const scoreEl = document.getElementById('final-score');
            if (scoreEl) scoreEl.textContent = score + '分';
            
            let message = '';
            let icon = '';
            if (score >= 80) {
                message = '太棒了！你已经掌握了这个项目！';
                icon = '🎉';
            } else if (score >= 60) {
                message = '不错！继续加油！';
                icon = '💪';
            } else {
                message = '再去复习一下吧！';
                icon = '📚';
            }
            
            const msgEl = document.getElementById('result-message');
            const iconEl = document.getElementById('result-icon');
            if (msgEl) msgEl.textContent = message;
            if (iconEl) iconEl.textContent = icon;
            
            const resultEl = document.getElementById('test-result');
            if (resultEl) resultEl.style.display = 'block';
            
            saveProgress('test', score);
        }
        
        // 重置测试
        function resetTest() {
            testAnswers = {};
            document.querySelectorAll('#test-tab .option-btn').forEach(opt => {
                opt.classList.remove('selected', 'correct', 'wrong');
            });
            const resultEl = document.getElementById('test-result');
            if (resultEl) resultEl.style.display = 'none';
        }
        
        // 本地存储 - 保存进度
        function saveProgress(type, value) {
            const projectId = 'project' + window.location.pathname.match(/project(\d+)/)?.[1] || '1';
            let progress = JSON.parse(localStorage.getItem('learningProgress') || '{}');
            
            if (!progress[projectId]) {
                progress[projectId] = { chapters: 0, exercises: 0, score: 0 };
            }
            
            if (type === 'chapter') {
                progress[projectId].chapters = Math.max(progress[projectId].chapters, value);
            } else if (type === 'exercise') {
                progress[projectId].exercises = Math.max(progress[projectId].exercises, value);
            } else if (type === 'test') {
                progress[projectId].score = Math.max(progress[projectId].score, value);
            }
            
            localStorage.setItem('learningProgress', JSON.stringify(progress));
            updateProgressDisplay();
        }
        
        // 更新进度显示
        function updateProgressDisplay() {
            const projectId = 'project' + window.location.pathname.match(/project(\d+)/)?.[1] || '1';
            const progress = JSON.parse(localStorage.getItem('learningProgress') || '{}')[projectId] || { chapters: 0, exercises: 0, score: 0 };
            
            const chaptersEl = document.getElementById('chapters-learned');
            const exercisesEl = document.getElementById('exercises-done');
            const scoreEl = document.getElementById('test-score');
            
            if (chaptersEl) chaptersEl.textContent = progress.chapters + '/4';
            if (exercisesEl) exercisesEl.textContent = progress.exercises + '/3';
            if (scoreEl) scoreEl.textContent = progress.score;
            
            const percentage = Math.round((progress.chapters / 4) * 100);
            const percentEl = document.getElementById('progress-percentage');
            const circleEl = document.getElementById('progress-circle-inner');
            
            if (percentEl) percentEl.textContent = percentage + '%';
            if (circleEl) circleEl.style.strokeDashoffset = 283 - (283 * percentage / 100);
        }
        
        // 搜索功能
        document.addEventListener('DOMContentLoaded', function() {
            const searchInput = document.getElementById('search-input');
            const searchResults = document.getElementById('search-results');
            
            // 键盘快捷键
            document.addEventListener('keydown', function(e) {
                if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
                    e.preventDefault();
                    if (searchInput) searchInput.focus();
                }
            });
            
            // 搜索
            if (searchInput) {
                searchInput.addEventListener('input', function() {
                    const query = this.value.toLowerCase().trim();
                    if (query.length < 2) {
                        if (searchResults) searchResults.innerHTML = '';
                        return;
                    }
                    
                    const projectId = 'project' + window.location.pathname.match(/project(\d+)/)?.[1] || '1';
                    const searchData = getSearchData(projectId);
                    const results = searchData.filter(item => 
                        item.title.toLowerCase().includes(query) ||
                        item.content.toLowerCase().includes(query)
                    );
                    
                    if (results.length === 0) {
                        if (searchResults) searchResults.innerHTML = '<p style="color: #a0a0b8;">未找到相关结果</p>';
                    } else {
                        if (searchResults) {
                            searchResults.innerHTML = results.map(r => 
                                `<div class="search-result-item" tabindex="0">
                                    <strong>${r.title}</strong><br>
                                    <small style="color: #8080a0;">${r.section}</small>
                                </div>`
                            ).join('');
                        }
                    }
                });
            }
            
            // 加载保存的进度
            updateProgressDisplay();
            
            // 预加载 Pyodide
            initPyodide();
        });
        
        function getSearchData(projectId) {
            const dataMap = DATA_PLACEHOLDER;
            return dataMap;
        }
        
        // Service Worker 注册
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                console.log('Service Worker 支持可用');
            });
        }
    </script>
'''

def add_enhancements_to_project(proj_num, config):
    file_path = f'/workspace/projects/project{proj_num}/index.html'
    if not os.path.exists(file_path):
        print(f'跳过: {file_path} 不存在')
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加搜索功能到 tabs 前面
    if '<!-- 搜索功能 -->' not in content:
        # 找到 tabs-wrapper 的位置
        tabs_pattern = r'<div class="tabs-wrapper"'
        if re.search(tabs_pattern, content):
            content = re.sub(tabs_pattern, SEARCH_HTML + '\n        <div class="tabs-wrapper"', content)
    
    # 添加 Pyodide 和增强功能
    if 'pyodide.js' not in content:
        # 在 </body> 前添加
        content = content.replace('</body>', ENHANCED_JS + '\n</body>')
    
    # 添加搜索数据
    search_data = f'const DATA_PLACEHOLDER = [{config["search_content"]}];'
    if 'const DATA_PLACEHOLDER' not in content:
        content = content.replace('<script src="https://cdn.jsdelivr.net/pyodide', search_data + '\n    <script src="https://cdn.jsdelivr.net/pyodide')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'已增强: project{proj_num}')
    return True

def main():
    print('开始为所有项目添加增强功能...')
    updated_count = 0
    
    for proj_num, config in PROJECTS.items():
        if add_enhancements_to_project(proj_num, config):
            updated_count += 1
    
    print(f'\n完成! 共更新 {updated_count} 个项目。')

if __name__ == '__main__':
    main()
