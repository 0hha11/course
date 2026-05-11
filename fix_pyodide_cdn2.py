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
        
        # 使用 unpkg 作为备选CDN (在国内有时更稳定)
        content = content.replace(
            'https://fastly.jsdelivr.net/npm/pyodide@0.25.0/dist/pyodide.js',
            'https://unpkg.com/pyodide@0.25.0/dist/pyodide.js'
        )
        content = content.replace(
            'indexURL: "https://fastly.jsdelivr.net/npm/pyodide@0.25.0/"',
            'indexURL: "https://unpkg.com/pyodide@0.25.0/"'
        )
        
        # 更新错误提示中的CDN地址
        content = content.replace(
            '请检查网络连接，确保可以访问 fastly.jsdelivr.net',
            '请检查网络连接，确保可以访问 unpkg.com'
        )
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated CDN: {index_file}")

if __name__ == '__main__':
    fix_project_files()
    print("All project files have been updated to use unpkg CDN.")
