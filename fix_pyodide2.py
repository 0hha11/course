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
        
        # 修复语法错误 - 缺少闭合大括号
        old_catch = '''                } else {
                        console.error('Pyodide加载最终失败:', error);
                document.getElementById('pyodide-loading').innerHTML = `
                    <div class="text-center bg-white p-8 rounded-xl shadow-lg">
                        <p class="text-red-500 mb-4 text-lg font-medium">Python环境加载失败</p>
                        <p class="text-gray-500 mb-4 text-sm">请检查网络连接后重试</p>
                        <button onclick="location.reload()" class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors">重试</button>
                    </div>
                `;
            }
        }'''
        
        new_catch = '''                } else {
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
        
        if old_catch in content:
            content = content.replace(old_catch, new_catch)
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {index_file}")
        else:
            print(f"Already fixed or different format: {index_file}")

if __name__ == '__main__':
    fix_project_files()
    print("Done!")
