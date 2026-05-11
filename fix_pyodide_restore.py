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
        
        # 恢复到最初的Pyodide版本 0.24.1
        content = content.replace(
            'https://unpkg.com/pyodide@0.25.0/dist/pyodide.js',
            'https://cdn.jsdelivr.net/npm/pyodide@0.24.1/dist/pyodide.js'
        )
        
        # 恢复原始的initPyodide函数（简化版，去掉复杂的重试逻辑）
        old_init = '''        async function initPyodide() {
            const maxRetries = 3;
            let retryCount = 0;
            
            // 检查网络连接
            if (!navigator.onLine) {
                document.getElementById('pyodide-loading').innerHTML = `
                    <div class="text-center bg-white p-8 rounded-xl shadow-lg">
                        <p class="text-red-500 mb-4 text-lg font-medium">网络未连接</p>
                        <p class="text-gray-500 mb-4 text-sm">请检查您的网络连接后重试</p>
                        <button onclick="location.reload()" class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">重试</button>
                    </div>
                `;
                return;
            }
            
            while (retryCount < maxRetries) {
                try {
                    console.log(`Pyodide加载尝试 ${retryCount + 1}/${maxRetries}...`);
                    document.getElementById('pyodide-loading').querySelector('p').textContent = 
                        `正在加载Python环境... (尝试 ${retryCount + 1}/${maxRetries})`;
                    
                    pyodide = await loadPyodide({
                        indexURL: "https://unpkg.com/pyodide@0.25.0/",
                        stdout: (text) => console.log(text),
                        stderr: (text) => console.error(text),
                        fullStdLib: false
                    });
                    
                    console.log('Pyodide核心加载完成，正在加载pandas...');
                    await pyodide.loadPackage(['pandas', 'numpy', 'pytz']);
                    
                    document.getElementById('pyodide-loading').style.display = 'none';
                    isLoading = false;
                    log('Python环境加载完成', 'success');
                    showToast('Python环境就绪', 'success');
                    return;
                } catch (error) {
                    retryCount++;
                    console.error(`Pyodide加载失败 (尝试 ${retryCount}/${maxRetries}):`, error);
                    
                    if (retryCount < maxRetries) {
                        console.log(`5秒后重试...`);
                        await new Promise(resolve => setTimeout(resolve, 5000));
                    } else {
                        console.error('Pyodide加载最终失败:', error);
                        document.getElementById('pyodide-loading').innerHTML = `
                            <div class="text-center bg-white p-8 rounded-xl shadow-lg">
                                <p class="text-red-500 mb-4 text-lg font-medium">Python环境加载失败</p>
                                <p class="text-gray-500 mb-4 text-sm">请检查网络连接后重试</p>
                                <p class="text-gray-400 text-xs mb-4">错误: ${error.message || '未知错误'}</p>
                                <button onclick="location.reload()" class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">重试</button>
                            </div>
                        `;
                    }
                }
            }
        }'''
        
        new_init = '''        async function initPyodide() {
            try {
                pyodide = await loadPyodide({
                    indexURL: "https://cdn.jsdelivr.net/npm/pyodide@0.24.1/"
                });
                await pyodide.loadPackage(['pandas', 'numpy', 'pytz']);
                document.getElementById('pyodide-loading').style.display = 'none';
                isLoading = false;
                log('Python环境加载完成', 'success');
                showToast('Python环境就绪', 'success');
            } catch (error) {
                console.error('Pyodide加载失败:', error);
                document.getElementById('pyodide-loading').innerHTML = `
                    <div class="text-center bg-white p-8 rounded-xl shadow-lg">
                        <p class="text-red-500 mb-4 text-lg font-medium">Python环境加载失败</p>
                        <p class="text-gray-500 mb-4 text-sm">请检查网络连接后重试</p>
                        <button onclick="location.reload()" class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">重试</button>
                    </div>
                `;
            }
        }'''
        
        content = content.replace(old_init, new_init)
        
        # 恢复原始的脚本调用方式
        old_script_end = '''        // 等待Pyodide加载完成后再初始化
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
            });'''
        
        new_script_end = '''        initPyodide();'''
        
        content = content.replace(old_script_end, new_script_end)
        
        # 恢复加载提示样式
        old_loading = '''<div id="pyodide-loading" class="fixed inset-0 bg-black/30 flex items-center justify-center z-[1001]">
        <div class="text-center bg-white p-8 rounded-xl shadow-lg">
            <div class="loading-spinner mx-auto mb-4"></div>
            <p class="text-gray-700 font-medium">正在加载Python环境...</p>
            <p class="text-gray-400 text-sm mt-2">首次加载可能需要30-60秒</p>
        </div>
    </div>'''
        
        new_loading = '''<div id="pyodide-loading" class="fixed inset-0 bg-black/50 flex items-center justify-center z-[1001]">
        <div class="text-center">
            <div class="loading-spinner mx-auto mb-4"></div>
            <p class="text-white">正在加载Python环境...</p>
        </div>
    </div>'''
        
        content = content.replace(old_loading, new_loading)
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Restored: {index_file}")

if __name__ == '__main__':
    fix_project_files()
    print("All project files have been restored to original working version.")
