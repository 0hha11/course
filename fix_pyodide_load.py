import os

def fix_project_files():
    projects_dir = '/workspace/projects'
    
    for project_dir in os.listdir(projects_dir):
        project_path = os.path.join(projects_dir, project_dir)
        if not os.path.isdir(project_path):
            continue
            
        index_file = os.path.join(project_path, 'index.html')
        if not os.path.exists(index_file):
            continue
            
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复：添加等待Pyodide加载完成的逻辑
        old_script_end = '''        initPyodide();
        updateDailyChallenge();
        updateLineNumbers();
        updateCodeEditor(1);
        Prism.highlightAll();
        log('项目1加载完成');
    </script>'''
        
        new_script_end = '''        // 等待Pyodide加载完成后再初始化
        function waitForPyodide() {
            return new Promise((resolve, reject) => {
                let attempts = 0;
                const maxAttempts = 100; // 最多等待10秒
                
                const checkInterval = setInterval(() => {
                    attempts++;
                    if (typeof loadPyodide !== 'undefined') {
                        clearInterval(checkInterval);
                        resolve();
                    } else if (attempts >= maxAttempts) {
                        clearInterval(checkInterval);
                        reject(new Error('Pyodide加载超时，请检查网络连接'));
                    }
                }, 100);
            });
        }
        
        // 先检查Pyodide是否已加载
        waitForPyodide()
            .then(() => {
                console.log('Pyodide脚本已加载，开始初始化...');
                initPyodide();
            })
            .catch(error => {
                console.error('Pyodide加载失败:', error);
                document.getElementById('pyodide-loading').innerHTML = `
                    <div class="text-center bg-white p-8 rounded-xl shadow-lg">
                        <p class="text-red-500 mb-4 text-lg font-medium">Python环境加载失败</p>
                        <p class="text-gray-500 mb-4 text-sm">${error.message}</p>
                        <p class="text-gray-400 text-xs mb-4">请检查网络连接，确保可以访问 fastly.jsdelivr.net</p>
                        <button onclick="location.reload()" class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">重试</button>
                    </div>
                `;
            });
        
        updateDailyChallenge();
        updateLineNumbers();
        updateCodeEditor(1);
        Prism.highlightAll();
        log('项目1加载完成');
    </script>'''
        
        # 根据项目号调整日志信息
        project_num = project_dir.replace('project', '')
        new_script_end = new_script_end.replace("项目1加载完成", f"项目{project_num}加载完成")
        
        if old_script_end in content:
            content = content.replace(old_script_end, new_script_end)
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {index_file}")
        else:
            print(f"Pattern not found: {index_file}")

if __name__ == '__main__':
    fix_project_files()
    print("Done!")
