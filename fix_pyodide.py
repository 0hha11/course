import os
import re

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
        
        # 1. 更新Pyodide版本到0.25.0（更稳定）
        content = content.replace(
            'https://cdn.jsdelivr.net/npm/pyodide@0.24.1/dist/pyodide.js',
            'https://cdn.jsdelivr.net/npm/pyodide@0.25.0/dist/pyodide.js'
        )
        content = content.replace(
            'indexURL: "https://cdn.jsdelivr.net/npm/pyodide@0.24.1/"',
            'indexURL: "https://cdn.jsdelivr.net/npm/pyodide@0.25.0/"'
        )
        
        # 2. 修复加载失败的提示样式 - 改为浅色主题
        old_error_msg = '''document.getElementById('pyodide-loading').innerHTML = `
                    <div class="text-center">
                        <p class="text-red-400 mb-4">Python环境加载失败</p>
                        <button onclick="location.reload()" class="neon-button px-4 py-2 rounded">重试</button>
                    </div>
                `;'''
        
        new_error_msg = '''document.getElementById('pyodide-loading').innerHTML = `
                    <div class="text-center bg-white p-8 rounded-xl shadow-lg">
                        <p class="text-red-500 mb-4 text-lg font-medium">Python环境加载失败</p>
                        <p class="text-gray-500 mb-4 text-sm">请检查网络连接后重试</p>
                        <button onclick="location.reload()" class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">重试</button>
                    </div>
                `;'''
        
        content = content.replace(old_error_msg, new_error_msg)
        
        # 3. 修复加载中的提示样式
        old_loading = '''<div id="pyodide-loading" class="fixed inset-0 bg-black/50 flex items-center justify-center z-[1001]">
        <div class="text-center">
            <div class="loading-spinner mx-auto mb-4"></div>
            <p class="text-white">正在加载Python环境...</p>
        </div>
    </div>'''
        
        new_loading = '''<div id="pyodide-loading" class="fixed inset-0 bg-black/30 flex items-center justify-center z-[1001]">
        <div class="text-center bg-white p-8 rounded-xl shadow-lg">
            <div class="loading-spinner mx-auto mb-4"></div>
            <p class="text-gray-700 font-medium">正在加载Python环境...</p>
            <p class="text-gray-400 text-sm mt-2">首次加载可能需要30-60秒</p>
        </div>
    </div>'''
        
        content = content.replace(old_loading, new_loading)
        
        # 4. 添加更健壮的加载逻辑 - 添加超时和重试机制
        old_init = '''async function initPyodide() {
            try {
                pyodide = await loadPyodide({
                    indexURL: "https://cdn.jsdelivr.net/npm/pyodide@0.25.0/"
                });
                await pyodide.loadPackage(['pandas', 'numpy', 'pytz']);
                document.getElementById('pyodide-loading').style.display = 'none';
                isLoading = false;
                log('Python环境加载完成', 'success');
                showToast('Python环境就绪', 'success');
            } catch (error) {
                console.error('Pyodide加载失败:', error);'''
        
        new_init = '''async function initPyodide() {
            const maxRetries = 3;
            let retryCount = 0;
            
            while (retryCount < maxRetries) {
                try {
                    console.log(`Pyodide加载尝试 ${retryCount + 1}/${maxRetries}...`);
                    
                    pyodide = await loadPyodide({
                        indexURL: "https://cdn.jsdelivr.net/npm/pyodide@0.25.0/",
                        stdout: (text) => console.log(text),
                        stderr: (text) => console.error(text)
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
                        console.error('Pyodide加载最终失败:', error);'''
        
        content = content.replace(old_init, new_init)
        
        # 5. 修复catch块中的错误处理
        old_catch = '''} catch (error) {
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
        
        new_catch = '''} else {
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
        
        content = content.replace(old_catch, new_catch)
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed Pyodide: {index_file}")

if __name__ == '__main__':
    fix_project_files()
    print("All project files have been fixed for Pyodide loading.")