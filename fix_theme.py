import os

# 定义浅色主题的CSS变量替换
old_theme = """        :root {
            --primary: #00f5ff;
            --primary-rgb: 0, 245, 255;
            --secondary: #8b5cf6;
            --accent: #00ff88;
            --bg-dark: #0a0a1a;
            --bg-panel: rgba(20, 20, 40, 0.8);
            --text: #e0e0e0;
            --text-muted: #9ca3af;
            --border: rgba(0, 245, 255, 0.2);
            --success: #22c55e;
            --warning: #f59e0b;
            --error: #ef4444;
        }
        .light-theme {
            --bg-dark: #f3f4f6;
            --bg-panel: rgba(255, 255, 255, 0.95);
            --text: #1f2937;
            --text-muted: #6b7280;
            --border: rgba(0, 0, 0, 0.1);
        }"""

new_theme = """        :root {
            --primary: #3b82f6;
            --primary-rgb: 59, 130, 246;
            --secondary: #8b5cf6;
            --accent: #22c55e;
            --bg-dark: #f8fafc;
            --bg-panel: rgba(255, 255, 255, 0.95);
            --text: #1e293b;
            --text-muted: #64748b;
            --border: rgba(0, 0, 0, 0.1);
            --success: #22c55e;
            --warning: #f59e0b;
            --error: #ef4444;
        }"""

# 需要修改的body背景样式
old_body_before = """        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: 
                radial-gradient(circle at 20% 20%, rgba(var(--primary-rgb), 0.05) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.05) 0%, transparent 50%),
                linear-gradient(rgba(10, 10, 26, 0.95), rgba(10, 10, 26, 0.95)),
                repeating-linear-gradient(0deg, transparent, transparent 50px, rgba(var(--primary-rgb), 0.03) 50px, rgba(var(--primary-rgb), 0.03) 51px),
                repeating-linear-gradient(90deg, transparent, transparent 50px, rgba(var(--primary-rgb), 0.03) 50px, rgba(var(--primary-rgb), 0.03) 51px);
            pointer-events: none;
            z-index: -1;
        }"""

new_body_before = """        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: 
                radial-gradient(circle at 20% 20%, rgba(var(--primary-rgb), 0.05) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(139, 92, 246, 0.05) 0%, transparent 50%);
            pointer-events: none;
            z-index: -1;
        }"""

# 需要修改的导航栏样式
old_nav = '    <nav class="glass-panel fixed w-full top-0 z-50">'
new_nav = '    <nav class="fixed w-full top-0 z-50 bg-white/95 backdrop-blur-lg shadow-sm border-b border-gray-200">'

# 需要修改的扫描线样式 - 删除扫描线
old_scanline = '    <div class="scanline"></div>'
new_scanline = ''

# 需要修改的section背景样式
old_section_bg = '        <div class="absolute inset-0 bg-gradient-to-r from-blue-900/30 to-purple-900/30"></div>'
new_section_bg = '        <div class="absolute inset-0 bg-gradient-to-r from-blue-50/50 to-purple-50/50"></div>'

# 需要修改的链接颜色
old_link_color = 'text-gray-300 hover:text-cyan-400'
new_link_color = 'text-gray-600 hover:text-blue-500'

# 需要修改的文字颜色
old_text_gray_400 = 'text-gray-400'
new_text_gray_400 = 'text-gray-500'

old_text_gray_500 = 'text-gray-500'
new_text_gray_500 = 'text-gray-400'

old_text_gray_300 = 'text-gray-300'
new_text_gray_300 = 'text-gray-700'

old_text_gray_200 = 'text-gray-200'
new_text_gray_200 = 'text-gray-800'

old_text_cyan_400 = 'text-cyan-400'
new_text_cyan_400 = 'text-blue-500'

old_text_yellow_400 = 'text-yellow-400'
new_text_yellow_400 = 'text-yellow-500'

old_text_purple_400 = 'text-purple-400'
new_text_purple_400 = 'text-purple-600'

old_text_green_400 = 'text-green-400'
new_text_green_400 = 'text-green-500'

# 需要修改的代码编辑器背景
old_code_editor_bg = '            background: rgba(5, 5, 15, 0.95);'
new_code_editor_bg = '            background: #1e293b;'

