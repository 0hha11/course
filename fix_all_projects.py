#!/usr/bin/env python3
import os

def fix_project_html(file_path, project_num, project_title):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 更新Pyodide版本
    old_pyodide_script = '<script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>'
    new_pyodide_script = '<script src="https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js"></script>'
    content = content.replace(old_pyodide_script, new_pyodide_script)
    
    # 2. 更新indexURL
    old_index_url = 'indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"'
    new_index_url = 'indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/"'
    content = content.replace(old_index_url, new_index_url)
    
    # 3. 改进initPyodide函数
    old_init = '''        async function initPyodide() {
            if (pyodide || isLoading) return;
            isLoading = true;
            
            const btn = document.getElementById('run-btn');
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = '<span class="loading-spinner"></span> 加载中...';
            }
            
            try {
                pyodide = await loadPyodide({
                    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/"
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
        }'''
    
    new_init = '''        async function initPyodide() {
            if (pyodide) return pyodide;
            if (isLoading) return new Promise(resolve => {
                const check = setInterval(() => {
                    if (pyodide) {
                        clearInterval(check);
                        resolve(pyodide);
                    }
                }, 100);
            });
            
            isLoading = true;
            
            // 更新所有运行按钮状态
            document.querySelectorAll('[onclick*="runCode"], [onclick*="runPracticeCode"], [onclick*="runHomeworkCode"]').forEach(btn => {
                btn.disabled = true;
                const originalText = btn.innerHTML;
                btn.dataset.originalText = originalText;
                btn.innerHTML = '<span class="loading-spinner"></span> 加载中...';
            });
            
            try {
                console.log('正在加载 Pyodide...');
                pyodide = await loadPyodide({
                    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/"
                });
                
                // 预加载常用包
                await pyodide.loadPackage(['micropip']);
                console.log('Pyodide 加载成功！');
                
                // 恢复所有按钮状态
                document.querySelectorAll('[onclick*="runCode"], [onclick*="runPracticeCode"], [onclick*="runHomeworkCode"]').forEach(btn => {
                    btn.disabled = false;
                    if (btn.dataset.originalText) {
                        btn.innerHTML = btn.dataset.originalText;
                    }
                });
                
                return pyodide;
            } catch (error) {
                console.error('Pyodide 加载失败:', error);
                alert('Pyodide 加载失败，请刷新页面重试！');
                
                // 恢复所有按钮状态
                document.querySelectorAll('[onclick*="runCode"], [onclick*="runPracticeCode"], [onclick*="runHomeworkCode"]').forEach(btn => {
                    btn.disabled = false;
                    if (btn.dataset.originalText) {
                        btn.innerHTML = btn.dataset.originalText;
                    }
                });
                
                isLoading = false;
                return null;
            }
        }'''
    content = content.replace(old_init, new_init)
    
    # 4. 改进runCode函数
    old_runcode = '''        async function runCode() {
            const code = document.getElementById('code-input').value;
            const outputBox = document.getElementById('output-box');
            const outputContent = document.getElementById('output-content');
            const btn = document.getElementById('run-btn');
            
            if (!code.trim()) {
                alert('请先输入代码！');
                return;
            }
            
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
            } finally {
                btn.disabled = false;
                btn.innerHTML = '▶️ 运行代码';
            }
        }'''
    
    new_runcode = '''        async function runCode() {
            const code = document.getElementById('code-input').value;
            const outputBox = document.getElementById('output-box');
            const outputContent = document.getElementById('output-content');
            const btn = document.getElementById('run-btn');
            
            if (!code.trim()) {
                alert('请先输入代码！');
                return;
            }
            
            outputBox.style.display = 'block';
            outputContent.textContent = '正在执行...';
            outputContent.className = 'output-content';
            btn.disabled = true;
            btn.innerHTML = '<span class="loading-spinner"></span> 运行中...';
            
            try {
                const p = await initPyodide();
                if (!p) throw new Error('Pyodide 未初始化');
                
                // 重置输出流
                p.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
                `);
                
                // 执行代码
                await p.runPythonAsync(code);
                
                const stdout = p.runPython('sys.stdout.getvalue()');
                const stderr = p.runPython('sys.stderr.getvalue()');
                
                if (stderr?.trim()) {
                    outputContent.textContent = stderr;
                    outputContent.className = 'output-content error';
                } else {
                    outputContent.textContent = stdout || '(代码执行完成，无输出)';
                    outputContent.className = 'output-content success';
                }
            } catch (error) {
                console.error('代码执行错误:', error);
                outputContent.textContent = '错误: ' + error.message;
                outputContent.className = 'output-content error';
            } finally {
                btn.disabled = false;
                btn.innerHTML = '▶️ 运行代码';
            }
        }'''
    content = content.replace(old_runcode, new_runcode)
    
    # 5. 改进runPracticeCode函数
    old_practice = '''        async function runPracticeCode(num) {
            const code = document.getElementById('practice-code-' + num).value;
            const outputBox = document.getElementById('practice-output-' + num);
            const outputContent = document.getElementById('practice-output-content-' + num);
            if (!code.trim()) { alert('请先输入代码！'); return; }
            outputBox.style.display = 'block';
            outputContent.textContent = '正在执行...';
            try {
                await initPyodide();
                pyodide.runPython(`import sys; from io import StringIO; sys.stdout = StringIO(); sys.stderr = StringIO()`);
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
        }'''
    
    new_practice = '''        async function runPracticeCode(num) {
            const code = document.getElementById('practice-code-' + num).value;
            const outputBox = document.getElementById('practice-output-' + num);
            const outputContent = document.getElementById('practice-output-content-' + num);
            const btn = event.target;
            
            if (!code.trim()) {
                alert('请先输入代码！');
                return;
            }
            
            outputBox.style.display = 'block';
            outputContent.textContent = '正在执行...';
            outputContent.className = 'output-content';
            btn.disabled = true;
            const originalText = btn.innerHTML;
            btn.innerHTML = '<span class="loading-spinner"></span> 运行中...';
            
            try {
                const p = await initPyodide();
                if (!p) throw new Error('Pyodide 未初始化');
                
                // 重置输出流
                p.runPython(`import sys; from io import StringIO; sys.stdout = StringIO(); sys.stderr = StringIO()`);
                
                // 执行代码
                await p.runPythonAsync(code);
                
                const stdout = p.runPython('sys.stdout.getvalue()');
                const stderr = p.runPython('sys.stderr.getvalue()');
                
                if (stderr?.trim()) {
                    outputContent.textContent = stderr;
                    outputContent.className = 'output-content error';
                } else {
                    outputContent.textContent = stdout || '(代码执行完成，无输出)';
                    outputContent.className = 'output-content success';
                }
            } catch (error) {
                console.error('代码执行错误:', error);
                outputContent.textContent = '错误: ' + error.message;
                outputContent.className = 'output-content error';
            } finally {
                btn.disabled = false;
                btn.innerHTML = originalText;
            }
        }'''
    content = content.replace(old_practice, new_practice)
    
    # 6. 改进runHomeworkCode函数
    old_homework = '''        async function runHomeworkCode() {
            const code = document.getElementById('homework-code').value;
            const outputBox = document.getElementById('homework-output');
            const outputContent = document.getElementById('homework-output-content');
            
            if (!code.trim()) {
                alert('请先输入代码！');
                return;
            }
            
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
        }'''
    
    new_homework = '''        async function runHomeworkCode() {
            const code = document.getElementById('homework-code').value;
            const outputBox = document.getElementById('homework-output');
            const outputContent = document.getElementById('homework-output-content');
            const btn = event.target;
            
            if (!code.trim()) {
                alert('请先输入代码！');
                return;
            }
            
            outputBox.style.display = 'block';
            outputContent.textContent = '正在执行...';
            outputContent.className = 'output-content';
            btn.disabled = true;
            const originalText = btn.innerHTML;
            btn.innerHTML = '<span class="loading-spinner"></span> 运行中...';
            
            try {
                const p = await initPyodide();
                if (!p) throw new Error('Pyodide 未初始化');
                
                // 重置输出流
                p.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
                `);
                
                // 执行代码
                await p.runPythonAsync(code);
                
                const stdout = p.runPython('sys.stdout.getvalue()');
                const stderr = p.runPython('sys.stderr.getvalue()');
                
                if (stderr?.trim()) {
                    outputContent.textContent = stderr;
                    outputContent.className = 'output-content error';
                } else {
                    outputContent.textContent = stdout || '(代码执行完成，无输出)';
                    outputContent.className = 'output-content success';
                }
            } catch (error) {
                console.error('代码执行错误:', error);
                outputContent.textContent = '错误: ' + error.message;
                outputContent.className = 'output-content error';
            } finally {
                btn.disabled = false;
                btn.innerHTML = originalText;
            }
        }'''
    content = content.replace(old_homework, new_homework)
    
    # 7. 添加页面加载时的预加载提示
    footer_end = '''    </script>
</body>
</html>'''
    
    new_footer = '''        // 页面加载完成后显示提示
        document.addEventListener('DOMContentLoaded', function() {
            const originalInit = initPyodide;
            let hasLoaded = false;
            
            // 在第一次点击运行时预加载
            document.addEventListener('click', function(e) {
                if (!hasLoaded && e.target.textContent && (e.target.textContent.includes('运行') || e.target.textContent.includes('▶️'))) {
                    hasLoaded = true;
                }
            }, { once: true });
            
            updateProgressDisplay();
        });
    </script>
</body>
</html>'''
    content = content.replace(footer_end, new_footer)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ 已更新 {file_path}')

def main():
    projects = [
        (1, '数据清洗'),
        (2, '分组聚合分析'),
        (3, '购物篮分析'),
        (4, '客户聚类分析'),
        (5, '数据可视化'),
        (6, 'A/B测试分析'),
        (7, '时间序列分析'),
        (8, '特征工程'),
        (9, '异常值检测'),
        (10, '多数据集合并')
    ]
    
    print('开始修复所有项目...\n')
    
    for num, title in projects:
        file_path = f'/workspace/projects/project{num}/index.html'
        if os.path.exists(file_path):
            fix_project_html(file_path, num, title)
        else:
            print(f'✗ 文件不存在: {file_path}')
    
    print('\n所有项目修复完成！')

if __name__ == '__main__':
    main()
