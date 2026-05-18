#!/usr/bin/env python3
import os

# 每个项目的专属内容
PROJECT_CONTENTS = {
    3: {
        'title': '购物篮分析',
        'icon': '🛒',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'market_basket.csv',
        'description': '学习关联规则挖掘，使用Apriori算法分析购物篮数据，发现商品之间的关联关系。',
        'search_data': [
            {'title': '关联规则', 'section': '什么是关联规则', 'content': '支持度 置信度 提升度'},
            {'title': 'Apriori算法', 'section': 'Apriori原理', 'content': '频繁项集 最小支持度'},
            {'title': '购物篮分析', 'section': '实战案例', 'content': '商品关联分析'},
            {'title': '支持度', 'section': '支持度计算', 'content': 'support'},
            {'title': '置信度', 'section': '置信度计算', 'content': 'confidence'},
            {'title': '提升度', 'section': '提升度计算', 'content': 'lift'}
        ],
        'chapters': [
            {
                'title': '第一章 关联规则基础',
                'sections': [
                    {'name': '1.1 什么是关联规则', 'content': '''
关联规则是数据挖掘中的重要技术，用于发现数据集中项之间的关系。
在购物篮分析中，可以发现诸如"购买牛奶的顾客也倾向于购买面包"这样的规则。

**核心概念：**
- **支持度(Support)**：项集出现的频率
- **置信度(Confidence)**：规则成立的概率  
- **提升度(Lift)**：规则的强度指标
                    '''},
                    {'name': '1.2 Apriori算法原理', 'content': '''
Apriori算法是发现频繁项集的经典算法：

1. 生成所有单个项目的项集
2. 筛选出满足最小支持度的项集（频繁项集）
3. 用频繁项集生成候选集
4. 重复步骤2-3直到没有新的频繁项集
                    '''}
                ]
            },
            {
                'title': '第二章 支持度与置信度',
                'sections': [
                    {'name': '2.1 支持度计算', 'content': '''
支持度 = 包含项集的交易数 / 总交易数

示例：
- 总交易数：1000
- 购买牛奶的交易数：200
- 支持度 = 200/1000 = 0.2
                    '''},
                    {'name': '2.2 置信度计算', 'content': '''
置信度(A→B) = 支持度(A∪B) / 支持度(A)

示例：
- 同时购买牛奶和面包的交易：150
- 购买牛奶的交易：200
- 置信度(牛奶→面包) = 150/200 = 0.75
                    '''}
                ]
            },
            {
                'title': '第三章 Apriori实现',
                'sections': [
                    {'name': '3.1 手动实现Apriori', 'content': '''
我们可以手动实现简单的Apriori算法来理解其原理。

步骤：
1. 扫描数据集，计算每个项的支持度
2. 筛选出满足最小支持度的项
3. 生成候选集并计算支持度
4. 重复直到没有新的频繁项集
                    '''},
                    {'name': '3.2 使用MLxtend库', 'content': '''
实际应用中，我们使用现成的库：

pip install mlxtend

from mlxtend.frequent_patterns import apriori, association_rules
                    '''}
                ]
            },
            {
                'title': '第四章 实战项目',
                'sections': [
                    {'name': '4.1 数据准备', 'content': '''
购物篮数据通常是交易记录格式，需要转换为稀疏矩阵格式。
                    '''},
                    {'name': '4.2 分析结果解读', 'content': '''
分析生成的关联规则，找出有价值的商业洞察：
- 哪些商品经常一起购买？
- 哪些商品组合有最高的提升度？
                    '''}
                ]
            }
        ],
        'practice_code': '''# 购物篮分析练习
import pandas as pd

# 创建模拟购物篮数据
data = {
    'transaction_id': ['T1', 'T1', 'T2', 'T2', 'T3', 'T3', 'T4'],
    'item': ['牛奶', '面包', '牛奶', '鸡蛋', '面包', '鸡蛋', '牛奶']
}
df = pd.DataFrame(data)

# 转换为交易格式
transactions = df.groupby('transaction_id')['item'].apply(list).tolist()
print("交易数据:", transactions)

# 计算支持度
total_transactions = len(transactions)
item_counts = {}
for transaction in transactions:
    for item in transaction:
        item_counts[item] = item_counts.get(item, 0) + 1

print("\\n各商品支持度:")
for item, count in item_counts.items():
    support = count / total_transactions
    print(f"{item}: {support:.2f}")''',
        'test_questions': [
            {'q': '关联规则中，支持度衡量的是什么？', 'options': ['规则的强度', '项集出现的频率', '规则的可信度', '规则的提升程度'], 'answer': 1},
            {'q': '置信度(A→B)的计算公式是什么？', 'options': ['support(A)/support(B)', 'support(A∪B)/support(A)', 'support(A∩B)/support(B)', 'support(B)/support(A)'], 'answer': 1},
            {'q': 'Apriori算法的核心思想是什么？', 'options': ['频繁项集的子集也是频繁的', '随机采样', '神经网络', '决策树'], 'answer': 0},
            {'q': '提升度大于1表示什么？', 'options': ['规则无意义', '两个事件负相关', '两个事件正相关', '独立事件'], 'answer': 2},
            {'q': '最小支持度的作用是什么？', 'options': ['筛选频繁项集', '计算置信度', '计算提升度', '生成规则'], 'answer': 0}
        ],
        'homework_code': '''# 购物篮分析作业
import pandas as pd

# 创建购物篮数据
data = {
    'transaction_id': ['T1', 'T1', 'T1', 'T2', 'T2', 'T3', 'T3', 'T3', 'T4', 'T4'],
    'item': ['牛奶', '面包', '鸡蛋', '牛奶', '面包', '面包', '鸡蛋', '果汁', '牛奶', '果汁']
}
df = pd.DataFrame(data)

# 1. 将数据转换为交易列表
transactions = df.groupby('transaction_id')['item'].apply(list).tolist()

# 2. 计算每个商品的支持度
total_trans = len(transactions)
item_support = {}

for trans in transactions:
    for item in trans:
        item_support[item] = item_support.get(item, 0) + 1

# 3. 计算支持度并输出
print("各商品支持度:")
for item, count in item_support.items():
    support = count / total_trans
    print(f"{item}: {support:.2f}")

# 4. 计算两个商品同时出现的支持度
print("\\n商品组合支持度:")
items = list(item_support.keys())
for i in range(len(items)):
    for j in range(i+1, len(items)):
        count = 0
        for trans in transactions:
            if items[i] in trans and items[j] in trans:
                count += 1
        support = count / total_trans
        print(f"{items[i]} & {items[j]}: {support:.2f}")''',
        'project_id': 'project3',
        'homework_key': 'homework_project3'
    },
    4: {
        'title': '客户聚类分析',
        'icon': '👥',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'customer_features.csv',
        'description': '使用K-Means算法对客户进行分群，理解客户行为特征。',
        'search_data': [
            {'title': 'K-Means', 'section': 'K-Means算法', 'content': '聚类 簇 质心'},
            {'title': '聚类分析', 'section': '聚类概念', 'content': '无监督学习 分组'},
            {'title': '肘部法则', 'section': '选择K值', 'content': 'elbow method'},
            {'title': '轮廓系数', 'section': '评估聚类', 'content': 'silhouette score'},
            {'title': '标准化', 'section': '数据预处理', 'content': 'StandardScaler'},
            {'title': '客户分群', 'section': '实战应用', 'content': '客户细分'}
        ],
        'chapters': [
            {
                'title': '第一章 聚类分析基础',
                'sections': [
                    {'name': '1.1 什么是聚类分析', 'content': '''
聚类分析是一种无监督学习方法，用于将数据分组到不同的簇中。
同一簇内的数据点相似度高，不同簇之间的数据点相似度低。

**聚类的应用场景：**
- 客户细分
- 市场细分
- 图像分割
- 异常检测
                    '''},
                    {'name': '1.2 K-Means算法原理', 'content': '''
K-Means是最常用的聚类算法：

1. 随机选择K个质心
2. 将每个数据点分配到最近的质心
3. 重新计算每个簇的质心
4. 重复步骤2-3直到质心不再变化

**核心概念：**
- **质心(Centroid)**：簇的中心点
- **距离度量**：通常使用欧氏距离
- **K值**：簇的数量
                    '''}
                ]
            },
            {
                'title': '第二章 K-Means实现',
                'sections': [
                    {'name': '2.1 使用Scikit-learn', 'content': '''
from sklearn.cluster import KMeans

# 创建模型
kmeans = KMeans(n_clusters=3, random_state=42)

# 训练模型
kmeans.fit(X)

# 获取聚类结果
labels = kmeans.labels_
centers = kmeans.cluster_centers_
                    '''},
                    {'name': '2.2 选择最佳K值', 'content': '''
使用肘部法则选择K值：

1. 尝试不同的K值
2. 计算每个K值的惯性值(inertia)
3. 找到惯性值下降变缓的点（肘部）
                    '''}
                ]
            },
            {
                'title': '第三章 数据预处理',
                'sections': [
                    {'name': '3.1 数据标准化', 'content': '''
K-Means对数据尺度敏感，需要标准化：

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
                    '''},
                    {'name': '3.2 特征选择', 'content': '''
选择对聚类有意义的特征：
- 客户消费金额
- 购买频率
- 最近购买时间
- 购买品类数量
                    '''}
                ]
            },
            {
                'title': '第四章 客户分群实战',
                'sections': [
                    {'name': '4.1 RFM模型', 'content': '''
RFM是客户分析的经典模型：
- Recency：最近购买时间
- Frequency：购买频率
- Monetary：消费金额
                    '''},
                    {'name': '4.2 分析聚类结果', 'content': '''
分析每个客户群体的特征：
- 高价值客户：高消费、高频次
- 沉睡客户：长时间未购买
- 新客户：刚注册不久
                    '''}
                ]
            }
        ],
        'practice_code': '''# K-Means聚类练习
import pandas as pd
import numpy as np

# 创建客户数据
data = {
    'customer_id': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
    'avg_spend': [500, 1200, 80, 600, 1500, 100],
    'purchase_freq': [2, 8, 1, 3, 10, 2]
}
df = pd.DataFrame(data)

print("客户数据:")
print(df)

# 简单的K-Means实现（手动）
def simple_kmeans(X, k=2, max_iter=100):
    # 随机初始化质心
    centroids = X.sample(k).values
    
    for _ in range(max_iter):
        # 计算距离并分配簇
        distances = np.sqrt(((X.values[:, np.newaxis] - centroids)**2).sum(axis=2))
        labels = np.argmin(distances, axis=1)
        
        # 更新质心
        new_centroids = np.array([X.values[labels == i].mean(axis=0) for i in range(k)])
        
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    
    return labels, centroids

# 执行聚类
labels, centers = simple_kmeans(df[['avg_spend', 'purchase_freq']], k=2)
df['cluster'] = labels

print("\\n聚类结果:")
print(df)''',
        'test_questions': [
            {'q': 'K-Means算法属于什么类型的学习？', 'options': ['监督学习', '无监督学习', '强化学习', '半监督学习'], 'answer': 1},
            {'q': 'K-Means中K代表什么？', 'options': ['迭代次数', '簇的数量', '学习率', '特征数'], 'answer': 1},
            {'q': '肘部法则用于什么目的？', 'options': ['选择K值', '计算质心', '评估模型', '数据标准化'], 'answer': 0},
            {'q': 'K-Means对什么敏感？', 'options': ['数据顺序', '数据尺度', '特征数量', '样本数量'], 'answer': 1},
            {'q': 'RFM模型中的F代表什么？', 'options': ['Recency', 'Frequency', 'Monetary', 'Revenue'], 'answer': 1}
        ],
        'homework_code': '''# 客户聚类分析作业
import pandas as pd
import numpy as np

# 创建客户RFM数据
data = {
    'customer': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
    'recency': [5, 30, 100, 10, 200, 15, 50, 80],  # 最近购买天数
    'frequency': [12, 2, 1, 8, 1, 15, 3, 2],       # 年购买次数
    'monetary': [3000, 500, 100, 2000, 200, 4000, 800, 300]  # 年消费金额
}
df = pd.DataFrame(data)

print("客户RFM数据:")
print(df)

# 数据标准化（简单版本）
df_norm = (df[['recency', 'frequency', 'monetary']] - df[['recency', 'frequency', 'monetary']].mean()) / df[['recency', 'frequency', 'monetary']].std()

print("\\n标准化后数据:")
print(df_norm)

# 简单K-Means聚类
def kmeans_simple(X, k=3):
    centroids = X.sample(k).values
    for _ in range(50):
        dists = np.sqrt(((X.values[:, np.newaxis] - centroids)**2).sum(axis=2))
        labels = np.argmin(dists, axis=1)
        new_centroids = np.array([X.values[labels == i].mean(axis=0) for i in range(k)])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return labels

df['cluster'] = kmeans_simple(df_norm)

print("\\n聚类结果:")
print(df)

# 分析每个簇的特征
print("\\n各簇统计:")
print(df.groupby('cluster')[['recency', 'frequency', 'monetary']].mean())''',
        'project_id': 'project4',
        'homework_key': 'homework_project4'
    },
    5: {
        'title': '数据可视化',
        'icon': '📈',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'retail_orders.csv',
        'description': '使用Matplotlib和Seaborn创建美观的数据图表，直观展示数据洞察。',
        'search_data': [
            {'title': 'Matplotlib', 'section': 'Matplotlib基础', 'content': 'plot bar scatter'},
            {'title': 'Seaborn', 'section': 'Seaborn高级', 'content': '统计图表'},
            {'title': '折线图', 'section': '趋势展示', 'content': 'line plot'},
            {'title': '柱状图', 'section': '对比分析', 'content': 'bar chart'},
            {'title': '散点图', 'section': '关系分析', 'content': 'scatter plot'},
            {'title': '热力图', 'section': '相关性', 'content': 'heatmap'}
        ],
        'chapters': [
            {
                'title': '第一章 Matplotlib基础',
                'sections': [
                    {'name': '1.1 基本图表类型', 'content': '''
Matplotlib是Python最常用的数据可视化库：

**常用图表类型：**
- 折线图：展示趋势变化
- 柱状图：比较不同类别
- 散点图：展示变量关系
- 直方图：展示数据分布
- 饼图：展示占比关系
                    '''},
                    {'name': '1.2 基本绘图语法', 'content': '''
import matplotlib.pyplot as plt

# 创建数据
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 绘制折线图
plt.plot(x, y)
plt.title('简单折线图')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.show()
                    '''}
                ]
            },
            {
                'title': '第二章 Seaborn高级可视化',
                'sections': [
                    {'name': '2.1 统计图表', 'content': '''
Seaborn提供更美观的统计图表：

import seaborn as sns
import pandas as pd

# 散点图带回归线
sns.regplot(x='x', y='y', data=df)

# 箱线图
sns.boxplot(x='category', y='value', data=df)

# 热力图
corr = df.corr()
sns.heatmap(corr, annot=True)
                    '''},
                    {'name': '2.2 样式设置', 'content': '''
设置图表样式：

sns.set_style('whitegrid')  # 白色网格背景
sns.set_palette('viridis')  # 颜色方案
plt.figure(figsize=(12, 6))  # 图表大小
                    '''}
                ]
            },
            {
                'title': '第三章 图表美化',
                'sections': [
                    {'name': '3.1 添加标题和标签', 'content': '''
清晰的标题和标签是图表的重要组成部分：

plt.title('销售趋势分析', fontsize=16)
plt.xlabel('月份', fontsize=12)
plt.ylabel('销售额(万元)', fontsize=12)
plt.legend(['2023年', '2024年'])
                    '''},
                    {'name': '3.2 保存图表', 'content': '''
保存高质量图表：

plt.savefig('sales_trend.png', dpi=300, bbox_inches='tight')

# dpi：分辨率
# bbox_inches：裁剪空白区域
                    '''}
                ]
            },
            {
                'title': '第四章 实战案例',
                'sections': [
                    {'name': '4.1 销售数据分析', 'content': '''
分析销售数据的关键指标：
- 月度销售趋势
- 各品类销售占比
- 地区销售对比
                    '''},
                    {'name': '4.2 数据分布分析', 'content': '''
分析数据分布特征：
- 客户消费金额分布
- 订单数量分布
- 相关性分析
                    '''}
                ]
            }
        ],
        'practice_code': '''# 数据可视化练习
import matplotlib.pyplot as plt

# 创建数据
months = ['1月', '2月', '3月', '4月', '5月', '6月']
sales_2023 = [120, 150, 130, 180, 200, 220]
sales_2024 = [150, 180, 160, 200, 230, 250]

# 创建图表
plt.figure(figsize=(10, 6))

# 绘制折线图
plt.plot(months, sales_2023, marker='o', label='2023年', linewidth=2)
plt.plot(months, sales_2024, marker='s', label='2024年', linewidth=2)

# 添加标题和标签
plt.title('月度销售额对比', fontsize=16)
plt.xlabel('月份', fontsize=12)
plt.ylabel('销售额(万元)', fontsize=12)

# 添加图例和网格
plt.legend()
plt.grid(True, alpha=0.3)

print("图表已创建，准备显示...")
print("2023年总销售额:", sum(sales_2023))
print("2024年总销售额:", sum(sales_2024))''',
        'test_questions': [
            {'q': 'Matplotlib中绘制折线图使用哪个函数？', 'options': ['plt.bar()', 'plt.plot()', 'plt.scatter()', 'plt.hist()'], 'answer': 1},
            {'q': 'Seaborn中绘制热力图使用哪个函数？', 'options': ['sns.lineplot()', 'sns.barplot()', 'sns.heatmap()', 'sns.scatterplot()'], 'answer': 2},
            {'q': 'plt.savefig()中dpi参数代表什么？', 'options': ['图表宽度', '分辨率', '颜色深度', '保存格式'], 'answer': 1},
            {'q': '箱线图主要展示什么？', 'options': ['趋势变化', '数据分布', '相关性', '占比关系'], 'answer': 1},
            {'q': '设置图表大小使用哪个参数？', 'options': ['size', 'figsize', 'width', 'dimensions'], 'answer': 1}
        ],
        'homework_code': '''# 数据可视化作业
import matplotlib.pyplot as plt

# 创建销售数据
categories = ['电子产品', '服装', '食品', '日用品', '图书']
sales = [350, 280, 180, 220, 120]
growth = [15, 8, -5, 12, 20]  # 增长率(%)

# 创建子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 第一个子图：柱状图
ax1.bar(categories, sales, color=['#00d4ff', '#8b5cf6', '#4ade80', '#fbbf24', '#f87171'])
ax1.set_title('各品类销售额', fontsize=14)
ax1.set_xlabel('品类', fontsize=12)
ax1.set_ylabel('销售额(万元)', fontsize=12)

# 第二个子图：横向柱状图（展示增长率）
ax2.barh(categories, growth, color='#00d4ff')
ax2.set_title('各品类增长率', fontsize=14)
ax2.set_xlabel('增长率(%)', fontsize=12)
ax2.axvline(0, color='gray', linestyle='--')

plt.tight_layout()
print("图表创建完成！")
print("销售总额:", sum(sales), "万元")
print("平均增长率:", sum(growth)/len(growth), "%")''',
        'project_id': 'project5',
        'homework_key': 'homework_project5'
    },
    6: {
        'title': 'A/B测试分析',
        'icon': '🔬',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'ab_test.csv',
        'description': '学习设计和分析A/B测试，验证产品改动的效果。',
        'search_data': [
            {'title': 'A/B测试', 'section': 'A/B测试基础', 'content': '对照组 实验组'},
            {'title': '假设检验', 'section': '统计检验', 'content': 't检验 z检验'},
            {'title': 'p值', 'section': 'p值解读', 'content': '显著性水平'},
            {'title': '样本量', 'section': '样本量计算', 'content': 'power analysis'},
            {'title': '转化率', 'section': '转化率分析', 'content': 'conversion rate'},
            {'title': '统计显著性', 'section': '结果判断', 'content': 'significant'}
        ],
        'chapters': [
            {
                'title': '第一章 A/B测试基础',
                'sections': [
                    {'name': '1.1 什么是A/B测试', 'content': '''
A/B测试是一种对照实验方法：
- 将用户随机分成两组
- 对照组(A组)：使用原有版本
- 实验组(B组)：使用新版本
- 比较两组的关键指标差异

**应用场景：**
- 网页设计优化
- 产品功能测试
- 营销策略对比
                    '''},
                    {'name': '1.2 测试设计原则', 'content': '''
设计A/B测试的关键原则：
1. 单一变量原则：只改变一个变量
2. 随机分配：确保两组用户特征相似
3. 足够样本量：保证统计显著性
4. 盲法测试：测试者不知道分组
                    '''}
                ]
            },
            {
                'title': '第二章 假设检验',
                'sections': [
                    {'name': '2.1 零假设与备择假设', 'content': '''
- **零假设(H0)**：两组没有差异
- **备择假设(H1)**：两组存在差异

**双尾检验vs单尾检验：**
- 双尾：检验是否有差异（不关心方向）
- 单尾：检验是否优于/劣于（关心方向）
                    '''},
                    {'name': '2.2 p值与显著性', 'content': '''
p值表示在零假设成立时，观察到当前数据的概率。

**判断标准：**
- p < 0.05：拒绝零假设，差异显著
- p >= 0.05：不能拒绝零假设

注意：p值不是效应大小的度量！
                    '''}
                ]
            },
            {
                'title': '第三章 常用统计检验',
                'sections': [
                    {'name': '3.1 比例检验（转化率）', 'content': '''
比较两组转化率差异：

from statsmodels.stats.proportion import proportions_ztest

count = [conversions_a, conversions_b]
nobs = [total_a, total_b]
z_stat, p_value = proportions_ztest(count, nobs)
                    '''},
                    {'name': '3.2 t检验（均值比较）', 'content': '''
比较两组均值差异：

from scipy.stats import ttest_ind

t_stat, p_value = ttest_ind(group_a, group_b)
                    '''}
                ]
            },
            {
                'title': '第四章 样本量计算',
                'sections': [
                    {'name': '4.1 影响样本量的因素', 'content': '''
1. 预期效应大小：希望检测的最小差异
2. 显著性水平(α)：通常0.05
3. 统计功效(β)：通常0.8（检测到真实效应的概率）
4. 基线转化率：原有版本的转化率
                    '''},
                    {'name': '4.2 样本量计算公式', 'content': '''
样本量 = (Zα/2 + Zβ)² × (p1(1-p1) + p2(1-p2)) / (p1-p2)²

可以使用statsmodels或在线计算器计算。
                    '''}
                ]
            }
        ],
        'practice_code': '''# A/B测试分析练习
import numpy as np
from scipy.stats import norm

# 模拟A/B测试数据
np.random.seed(42)

# 对照组：转化率15%
n_a = 1000
conversion_a = np.random.binomial(n_a, 0.15)

# 实验组：转化率18%
n_b = 1000
conversion_b = np.random.binomial(n_b, 0.18)

print(f"对照组: {n_a}人, 转化{conversion_a}人, 转化率{(conversion_a/n_a):.2%}")
print(f"实验组: {n_b}人, 转化{conversion_b}人, 转化率{(conversion_b/n_b):.2%}")

# 计算转化率差异
p_a = conversion_a / n_a
p_b = conversion_b / n_b
diff = p_b - p_a
print(f"\\n转化率差异: {diff:.2%}")

# 计算标准误
se = np.sqrt(p_a*(1-p_a)/n_a + p_b*(1-p_b)/n_b)
z_score = diff / se
p_value = 2 * (1 - norm.cdf(abs(z_score)))

print(f"Z值: {z_score:.2f}")
print(f"p值: {p_value:.4f}")

# 判断结果
if p_value < 0.05:
    print("结果显著！拒绝零假设，实验组效果更好。")
else:
    print("结果不显著，无法拒绝零假设。")''',
        'test_questions': [
            {'q': 'A/B测试中，零假设是什么？', 'options': ['实验组更好', '对照组更好', '两组没有差异', '差异显著'], 'answer': 2},
            {'q': 'p值小于0.05意味着什么？', 'options': ['差异不显著', '拒绝零假设', '接受零假设', '效应很大'], 'answer': 1},
            {'q': '比较转化率差异应该使用什么检验？', 'options': ['t检验', '比例检验', '方差分析', '卡方检验'], 'answer': 1},
            {'q': '统计功效通常设置为多少？', 'options': ['0.5', '0.8', '0.95', '0.99'], 'answer': 1},
            {'q': '单一变量原则的含义是什么？', 'options': ['只测试一个指标', '只改变一个变量', '只用一组用户', '只运行一次'], 'answer': 1}
        ],
        'homework_code': '''# A/B测试分析作业
import numpy as np
from scipy.stats import norm

# A/B测试数据
data = {
    'group': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'visitors': [2000, 2200, 1800, 2100, 1900, 2000, 2100, 1900, 2200, 1800],
    'conversions': [300, 330, 270, 315, 285, 360, 399, 342, 396, 324]
}

df = pd.DataFrame(data)

# 计算总访客和转化数
total_a = df[df['group'] == 'A']['visitors'].sum()
total_b = df[df['group'] == 'B']['visitors'].sum()
conv_a = df[df['group'] == 'A']['conversions'].sum()
conv_b = df[df['group'] == 'B']['conversions'].sum()

print(f"对照组(A): {total_a}访客, {conv_a}转化, 转化率{(conv_a/total_a):.2%}")
print(f"实验组(B): {total_b}访客, {conv_b}转化, 转化率{(conv_b/total_b):.2%}")

# 计算统计显著性
p_a = conv_a / total_a
p_b = conv_b / total_b
diff = p_b - p_a

se = np.sqrt(p_a*(1-p_a)/total_a + p_b*(1-p_b)/total_b)
z_score = diff / se
p_value = 2 * (1 - norm.cdf(abs(z_score)))

print(f"\\n转化率提升: {diff:.2%}")
print(f"Z值: {z_score:.2f}")
print(f"p值: {p_value:.4f}")

# 计算置信区间
margin = 1.96 * se
print(f"95%置信区间: [{(diff-margin):.2%}, {(diff+margin):.2%}]")''',
        'project_id': 'project6',
        'homework_key': 'homework_project6'
    },
    7: {
        'title': '时间序列分析',
        'icon': '⏰',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'time_series_sales.csv',
        'description': '分析时间序列数据，识别趋势和季节性模式，进行预测。',
        'search_data': [
            {'title': '时间序列', 'section': '时间序列基础', 'content': '趋势 季节性 周期性'},
            {'title': '移动平均', 'section': '平滑方法', 'content': 'moving average'},
            {'title': '指数平滑', 'section': '指数加权', 'content': 'exponential smoothing'},
            {'title': 'ARIMA', 'section': 'ARIMA模型', 'content': '自回归 差分 移动平均'},
            {'title': '趋势分析', 'section': '趋势识别', 'content': 'trend analysis'},
            {'title': '季节性', 'section': '季节模式', 'content': 'seasonality'}
        ],
        'chapters': [
            {
                'title': '第一章 时间序列基础',
                'sections': [
                    {'name': '1.1 时间序列组成', 'content': '''
时间序列数据由以下成分组成：

1. **趋势(Trend)**：长期上升或下降的趋势
2. **季节性(Seasonality)**：周期性重复的模式
3. **周期性(Cycle)**：非固定周期的波动
4. **残差(Residual)**：随机波动

**示例：**
- 销售数据通常有年度季节性
- 股票价格有趋势和随机波动
                    '''},
                    {'name': '1.2 时间序列数据格式', 'content': '''
处理时间序列的关键步骤：

1. 将日期列转换为datetime类型
2. 设置日期为索引
3. 处理缺失值
4. 按时间排序

import pandas as pd

df = pd.read_csv('sales.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
                    '''}
                ]
            },
            {
                'title': '第二章 时间序列可视化',
                'sections': [
                    {'name': '2.1 绘制时间序列', 'content': '''
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制时间序列图
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['sales'])
plt.title('销售趋势')
plt.ylabel('销售额')
plt.show()

# 季节性分解图
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(df['sales'], period=12)
decomposition.plot()
                    '''},
                    {'name': '2.2 滚动统计', 'content': '''
计算滚动统计量：

# 滚动均值
df['rolling_mean'] = df['sales'].rolling(window=30).mean()

# 滚动标准差
df['rolling_std'] = df['sales'].rolling(window=30).std()
                    '''}
                ]
            },
            {
                'title': '第三章 时间序列预测',
                'sections': [
                    {'name': '3.1 移动平均预测', 'content': '''
简单移动平均：

def moving_average(data, window=7):
    return data.rolling(window=window).mean()

# 预测下一个值
last_window = df['sales'].tail(7)
prediction = last_window.mean()
                    '''},
                    {'name': '3.2 指数平滑', 'content': '''
指数加权移动平均：

# alpha是平滑系数(0-1)
alpha = 0.3
df['ewma'] = df['sales'].ewm(alpha=alpha).mean()

# 预测公式
# forecast = alpha * last_value + (1-alpha) * last_forecast
                    '''}
                ]
            },
            {
                'title': '第四章 ARIMA模型',
                'sections': [
                    {'name': '4.1 ARIMA参数', 'content': '''
ARIMA(p, d, q)：
- p：自回归阶数
- d：差分阶数（使数据平稳）
- q：移动平均阶数

from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(df['sales'], order=(1, 1, 1))
result = model.fit()
forecast = result.predict(start=len(df), end=len(df)+7)
                    '''},
                    {'name': '4.2 模型评估', 'content': '''
评估预测准确性：

from sklearn.metrics import mean_squared_error

# 均方误差
mse = mean_squared_error(y_true, y_pred)

# 平均绝对百分比误差
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
                    '''}
                ]
            }
        ],
        'practice_code': '''# 时间序列分析练习
import pandas as pd
import numpy as np

# 创建时间序列数据
dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
sales = 100 + np.sin(np.arange(30)*2*np.pi/7) * 20 + np.random.randn(30)*5

df = pd.DataFrame({'date': dates, 'sales': sales})
df = df.set_index('date')

print("时间序列数据:")
print(df.head())

# 计算7日移动平均
df['ma7'] = df['sales'].rolling(window=7).mean()

# 计算指数平滑
df['ewma'] = df['sales'].ewm(alpha=0.3).mean()

print("\\n统计摘要:")
print(f"平均销售额: {df['sales'].mean():.2f}")
print(f"最大销售额: {df['sales'].max():.2f}")
print(f"最小销售额: {df['sales'].min():.2f}")

# 预测下一天销售额（使用移动平均）
last_ma = df['ma7'].iloc[-1]
print(f"\\n下一天预测销售额: {last_ma:.2f}")''',
        'test_questions': [
            {'q': '时间序列的四个组成部分不包括？', 'options': ['趋势', '季节性', '周期性', '相关性'], 'answer': 3},
            {'q': '移动平均的主要作用是什么？', 'options': ['增加噪声', '平滑数据', '预测长期趋势', '检测异常值'], 'answer': 1},
            {'q': 'ARIMA模型中的d代表什么？', 'options': ['自回归阶数', '差分阶数', '移动平均阶数', '数据维度'], 'answer': 1},
            {'q': '指数平滑中alpha值越大意味着什么？', 'options': ['越重视历史数据', '越重视近期数据', '越平滑', '预测越稳定'], 'answer': 1},
            {'q': '季节性分解使用什么方法？', 'options': ['ARIMA', '移动平均', 'STL分解', '线性回归'], 'answer': 2}
        ],
        'homework_code': '''# 时间序列分析作业
import pandas as pd
import numpy as np

# 创建月度销售数据
dates = pd.date_range(start='2023-01-01', periods=24, freq='M')

# 添加趋势和季节性
trend = np.linspace(100, 200, 24)
seasonality = np.sin(np.arange(24)*2*np.pi/12) * 30
noise = np.random.randn(24)*5

sales = trend + seasonality + noise

df = pd.DataFrame({'date': dates, 'sales': sales})
df = df.set_index('date')

print("时间序列数据:")
print(df.head())

# 1. 计算移动平均
df['ma3'] = df['sales'].rolling(window=3).mean()
df['ma6'] = df['sales'].rolling(window=6).mean()

# 2. 计算指数平滑
df['ewma_03'] = df['sales'].ewm(alpha=0.3).mean()
df['ewma_07'] = df['sales'].ewm(alpha=0.7).mean()

# 3. 分析季节性模式
monthly_avg = df.groupby(df.index.month)['sales'].mean()
print("\\n各月平均销售额:")
print(monthly_avg)

# 4. 预测下一个月
last_3_months = df['sales'].tail(3)
prediction = last_3_months.mean()
print(f"\\n下一个月预测销售额: {prediction:.2f}")''',
        'project_id': 'project7',
        'homework_key': 'homework_project7'
    },
    8: {
        'title': '特征工程',
        'icon': '🔧',
        'level': '高级',
        'level_class': 'badge-hard',
        'dataset': 'customer_features.csv',
        'description': '学习特征提取、编码和选择技术，提升模型性能。',
        'search_data': [
            {'title': '特征提取', 'section': '特征创建', 'content': 'feature extraction'},
            {'title': '特征编码', 'section': '类别编码', 'content': 'one-hot encoding label encoding'},
            {'title': '特征选择', 'section': '特征筛选', 'content': 'feature selection'},
            {'title': '特征缩放', 'section': '标准化归一化', 'content': 'scaling normalization'},
            {'title': '特征交互', 'section': '特征组合', 'content': 'feature interaction'},
            {'title': '降维', 'section': 'PCA', 'content': 'principal component analysis'}
        ],
        'chapters': [
            {
                'title': '第一章 特征工程概述',
                'sections': [
                    {'name': '1.1 什么是特征工程', 'content': '''
特征工程是将原始数据转换为机器学习模型可用特征的过程。

**特征工程的重要性：**
- 好的特征可以大幅提升模型性能
- 数据决定了模型的上限
- 特征工程是数据分析的核心技能

**特征类型：**
- 数值型特征
- 类别型特征
- 时间特征
- 文本特征
                    '''},
                    {'name': '1.2 特征工程流程', 'content': '''
1. **数据理解**：分析数据类型和分布
2. **特征提取**：从原始数据创建特征
3. **特征转换**：编码、缩放、变换
4. **特征选择**：选择最有信息量的特征
5. **特征评估**：验证特征效果
                    '''}
                ]
            },
            {
                'title': '第二章 类别特征编码',
                'sections': [
                    {'name': '2.1 独热编码', 'content': '''
适合类别无顺序关系的情况：

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(df[['category']])
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())
                    '''},
                    {'name': '2.2 标签编码', 'content': '''
适合类别有顺序关系的情况：

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df['encoded'] = encoder.fit_transform(df['category'])

注意：仅用于目标变量或有序类别
                    '''},
                    {'name': '2.3 目标编码', 'content': '''
用目标变量的均值编码：

mean_target = df.groupby('category')['target'].mean()
df['target_encoded'] = df['category'].map(mean_target)

注意：可能导致过拟合，需要交叉验证
                    '''}
                ]
            },
            {
                'title': '第三章 数值特征处理',
                'sections': [
                    {'name': '3.1 特征缩放', 'content': '''
标准化和归一化：

from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 标准化（均值为0，标准差为1）
scaler = StandardScaler()
df['scaled'] = scaler.fit_transform(df[['value']])

# 归一化（缩放到0-1）
scaler = MinMaxScaler()
df['normalized'] = scaler.fit_transform(df[['value']])
                    '''},
                    {'name': '3.2 特征变换', 'content': '''
对数变换和幂变换：

# 对数变换（处理右偏分布）
df['log_value'] = np.log1p(df['value'])

# 平方根变换
df['sqrt_value'] = np.sqrt(df['value'])

# Box-Cox变换
from scipy.stats import boxcox
df['boxcox'], _ = boxcox(df['value'])
                    '''}
                ]
            },
            {
                'title': '第四章 特征选择',
                'sections': [
                    {'name': '4.1 过滤法', 'content': '''
基于统计指标选择特征：

# 相关系数
corr_matrix = df.corr()

# 方差阈值
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0.1)
selected = selector.fit_transform(df)
                    '''},
                    {'name': '4.2 包裹法', 'content': '''
基于模型性能选择特征：

from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

rfe = RFE(estimator=LinearRegression(), n_features_to_select=5)
selected = rfe.fit_transform(X, y)
                    '''},
                    {'name': '4.3 嵌入法', 'content': '''
使用正则化模型选择特征：

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.1)
lasso.fit(X, y)
important_features = np.where(lasso.coef_ != 0)[0]
                    '''}
                ]
            }
        ],
        'practice_code': '''# 特征工程练习
import pandas as pd
import numpy as np

# 创建示例数据
data = {
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
    'age': [25, 30, 35, 40, 45, 50, 55, 60],
    'income': [5000, 8000, 6000, 12000, 10000, 7000, 15000, 9000],
    'target': [0, 1, 0, 1, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

print("原始数据:")
print(df)

# 1. 独热编码
encoded = pd.get_dummies(df['category'], prefix='cat')
df_encoded = pd.concat([df, encoded], axis=1)
print("\\n独热编码后:")
print(df_encoded[['cat_A', 'cat_B', 'cat_C']])

# 2. 标准化
df_encoded['income_scaled'] = (df['income'] - df['income'].mean()) / df['income'].std()
print("\\n标准化后的收入:")
print(df_encoded[['income', 'income_scaled']])

# 3. 创建交互特征
df_encoded['age_income'] = df['age'] * df['income']
print("\\n交互特征:")
print(df_encoded[['age', 'income', 'age_income']])''',
        'test_questions': [
            {'q': '独热编码适合什么类型的特征？', 'options': ['有序类别', '无序类别', '数值特征', '文本特征'], 'answer': 1},
            {'q': '标准化的目的是什么？', 'options': ['增加数据量', '使特征均值为0标准差为1', '减少特征数量', '处理缺失值'], 'answer': 1},
            {'q': 'Lasso回归可以用于什么？', 'options': ['分类任务', '特征选择', '聚类分析', '时间序列预测'], 'answer': 1},
            {'q': '对数变换适合处理什么数据？', 'options': ['左偏分布', '右偏分布', '正态分布', '均匀分布'], 'answer': 1},
            {'q': 'RFE算法属于哪种特征选择方法？', 'options': ['过滤法', '包裹法', '嵌入法', '统计法'], 'answer': 1}
        ],
        'homework_code': '''# 特征工程作业
import pandas as pd
import numpy as np

# 创建客户数据
data = {
    'gender': ['男', '女', '男', '女', '男', '女', '男', '女'],
    'education': ['本科', '硕士', '高中', '本科', '博士', '本科', '硕士', '高中'],
    'age': [28, 35, 42, 29, 50, 31, 38, 45],
    'tenure': [2, 5, 8, 3, 10, 4, 6, 7],
    'monthly_spend': [300, 800, 500, 600, 1200, 400, 900, 700],
    'churn': [0, 1, 0, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

print("原始数据:")
print(df)

# 1. 独热编码类别特征
df_encoded = pd.get_dummies(df, columns=['gender', 'education'])
print("\\n编码后的数据:")
print(df_encoded.columns.tolist())

# 2. 标准化数值特征
numeric_cols = ['age', 'tenure', 'monthly_spend']
for col in numeric_cols:
    df_encoded[f'{col}_scaled'] = (df[col] - df[col].mean()) / df[col].std()

# 3. 创建衍生特征
df_encoded['spend_per_year'] = df_encoded['monthly_spend'] * 12
df_encoded['age_group'] = pd.cut(df_encoded['age'], bins=[20, 30, 40, 50, 60], labels=['20-30', '30-40', '40-50', '50+'])

# 4. 目标编码年龄组
age_group_mean = df_encoded.groupby('age_group')['churn'].mean()
df_encoded['age_group_encoded'] = df_encoded['age_group'].map(age_group_mean)

print("\\n最终特征集:")
print(df_encoded.head())''',
        'project_id': 'project8',
        'homework_key': 'homework_project8'
    },
    9: {
        'title': '异常值检测',
        'icon': '🎯',
        'level': '高级',
        'level_class': 'badge-hard',
        'dataset': 'customer_features.csv',
        'description': '识别和处理数据中的异常值，保证数据分析的准确性。',
        'search_data': [
            {'title': '异常值', 'section': '异常值概念', 'content': 'outlier detection'},
            {'title': 'IQR方法', 'section': '四分位距', 'content': 'interquartile range'},
            {'title': 'Z-score', 'section': '标准差法', 'content': 'standard score'},
            {'title': '孤立森林', 'section': '机器学习方法', 'content': 'isolation forest'},
            {'title': 'DBSCAN', 'section': '密度聚类', 'content': 'density based'},
            {'title': '处理策略', 'section': '异常值处理', 'content': 'remove impute'}
        ],
        'chapters': [
            {
                'title': '第一章 异常值概述',
                'sections': [
                    {'name': '1.1 什么是异常值', 'content': '''
异常值是数据集中与其他数据点显著不同的值。

**异常值的来源：**
- 数据录入错误
- 测量误差
- 真实的极端情况

**异常值的影响：**
- 影响统计分析结果
- 降低模型准确性
- 误导业务决策

**检测方法分类：**
1. 统计方法（IQR、Z-score）
2. 机器学习方法（孤立森林、DBSCAN）
3. 可视化方法（箱线图、散点图）
                    '''},
                    {'name': '1.2 异常值检测流程', 'content': '''
1. **可视化探索**：绘制箱线图、直方图
2. **统计检测**：使用IQR或Z-score
3. **机器学习检测**：使用孤立森林等算法
4. **验证分析**：确认异常值原因
5. **处理决策**：删除、替换或保留
                    '''}
                ]
            },
            {
                'title': '第二章 统计方法检测',
                'sections': [
                    {'name': '2.1 IQR方法', 'content': '''
四分位距方法：

1. 计算Q1（下四分位数）和Q3（上四分位数）
2. 计算IQR = Q3 - Q1
3. 定义异常值范围：
   - 下限：Q1 - 1.5 × IQR
   - 上限：Q3 + 1.5 × IQR

代码实现：
q1 = df['value'].quantile(0.25)
q3 = df['value'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]
                    '''},
                    {'name': '2.2 Z-score方法', 'content': '''
Z-score表示数据点距离均值的标准差倍数：

z = (x - μ) / σ

通常认为|z| > 3的点是异常值。

代码实现：
z_scores = (df['value'] - df['value'].mean()) / df['value'].std()
outliers = df[abs(z_scores) > 3]

注意：假设数据服从正态分布
                    '''}
                ]
            },
            {
                'title': '第三章 机器学习方法',
                'sections': [
                    {'name': '3.1 孤立森林', 'content': '''
孤立森林是专门用于异常值检测的算法：

from sklearn.ensemble import IsolationForest

# 创建模型
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,  # 预期异常值比例
    random_state=42
)

# 训练并预测
df['anomaly'] = model.fit_predict(X)
# -1表示异常值，1表示正常值
                    '''},
                    {'name': '3.2 DBSCAN', 'content': '''
DBSCAN基于密度检测异常值：

from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.5, min_samples=5)
df['cluster'] = dbscan.fit_predict(X)
# -1表示噪声点（异常值）
                    '''}
                ]
            },
            {
                'title': '第四章 异常值处理',
                'sections': [
                    {'name': '4.1 删除异常值', 'content': '''
直接删除异常值：

df_clean = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

适用情况：
- 异常值数量较少
- 确认是数据错误
                    '''},
                    {'name': '4.2 替换异常值', 'content': '''
用统计值替换：

# 用中位数替换
median = df['value'].median()
df['value'] = np.where(
    (df['value'] < lower_bound) | (df['value'] > upper_bound),
    median,
    df['value']
)

适用情况：
- 异常值数量较多
- 需要保留样本
                    '''},
                    {'name': '4.3 保留并标记', 'content': '''
保留但标记为异常：

df['is_outlier'] = (df['value'] < lower_bound) | (df['value'] > upper_bound)

适用情况：
- 异常值可能包含有价值信息
- 需要在分析中特别处理
                    '''}
                ]
            }
        ],
        'practice_code': '''# 异常值检测练习
import pandas as pd
import numpy as np

# 创建包含异常值的数据
np.random.seed(42)
data = np.random.normal(100, 10, 100)
# 添加异常值
data[95] = 150
data[96] = 160
data[97] = 50
data[98] = 40
data[99] = 170

df = pd.DataFrame({'value': data})

print("数据统计摘要:")
print(df.describe())

# 方法1: IQR检测
q1 = df['value'].quantile(0.25)
q3 = df['value'].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers_iqr = df[(df['value'] < lower) | (df['value'] > upper)]
print(f"\\nIQR检测到的异常值数量: {len(outliers_iqr)}")

# 方法2: Z-score检测
z_scores = (df['value'] - df['value'].mean()) / df['value'].std()
outliers_z = df[abs(z_scores) > 3]
print(f"Z-score检测到的异常值数量: {len(outliers_z)}")

# 处理异常值（用中位数替换）
median = df['value'].median()
df['cleaned'] = np.where(
    (df['value'] < lower) | (df['value'] > upper),
    median,
    df['value']
)

print("\\n处理后的统计摘要:")
print(df['cleaned'].describe())''',
        'test_questions': [
            {'q': 'IQR方法中，异常值的判断标准是什么？', 'options': ['超出均值±1σ', '超出Q1/Q3±1.5×IQR', '超出中位数±2σ', '超出范围的10%'], 'answer': 1},
            {'q': 'Z-score方法假设数据服从什么分布？', 'options': ['均匀分布', '正态分布', '泊松分布', '指数分布'], 'answer': 1},
            {'q': '孤立森林中contamination参数表示什么？', 'options': ['树的数量', '预期异常值比例', '特征数量', '训练轮数'], 'answer': 1},
            {'q': 'DBSCAN中-1表示什么？', 'options': ['正常点', '噪声点', '核心点', '边界点'], 'answer': 1},
            {'q': '异常值数量较多时，最好的处理方式是？', 'options': ['直接删除', '用中位数替换', '保留不处理', '用均值替换'], 'answer': 1}
        ],
        'homework_code': '''# 异常值检测作业
import pandas as pd
import numpy as np

# 创建销售数据（包含异常值）
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=50)
sales = np.random.normal(500, 50, 50)

# 添加异常值
sales[[10, 20, 30, 40]] = [800, 200, 900, 150]

df = pd.DataFrame({'date': dates, 'sales': sales})

print("原始数据统计:")
print(df['sales'].describe())

# 1. 使用IQR方法检测异常值
q1, q3 = df['sales'].quantile([0.25, 0.75])
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

df['is_outlier'] = (df['sales'] < lower_bound) | (df['sales'] > upper_bound)
print(f"\\n检测到的异常值:")
print(df[df['is_outlier']])

# 2. 使用Z-score方法验证
z_scores = (df['sales'] - df['sales'].mean()) / df['sales'].std()
df['z_score'] = z_scores
print(f"\\nZ-score > 3的点:")
print(df[abs(z_scores) > 3][['sales', 'z_score']])

# 3. 处理异常值（用相邻两天的均值替换）
for i in df[df['is_outlier']].index:
    neighbors = []
    if i > 0:
        neighbors.append(df.loc[i-1, 'sales'])
    if i < len(df)-1:
        neighbors.append(df.loc[i+1, 'sales'])
    df.loc[i, 'sales_cleaned'] = np.mean(neighbors)
    df.loc[i, 'sales_cleaned'] = df.loc[i, 'sales']

print("\\n处理完成！")''',
        'project_id': 'project9',
        'homework_key': 'homework_project9'
    },
    10: {
        'title': '多数据集合并',
        'icon': '🔗',
        'level': '进阶',
        'level_class': 'badge-medium',
        'dataset': 'retail_orders.csv',
        'description': '学习合并、连接和拼接多个数据集，整合信息进行分析。',
        'search_data': [
            {'title': '合并', 'section': 'merge连接', 'content': 'inner outer left right join'},
            {'title': '拼接', 'section': 'concat拼接', 'content': 'concatenation'},
            {'title': '连接类型', 'section': 'join types', 'content': 'inner outer left right'},
            {'title': '索引操作', 'section': 'index operations', 'content': 'set_index reset_index'},
            {'title': '数据整合', 'section': 'data integration', 'content': 'combine merge'},
            {'title': '重复处理', 'section': 'duplicates', 'content': 'drop_duplicates'}
        ],
        'chapters': [
            {
                'title': '第一章 数据集合并基础',
                'sections': [
                    {'name': '1.1 为什么需要合并数据', 'content': '''
在实际数据分析中，数据常常分散在多个文件或表中：

- **订单表**：订单ID、用户ID、金额
- **用户表**：用户ID、姓名、注册日期
- **商品表**：商品ID、商品名称、价格

需要将这些表合并才能进行完整分析。

**合并类型：**
- 一对一合并
- 一对多合并
- 多对多合并
                    '''},
                    {'name': '1.2 关键概念', 'content': '''
**键(Key)**：用于匹配行的列（如用户ID、订单ID）

**连接类型：**
- 内连接(Inner Join)：只保留两边都有的行
- 左连接(Left Join)：保留左表所有行
- 右连接(Right Join)：保留右表所有行
- 外连接(Outer Join)：保留两边所有行
                    '''}
                ]
            },
            {
                'title': '第二章 Merge连接',
                'sections': [
                    {'name': '2.1 基本语法', 'content': '''
pd.merge(left, right, on='key_column')

# 指定连接类型
pd.merge(left, right, on='key', how='inner')  # 默认
pd.merge(left, right, on='key', how='left')
pd.merge(left, right, on='key', how='right')
pd.merge(left, right, on='key', how='outer')

# 不同列名的连接
pd.merge(left, right, left_on='id', right_on='user_id')
                    '''},
                    {'name': '2.2 多键连接', 'content': '''
按多个键连接：

pd.merge(
    orders, 
    customers, 
    on=['customer_id', 'order_date'],
    how='inner'
)
                    '''},
                    {'name': '2.3 指示器', 'content': '''
显示数据来源：

merged = pd.merge(
    df1, df2,
    on='id',
    how='outer',
    indicator=True
)
# _merge列显示：left_only, right_only, both
                    '''}
                ]
            },
            {
                'title': '第三章 Concat拼接',
                'sections': [
                    {'name': '3.1 纵向拼接', 'content': '''
将多个DataFrame按行拼接：

pd.concat([df1, df2, df3], axis=0)

# 重置索引
pd.concat([df1, df2], ignore_index=True)

# 保留原索引
pd.concat([df1, df2], keys=['df1', 'df2'])
                    '''},
                    {'name': '3.2 横向拼接', 'content': '''
按