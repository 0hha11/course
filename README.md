# TT的个人学习页面

这是一个纯静态的个人学习页面，展示了广东科学技术职业学院商学院商务数据分析与应用专业学生TT的课程信息。

## 项目结构

```
├── index.html          # 首页
├── about.html          # 关于我页面
├── courses/            # 课程目录
│   ├── python-basic/   # Python基础课程
│   ├── data-analysis/  # 数据分析技术课程
│   ├── data-collection/ # 数据采集与处理课程
│   ├── supply-chain/   # 供应链数据分析课程
│   └── database/       # 数据库原理与应用课程
├── .trae/              # 文档目录
│   └── documents/      # 产品需求和技术架构文档
└── README.md           # 项目说明文件
```

## 部署到Cloudflare Pages

1. 登录Cloudflare账号
2. 点击"Pages"选项
3. 点击"Create a project"
4. 选择"Connect to Git"
5. 选择你的Git仓库（需要先将项目推送到Git仓库）
6. 配置构建设置：
   - 构建命令：`echo "Building static site"`
   - 构建输出目录：`/`
7. 点击"Deploy site"
8. 等待部署完成，获取部署URL

## 后续更新

后续可以通过以下方式更新内容：
1. 修改首页的个人信息和课程列表
2. 更新各课程的详细内容
3. 添加新的课程页面
4. 自定义页面样式和布局

## 技术栈

- HTML5
- CSS3 (Tailwind CSS)
- JavaScript
- Font Awesome 图标库