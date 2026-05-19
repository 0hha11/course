#!/usr/bin/env python3
import os

def improve_project_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 更新Pyodide版本（如果还没更新）
    content = content.replace(
        'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/',
        'https://cdn.jsdelivr.net/pyodide/v0.26.2/full/'
    )
    
    # 2. 添加skip link和focus样式
    if '.skip-link' not in content:
        skip_link_css = '''
        /* Skip to main content link */
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: #00d4ff;
            color: #0f172a;
            padding: 8px 16px;
            z-index: 1000;
            transition: top 0.3s;
            text-decoration: none;
            font-weight: 600;
        }
        .skip-link:focus {
            top: 0;
            outline: 2px solid #ffffff;
        }

        /* Focus styles for accessibility */
        *:focus-visible {
            outline: 3px solid #00d4ff;
            outline-offset: 3px;
        }

        a:focus-visible,
        button:focus-visible {
            outline: 3px solid #00d4ff;
            outline-offset: 3px;
        }
'''
        content = content.replace(
            '        body {',
            skip_link_css + '\n        body {'
        )
    
    # 3. 改进对比度
    content = content.replace(
        'background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);',
        'background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);'
    )
    content = content.replace(
        'color: #e6e6e6;',
        'color: #f1f5f9;'
    )
    content = content.replace(
        'color: #a0a0b8;',
        'color: #cbd5e1;'
    )
    content = content.replace(
        'color: #8080a0;',
        'color: #94a3b8;'
    )
    content = content.replace(
        'color: #d4d4e8;',
        'color: #e2e8f0;'
    )
    content = content.replace(
        'color: #c8c8d8;',
        'color: #cbd5e1;'
    )
    
    # 4. 添加skip link到HTML
    if '<a href="#main-content" class="skip-link"' not in content:
        content = content.replace(
            '<body>',
            '<body>\n    <a href="#main-content" class="skip-link">跳转到主要内容</a>'
        )
    
    # 5. 添加main-content ID到主要内容区域
    if 'id="main-content"' not in content:
        content = content.replace(
            '    <main>',
            '    <main id="main-content">'
        )
    
    # 6. 确保Pyodide的改进是完整的
    # 更新initPyodide函数
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
    
    # 更新runCode函数
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
    
    # 更新runPracticeCode函数
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
    
    # 更新runHomeworkCode函数
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
    
    # 保存修改
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✓ 已改进: {file_path}')

def main():
    print('开始改进所有项目页面...\n')
    
    for i in range(1, 11):
        file_path = f'/workspace/projects/project{i}/index.html'
        if os.path.exists(file_path):
            improve_project_file(file_path)
        else:
            print(f'✗ 文件不存在: {file_path}')
    
    print('\n所有项目页面改进完成！')

if __name__ == '__main__':
    main()
