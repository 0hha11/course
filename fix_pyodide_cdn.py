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
        
        # 使用 jsDelivr 的中国CDN (fastly.jsdelivr.net 在国内更快)
        content = content.replace(
            'https://cdn.jsdelivr.net/npm/pyodide@0.25.0/dist/pyodide.js',
            'https://fastly.jsdelivr.net/npm/pyodide@0.25.0/dist/pyodide.js'
        )
        content = content.replace(
            'indexURL: "https://cdn.jsdelivr.net/npm/pyodide@0.25.0/"',
            'indexURL: "https://fastly.jsdelivr.net/npm/pyodide@0.25.0/"'
        )
        
        # 添加更长的超时时间
        old_init = '''async function initPyodide() {
            const maxRetries = 3;
            let retryCount = 0;
            
            while (retryCount < maxRetries) {
                try {
                    console.log(`Pyodide加载尝试 ${retryCount + 1}/${maxRetries}...`);
                    
                    pyodide = await loadPyodide({
                        indexURL: "https://fastly.jsdelivr.net/npm/pyodide@0.25.0/",
                        stdout: (text) => console.log(text),
                        stderr: (text) => console.error(text)
                    });'''
        
        new_init = '''async function initPyodide() {
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
                        indexURL: "https://fastly.jsdelivr.net/npm/pyodide@0.25.0/",
                        stdout: (text) => console.log(text),
                        stderr: (text) => console.error(text),
                        fullStdLib: false
                    });'''
        
        content = content.replace(old_init, new_init)
        
        # 更新加载提示文字
        old_loading_text = '<p class="text-gray-700 font-medium">正在加载Python环境...</p>'
        new_loading_text = '<p class="text-gray-700 font-medium">正在加载Python环境...</p>'
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated CDN: {index_file}")

if __name__ == '__main__':
    fix_project_files()
    print("All project files have been updated to use fastly CDN.")