old_terminal_bg = '            background: rgba(5, 5, 15, 0.95);'
new_terminal_bg = '            background: #1e293b;'

old_code_block_bg = '            background: rgba(10, 10, 26, 0.9);'
new_code_block_bg = '            background: #1e293b;'

old_code_card_bg = '            background: rgba(10, 10, 26, 0.95);'
new_code_card_bg = '            background: #1e293b;'

old_practice_nav_bg = '            background: rgba(20, 20, 40, 0.6);'
new_practice_nav_bg = '            background: #f1f5f9;'

old_detail_card_bg = '            background: rgba(20, 20, 40, 0.8);'
new_detail_card_bg = '            background: #fef3c7;'

old_tip_card_bg = '            background: rgba(20, 20, 40, 0.8);'
new_tip_card_bg = '            background: #fefce8;'

old_file_tab_bg = '            background: rgba(30, 30, 50, 0.8);'
new_file_tab_bg = '            background: #e2e8f0;'

old_toolbar_bg = '            background: rgba(20, 20, 40, 0.9);'
new_toolbar_bg = '            background: #e2e8f0;'

old_autocomplete_bg = '            background: rgba(20, 20, 40, 0.98);'
new_autocomplete_bg = '            background: #ffffff;'

old_modal_bg = '            background: rgba(0, 0, 0, 0.8);'
new_modal_bg = '            background: rgba(0, 0, 0, 0.5);'

old_history_item_bg = '            background: rgba(var(--primary-rgb), 0.1);'
new_history_item_bg = '            background: rgba(var(--primary-rgb), 0.15);'

old_file_tree_item_bg = '            background: rgba(var(--primary-rgb), 0.1);'
new_file_tree_item_bg = '            background: rgba(var(--primary-rgb), 0.15);'

old_file_tree_item_active_bg = '            background: rgba(var(--primary-rgb), 0.2);'
new_file_tree_item_active_bg = '            background: rgba(var(--primary-rgb), 0.25);'

def modify_project_files():
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
        
        # 替换主题变量
        content = content.replace(old_theme, new_theme)
        
        # 替换body背景
        content = content.replace(old_body_before, new_body_before)
        
        # 替换导航栏
        content = content.replace(old_nav, new_nav)
        
        # 移除扫描线
        content = content.replace(old_scanline, new_scanline)
        
        # 替换section背景
        content = content.replace(old_section_bg, new_section_bg)
        
        # 替换链接颜色
        content = content.replace(old_link_color, new_link_color)
        
        # 替换文字颜色
        content = content.replace(old_text_gray_400, new_text_gray_400)
        content = content.replace(old_text_gray_500, new_text_gray_500)
        content = content.replace(old_text_gray_300, new_text_gray_300)
        content = content.replace(old_text_gray_200, new_text_gray_200)
        content = content.replace(old_text_cyan_400, new_text_cyan_400)
        content = content.replace(old_text_yellow_400, new_text_yellow_400)
        content = content.replace(old_text_purple_400, new_text_purple_400)
        content = content.replace(old_text_green_400, new_text_green_400)
        
        # 替换代码编辑器背景
        content = content.replace(old_code_editor_bg, new_code_editor_bg)
        content = content.replace(old_terminal_bg, new_terminal_bg)
        content = content.replace(old_code_block_bg, new_code_block_bg)
        content = content.replace(old_code_card_bg, new_code_card_bg)
        
        # 替换面板背景
        content = content.replace(old_practice_nav_bg, new_practice_nav_bg)
        content = content.replace(old_detail_card_bg, new_detail_card_bg)
        content = content.replace(old_tip_card_bg, new_tip_card_bg)
        content = content.replace(old_file_tab_bg, new_file_tab_bg)
        content = content.replace(old_toolbar_bg, new_toolbar_bg)
        content = content.replace(old_autocomplete_bg, new_autocomplete_bg)
        content = content.replace(old_modal_bg, new_modal_bg)
        
        # 替换hover背景
        content = content.replace(old_history_item_bg, new_history_item_bg)
        content = content.replace(old_file_tree_item_bg, new_file_tree_item_bg)
        content = content.replace(old_file_tree_item_active_bg, new_file_tree_item_active_bg)
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Modified: {index_file}")

if __name__ == '__main__':
    modify_project_files()
    print("All project files have been updated to light theme.")