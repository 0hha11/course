#!/usr/bin/env python3
"""
生成所有项目的专属内容
每个项目需要有：
1. 独特的学习内容匹配项目标题
2. 练习板块使用代码编辑器而不是选择题
"""

import os

projects = [
    {
        "id": "project3",
        "title": "购物篮分析",
        "icon": "🛒",
        "description": "学习关联规则挖掘，使用Apriori算法分析购物篮数据，发现商品之间的关联关系。",
        "difficulty": "badge-medium",
        "difficulty_label": "进阶",
        "dataset": "market_basket.csv",
        "chapters": [
            {
                "title": "第一章 关联规则基础",
                "sections": [
                    {
                        "subtitle": "1.1 什么是关联规则",
                        "content": "关联规则是数据挖掘中用于发现数据项之间有趣关系的方法。最经典的应用场景就是购物篮分析，比如发现购买牛奶的顾客也倾向于购买面包。",
                        "points": ["频繁项集", "支持度 (Support)", "置信度 (Confidence)", "提升度 (Lift)"],
                        "info": "💡 关联规则广泛应用于零售行业的商品推荐和货架摆放优化。"
                    },
                    {
                        "subtitle": "1.2 核心概念",
                        "content": "让我们理解关联规则的核心指标：",
                        "code": """# 支持度: P(A ∩ B) - 同时购买A和B的概率
support = len(A ∩ B) / total_transactions

# 置信度: P(B|A) - 购买A的顾客中也购买B的概率
confidence = len(A ∩ B) / len(A)

# 提升度: 衡量A和B的关联强度
lift = confidence / P(B)"""
                    }
                ]
            },
            {
                "title": "第二章 Apriori算法",
                "sections": [
                    {
                        "subtitle": "2.1 Apriori原理",
                        "content": "Apriori算法是最经典的关联规则挖掘算法，其核心思想是：如果一个项集是频繁的，那么它的所有子集也是频繁的。",
                        "points": ["扫描数据库生成候选集", "计算支持度", "剪枝不满足最小支持度的项集", "迭代直到没有新的频繁项集"],
                        "tip": "📌 Apriori算法的效率很大程度上取决于最小支持度阈值的选择。"
                    },
                    {
                        "subtitle": "2.2 Python实现Apriori",
                        "content": "使用mlxtend库实现Apriori算法：",
                        "code": """import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 创建购物篮数据
data = {
    '牛奶': [1, 1, 0, 1, 0],
    '面包': [1, 0, 1, 1, 1],
    '鸡蛋': [0, 1, 1, 0, 1],
    '黄油': [1, 1, 0, 0, 0]
}
df = pd.DataFrame(data)

# 挖掘频繁项集
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# 生成关联规则
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])"""
                    }
                ]
            },
            {
                "title": "第三章 规则评估与筛选",
                "sections": [
                    {
                        "subtitle": "3.1 规则评价指标",
                        "content": "除了支持度和置信度，还有其他重要指标：",
                        "code": """# 提升度 > 1 表示正相关
# 杠杆率 (Leverage): 衡量实际与期望频率的差异
leverage = support - P(A) * P(B)

# 确信度 (Conviction): 衡量规则的可靠性
conviction = (1 - P(B)) / (1 - confidence)"""
                    },
                    {
                        "subtitle": "3.2 规则筛选技巧",
                        "content": "如何从大量规则中筛选有价值的规则：",
                        "points": ["设置合理的最小支持度和置信度", "关注提升度大于1的规则", "优先选择简洁的规则", "结合业务知识筛选"],
                        "info": "💡 并非所有强规则都有实际业务价值，需要领域专家的参与。"
                    }
                ]
            },
            {
                "title": "第四章 实战案例",
                "sections": [
                    {
                        "subtitle": "4.1 案例分析",
                        "content": "分析超市购物篮数据，发现有趣的商品关联：",
                        "code": """# 加载真实购物篮数据
df = pd.read_csv('market_basket.csv')

# 数据预处理
df['Date'] = pd.to_datetime(df['Date'])
df['Revenue'] = df['Quantity'] * df['Price']

# 转换为交易格式
basket = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)"""
                    },
                    {
                        "subtitle": "4.2 结果解读",
                        "content": "解读关联规则挖掘结果，为业务决策提供支持：",
                        "points": ["识别捆绑销售机会", "优化商品摆放位置", "制定促销策略", "发现潜在的产品组合"]
                    }
                ]
            }
        ],
        "practice_tasks": [
            {
                "title": "练习 1：创建购物篮数据",
                "description": "创建一个包含5个交易记录的购物篮数据集，每个交易包含3-5个商品。",
                "template": """import pandas as pd

# 创建购物篮数据
data = {
    'Transaction': ['T1', 'T2', 'T3', 'T4', 'T5'],
    'Items': [['牛奶', '面包', '鸡蛋'],
              ['面包', '黄油'],
              ['牛奶', '面包', '黄油'],
              ['鸡蛋', '黄油'],
              ['牛奶', '鸡蛋']]
}

# 转换为适合Apriori的格式
# 请完成以下代码


print("转换后的购物篮数据:")
print(basket_df)"""
            },
            {
                "title": "练习 2：计算支持度",
                "description": "计算单个商品和商品组合的支持度。",
                "template": """import pandas as pd

data = {
    '牛奶': [1, 1, 0, 1, 0],
    '面包': [1, 0, 1, 1, 1],
    '鸡蛋': [0, 1, 1, 0, 1],
    '黄油': [1, 1, 0, 0, 0]
}
df = pd.DataFrame(data)

# 计算单个商品的支持度
item_support = df.mean()
print("单个商品支持度:")
print(item_support)

# 计算{牛奶,面包}的支持度
milk_bread_support = (df['牛奶'] & df['面包']).mean()
print("\\n{牛奶,面包}支持度:", milk_bread_support)"""
            },
            {
                "title": "练习 3：应用Apriori算法",
                "description": "使用mlxtend库挖掘频繁项集和关联规则。",
                "template": """import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 创建购物篮数据
data = {
    '牛奶': [1, 1, 0, 1, 0, 1],
    '面包': [1, 0, 1, 1, 1, 1],
    '鸡蛋': [0, 1, 1, 0, 1, 0],
    '黄油': [1, 1, 0, 0, 0, 1]
}
df = pd.DataFrame(data)

# 挖掘频繁项集（最小支持度0.4）
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
print("频繁项集:")
print(frequent_itemsets)

# 生成关联规则（最小置信度0.7）
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
print("\\n关联规则:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])"""
            },
            {
                "title": "练习 4：规则筛选",
                "description": "从关联规则中筛选出有价值的规则。",
                "template": """import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

data = {
    'A': [1, 1, 0, 1, 0, 1, 1, 0],
    'B': [1, 0, 1, 1, 1, 1, 0, 1],
    'C': [0, 1, 1, 0, 1, 0, 0, 1],
    'D': [1, 1, 0, 0, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)

# 筛选提升度大于1的规则
useful_rules = rules[rules['lift'] > 1]
print("有用的关联规则（提升度>1）:")
print(useful_rules[['antecedents', 'consequents', 'lift']])"""
            },
            {
                "title": "练习 5：完整购物篮分析",
                "description": "综合运用所学知识进行完整的购物篮分析。",
                "template": """import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 模拟真实购物篮数据
transactions = [
    ['苹果', '香蕉', '牛奶'],
    ['香蕉', '面包', '鸡蛋'],
    ['苹果', '香蕉', '面包'],
    ['牛奶', '面包', '鸡蛋'],
    ['苹果', '牛奶', '面包'],
    ['香蕉', '牛奶'],
    ['苹果', '香蕉', '牛奶', '面包'],
    ['面包', '鸡蛋']
]

# 转换为DataFrame格式
unique_items = sorted(set(item for transaction in transactions for item in transaction))
basket_data = []
for transaction in transactions:
    row = [1 if item in transaction else 0 for item in unique_items]
    basket_data.append(row)

df = pd.DataFrame(basket_data, columns=unique_items)

# 挖掘频繁项集
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
print("频繁项集:")
print(frequent_itemsets)

# 生成关联规则
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.6)
print("\\n关联规则:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])"""
            }
        ],
        "test_questions": [
            {"q": "关联规则中，支持度的计算公式是什么？", "options": ["P(A) * P(B)", "P(A ∩ B)", "P(B|A)", "P(A) + P(B)"], "answer": "B"},
            {"q": "Apriori算法的核心思想是什么？", "options": ["频繁项集的子集也是频繁的", "使用决策树进行分类", "基于神经网络的学习", "随机森林集成"], "answer": "A"},
            {"q": "提升度大于1表示什么？", "options": ["A和B负相关", "A和B无关联", "A和B正相关", "计算错误"], "answer": "C"},
            {"q": "以下哪个不是关联规则的评价指标？", "options": ["支持度", "置信度", "提升度", "准确率"], "answer": "D"},
            {"q": "购物篮分析最典型的应用场景是什么？", "options": ["图像识别", "商品推荐", "语音识别", "股票预测"], "answer": "B"}
        ],
        "homework": {
            "title": "购物篮分析作业",
            "tasks": ["1. 创建包含10个交易记录的购物篮数据集", "2. 使用Apriori算法挖掘频繁项集", "3. 生成关联规则并筛选提升度大于1的规则", "4. 分析结果并给出业务建议"],
            "template": """import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 1. 创建购物篮数据（至少10条交易）


# 2. 挖掘频繁项集


# 3. 生成关联规则并筛选


# 4. 输出分析结果和业务建议"""
        }
    },
    {
        "id": "project4",
        "title": "客户聚类分析",
        "icon": "👥",
        "description": "使用K-Means算法对客户进行分群，理解客户行为特征，为精准营销提供支持。",
        "difficulty": "badge-medium",
        "difficulty_label": "进阶",
        "dataset": "customer_features.csv",
        "chapters": [
            {
                "title": "第一章 聚类分析基础",
                "sections": [
                    {
                        "subtitle": "1.1 什么是聚类分析",
                        "content": "聚类分析是一种无监督学习方法，它将数据集中的对象分组，使得同一组内的对象相似度较高，而不同组间的对象相似度较低。",
                        "points": ["无监督学习", "相似度度量", "簇的定义", "聚类算法分类"],
                        "info": "💡 聚类分析广泛应用于客户细分、市场定位、图像分割等领域。"
                    },
                    {
                        "subtitle": "1.2 常用距离度量",
                        "content": "距离度量是聚类的基础，常用的距离包括：",
                        "code": """# 欧氏距离
distance = sqrt(sum((x_i - y_i)^2))

# 曼哈顿距离
distance = sum(|x_i - y_i|)

# 余弦相似度
similarity = (x · y) / (||x|| * ||y||)"""
                    }
                ]
            },
            {
                "title": "第二章 K-Means算法",
                "sections": [
                    {
                        "subtitle": "2.1 K-Means原理",
                        "content": "K-Means是最常用的聚类算法之一，其目标是将n个对象划分为k个簇，使得每个簇内的对象到簇中心的距离最小。",
                        "points": ["随机初始化k个簇中心", "计算每个点到各中心的距离", "将点分配到最近的簇", "更新簇中心为簇内点的均值", "迭代直到收敛"],
                        "tip": "📌 K-Means对初始簇中心的选择很敏感，通常需要多次运行取最优结果。"
                    },
                    {
                        "subtitle": "2.2 Python实现K-Means",
                        "content": "使用scikit-learn实现K-Means聚类：",
                        "code": """import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# 创建客户数据
data = {
    'Age': [25, 32, 45, 28, 35, 42, 29, 38],
    'Income': [45000, 67000, 89000, 52000, 78000, 95000, 58000, 72000],
    'SpendingScore': [61, 78, 85, 55, 72, 90, 65, 82]
}
df = pd.DataFrame(data)

# 应用K-Means聚类
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Age', 'Income', 'SpendingScore']])

print("聚类结果:")
print(df)
print("\\n簇中心:")
print(pd.DataFrame(kmeans.cluster_centers_, columns=['Age', 'Income', 'SpendingScore']))"""
                    }
                ]
            },
            {
                "title": "第三章 确定最佳K值",
                "sections": [
                    {
                        "subtitle": "3.1 肘部法则",
                        "content": "肘部法则是确定最佳K值的常用方法：",
                        "code": """import matplotlib.pyplot as plt

# 计算不同K值的惯性
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df[['Age', 'Income', 'SpendingScore']])
    inertia.append(kmeans.inertia_)

# 绘制肘部曲线
plt.plot(range(1, 11), inertia, 'bo-')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()"""
                    },
                    {
                        "subtitle": "3.2 轮廓系数",
                        "content": "轮廓系数是另一种评估聚类质量的指标：",
                        "code": """from sklearn.metrics import silhouette_score

# 计算轮廓系数
sil_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(df[['Age', 'Income', 'SpendingScore']])
    sil_score = silhouette_score(df[['Age', 'Income', 'SpendingScore']], labels)
    sil_scores.append(sil_score)

print("各K值的轮廓系数:")
for k, score in zip(range(2, 11), sil_scores):
    print(f"K={k}: {score:.3f}")"""
                    }
                ]
            },
            {
                "title": "第四章 客户细分实战",
                "sections": [
                    {
                        "subtitle": "4.1 数据预处理",
                        "content": "对客户数据进行标准化处理：",
                        "code": """from sklearn.preprocessing import StandardScaler

# 数据标准化
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Age', 'Income', 'SpendingScore']])

# 应用K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)"""
                    },
                    {
                        "subtitle": "4.2 结果分析",
                        "content": "分析各个客户群体的特征：",
                        "points": ["高收入高消费群体", "高收入低消费群体", "低收入高消费群体", "低收入低消费群体"],
                        "info": "💡 通过聚类分析，企业可以针对不同客户群体制定差异化的营销策略。"
                    }
                ]
            }
        ],
        "practice_tasks": [
            {
                "title": "练习 1：创建客户数据",
                "description": "创建一个包含客户特征的数据集。",
                "template": """import pandas as pd

# 创建客户数据
data = {
    'CustomerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C006'],
    'Age': [28, 35, 42, 25, 48, 31],
    'AnnualIncome': [55000, 78000, 92000, 42000, 110000, 65000],
    'SpendingScore': [72, 85, 68, 45, 90, 58]
}

df = pd.DataFrame(data)
print("客户数据:")
print(df)"""
            },
            {
                "title": "练习 2：应用K-Means",
                "description": "使用K-Means对客户数据进行聚类。",
                "template": """import pandas as pd
from sklearn.cluster import KMeans

data = {
    'Age': [28, 35, 42, 25, 48, 31, 38, 29],
    'Income': [55000, 78000, 92000, 42000, 110000, 65000, 82000, 52000],
    'Score': [72, 85, 68, 45, 90, 58, 78, 62]
}
df = pd.DataFrame(data)

# 使用K-Means进行聚类（K=3）
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Age', 'Income', 'Score']])

print("聚类结果:")
print(df)"""
            },
            {
                "title": "练习 3：肘部法则",
                "description": "使用肘部法则确定最佳K值。",
                "template": """import pandas as pd
from sklearn.cluster import KMeans

data = {
    'Feature1': [1, 2, 8, 9, 2, 3, 7, 8],
    'Feature2': [1, 2, 8, 9, 8, 9, 1, 2]
}
df = pd.DataFrame(data)

# 计算不同K值的惯性
inertia = []
for k in range(1, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df)
    inertia.append(kmeans.inertia_)

print("K值 vs 惯性:")
for k, iner in zip(range(1, 7), inertia):
    print(f"K={k}: {iner:.2f}")

# 根据肘部法则，最佳K值是多少？"""
            },
            {
                "title": "练习 4：数据标准化",
                "description": "对数据进行标准化后再聚类。",
                "template": """import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'Age': [28, 35, 42, 25, 48],
    'Income': [55000, 78000, 92000, 42000, 110000],
    'Score': [72, 85, 68, 45, 90]
}
df = pd.DataFrame(data)

# 数据标准化
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

# 应用K-Means
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(scaled_features)

print("标准化后的数据:")
print(pd.DataFrame(scaled_features, columns=['Age', 'Income', 'Score']))
print("\\n聚类标签:", clusters)"""
            },
            {
                "title": "练习 5：客户细分分析",
                "description": "综合运用K-Means进行客户细分。",
                "template": """import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 模拟客户数据
data = {
    'Age': [25, 32, 45, 28, 35, 42, 29, 38, 48, 31],
    'Income': [45000, 67000, 89000, 52000, 78000, 95000, 58000, 72000, 110000, 62000],
    'SpendingScore': [61, 78, 85, 55, 72, 90, 65, 82, 88, 58]
}
df = pd.DataFrame(data)

# 标准化数据
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# 使用K-Means聚类（假设K=4）
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# 分析各簇特征
print("各簇统计信息:")
print(df.groupby('Cluster').mean())"""
            }
        ],
        "test_questions": [
            {"q": "K-Means算法的目标是什么？", "options": ["最小化簇内距离", "最大化簇间距离", "最小化分类误差", "最大化信息增益"], "answer": "A"},
            {"q": "确定K-Means最佳K值的常用方法是什么？", "options": ["肘部法则", "交叉验证", "网格搜索", "特征选择"], "answer": "A"},
            {"q": "K-Means属于哪种学习类型？", "options": ["监督学习", "无监督学习", "强化学习", "半监督学习"], "answer": "B"},
            {"q": "K-Means对初始簇中心敏感，通常如何解决？", "options": ["使用固定种子", "多次运行取最优", "增加数据量", "减少特征数"], "answer": "B"},
            {"q": "聚类分析在客户关系管理中的主要应用是什么？", "options": ["客户细分", "客户流失预测", "客户满意度分析", "客户价值评估"], "answer": "A"}
        ],
        "homework": {
            "title": "客户聚类分析作业",
            "tasks": ["1. 创建包含20个客户的数据集", "2. 对数据进行标准化处理", "3. 使用肘部法则确定最佳K值", "4. 应用K-Means聚类并分析各簇特征"],
            "template": """import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. 创建客户数据集


# 2. 数据标准化


# 3. 使用肘部法则确定最佳K值


# 4. 应用K-Means并分析"""
        }
    },
    {
        "id": "project5",
        "title": "数据可视化",
        "icon": "📊",
        "description": "掌握Matplotlib和Seaborn库，创建专业的数据可视化图表，有效传达数据洞察。",
        "difficulty": "badge-easy",
        "difficulty_label": "入门",
        "dataset": "sales_data.csv",
        "chapters": [
            {
                "title": "第一章 Matplotlib基础",
                "sections": [
                    {
                        "subtitle": "1.1 基本图表类型",
                        "content": "Matplotlib是Python最常用的数据可视化库，支持多种图表类型：",
                        "code": """import matplotlib.pyplot as plt
import numpy as np

# 折线图
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('折线图示例')
plt.legend()
plt.show()"""
                    },
                    {
                        "subtitle": "1.2 柱状图与直方图",
                        "content": "柱状图用于比较类别数据，直方图用于展示数据分布：",
                        "code": """# 柱状图
categories = ['A', 'B', 'C', 'D']
values = [30, 45, 25, 50]
plt.bar(categories, values, color='skyblue')
plt.title('柱状图')
plt.show()

# 直方图
data = np.random.randn(1000)
plt.hist(data, bins=30, alpha=0.7, color='orange')
plt.title('直方图')
plt.show()"""
                    }
                ]
            },
            {
                "title": "第二章 Seaborn高级可视化",
                "sections": [
                    {
                        "subtitle": "2.1 统计图表",
                        "content": "Seaborn提供了更高级的统计可视化功能：",
                        "code": """import seaborn as sns
import pandas as pd

# 创建数据
data = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 15, 8, 12, 14, 9]
})

# 箱线图
sns.boxplot(x='Category', y='Value', data=data)
plt.title('箱线图')
plt.show()

# 散点图带回归线
sns.regplot(x='Category', y='Value', data=data)
plt.title('散点图')
plt.show()"""
                    },
                    {
                        "subtitle": "2.2 热力图",
                        "content": "热力图用于展示数据矩阵的相关性：",
                        "code": """# 创建相关矩阵
corr_matrix = data.corr()

# 热力图
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('相关性热力图')
plt.show()"""
                    }
                ]
            },
            {
                "title": "第三章 图表美化",
                "sections": [
                    {
                        "subtitle": "3.1 样式设置",
                        "content": "自定义图表样式：",
                        "code": """# 设置样式
plt.style.use('seaborn-v0_8-darkgrid')

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建更美观的图表
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, color='#00d4ff', linewidth=2, linestyle='--')
ax.set_title('美化后的图表', fontsize=16)
ax.set_xlabel('X轴', fontsize=14)
ax.set_ylabel('Y轴', fontsize=14)
plt.show()"""
                    },
                    {
                        "subtitle": "3.2 子图布局",
                        "content": "创建多子图布局：",
                        "code": """fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('子图1')

axes[0, 1].bar(categories, values)
axes[0, 1].set_title('子图2')

axes[1, 0].hist(data, bins=20)
axes[1, 0].set_title('子图3')

axes[1, 1].scatter(np.random.rand(50), np.random.rand(50))
axes[1, 1].set_title('子图4')

plt.tight_layout()
plt.show()"""
                    }
                ]
            },
            {
                "title": "第四章 实战案例",
                "sections": [
                    {
                        "subtitle": "4.1 销售数据分析可视化",
                        "content": "综合运用所学知识进行销售数据可视化：",
                        "code": """# 加载销售数据
sales_data = pd.read_csv('sales_data.csv')

# 月度销售趋势
monthly_sales = sales_data.groupby('Month')['Revenue'].sum()

# 创建仪表盘式布局
fig = plt.figure(figsize=(14, 10))

# 主图：销售趋势
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(monthly_sales.index, monthly_sales.values, marker='o')
ax1.set_title('月度销售趋势')

# 产品分类销售
ax2 = fig.add_subplot(2, 2, 2)
category_sales = sales_data.groupby('Category')['Revenue'].sum()
ax2.pie(category_sales.values, labels=category_sales.index, autopct='%1.1f%%')
ax2.set_title('产品分类销售占比')

plt.show()"""
                    }
                ]
            }
        ],
        "practice_tasks": [
            {
                "title": "练习 1：绘制折线图",
                "description": "使用Matplotlib绘制简单的折线图。",
                "template": """import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.arange(1, 11)
y = x ** 2  # y = x²

# 绘制折线图
plt.plot(x, y, color='blue', marker='o', linestyle='-')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('y = x²')
plt.grid(True)
plt.show()"""
            },
            {
                "title": "练习 2：绘制柱状图",
                "description": "绘制不同类别的对比柱状图。",
                "template": """import matplotlib.pyplot as plt

# 数据
categories = ['产品A', '产品B', '产品C', '产品D']
sales_2022 = [150, 200, 180, 220]
sales_2023 = [180, 220, 200, 250]

# 绘制分组柱状图
x = range(len(categories))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar([i - width/2 for i in x], sales_2022, width, label='2022年')
rects2 = ax.bar([i + width/2 for i in x], sales_2023, width, label='2023年')

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

plt.title('产品销售对比')
plt.show()"""
            },
            {
                "title": "练习 3：Seaborn箱线图",
                "description": "使用Seaborn绘制箱线图展示数据分布。",
                "template": """import seaborn as sns
import pandas as pd

# 创建数据
data = pd.DataFrame({
    'Group': ['A']*10 + ['B']*10 + ['C']*10,
    'Value': [1,2,3,4,5,6,7,8,9,10,
              2,3,4,5,6,7,8,9,10,11,
              3,4,5,6,7,8,9,10,11,12]
})

# 绘制箱线图
sns.boxplot(x='Group', y='Value', data=data, palette='Set2')
plt.title('三组数据分布对比')
plt.show()"""
            },
            {
                "title": "练习 4：热力图",
                "description": "绘制相关性热力图。",
                "template": """import seaborn as sns
import pandas as pd
import numpy as np

# 创建相关矩阵
np.random.seed(42)
data = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.rand(100),
    'C': np.random.rand(100),
    'D': np.random.rand(100)
})

# 计算相关系数
corr = data.corr()

# 绘制热力图
sns.heatmap(corr, annot=True, cmap='coolwarm', 
            vmin=-1, vmax=1, center=0)
plt.title('变量相关性热力图')
plt.show()"""
            },
            {
                "title": "练习 5：综合可视化",
                "description": "创建包含多个子图的仪表板式布局。",
                "template": """import matplotlib.pyplot as plt
import numpy as np

# 创建数据
months = ['1月', '2月', '3月', '4月', '5月', '6月']
sales = [120, 150, 180, 160, 200, 220]
profit = [20, 25, 30, 28, 35, 40]

# 创建子图布局
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 子图1：销售趋势
axes[0].plot(months, sales, marker='s', color='green')
axes[0].set_title('销售趋势')

# 子图2：利润趋势
axes[1].bar(months, profit, color='orange')
axes[1].set_title('利润趋势')

# 子图3：销售利润对比
axes[2].scatter(sales, profit, color='purple', s=100)
axes[2].set_xlabel('销售额')
axes[2].set_ylabel('利润')
axes[2].set_title('销售利润关系')

plt.tight_layout()
plt.show()"""
            }
        ],
        "test_questions": [
            {"q": "Matplotlib中绘制折线图的函数是？", "options": ["plt.bar()", "plt.plot()", "plt.hist()", "plt.scatter()"], "answer": "B"},
            {"q": "Seaborn是基于哪个库开发的？", "options": ["Plotly", "Matplotlib", "ggplot", "Bokeh"], "answer": "B"},
            {"q": "用于展示数据矩阵相关性的图表是？", "options": ["折线图", "柱状图", "热力图", "散点图"], "answer": "C"},
            {"q": "设置图表标题的方法是？", "options": ["plt.xlabel()", "plt.ylabel()", "plt.title()", "plt.legend()"], "answer": "C"},
            {"q": "创建多个子图应该使用？", "options": ["plt.figure()", "plt.subplots()", "plt.show()", "plt.savefig()"], "answer": "B"}
        ],
        "homework": {
            "title": "数据可视化作业",
            "tasks": ["1. 创建模拟销售数据集", "2. 绘制销售趋势折线图", "3. 绘制产品分类饼图", "4. 创建仪表板式布局展示多个图表"],
            "template": """import matplotlib.pyplot as plt
import pandas as pd

# 1. 创建销售数据


# 2. 绘制销售趋势图


# 3. 绘制分类占比饼图


# 4. 创建仪表板布局"""
        }
    },
    {
        "id": "project6",
        "title": "A/B测试分析",
        "icon": "🧪",
        "description": "学习假设检验方法，掌握A/B测试的设计与分析流程，为业务决策提供数据支持。",
        "difficulty": "badge-medium",
        "difficulty_label": "进阶",
        "dataset": "ab_test_data.csv",
        "chapters": [
            {
                "title": "第一章 假设检验基础",
                "sections": [
                    {
                        "subtitle": "1.1 假设检验概念",
                        "content": "假设检验是统计推断的核心方法，用于判断样本数据是否支持某个假设。",
                        "points": ["原假设 (H₀)", "备择假设 (H₁)", "显著性水平 (α)", "p值", "第一类错误与第二类错误"],
                        "info": "💡 A/B测试是假设检验在业务决策中的典型应用。"
                    },
                    {
                        "subtitle": "1.2 常用假设检验类型",
                        "content": "根据数据类型选择合适的检验方法：",
                        "code": """# Z检验 - 大样本均值检验
from scipy import stats

# 单样本Z检验
z_score = (sample_mean - pop_mean) / (pop_std / sqrt(n))

# 双样本Z检验（比例检验）
p1, p2 = 0.15, 0.18
n1, n2 = 1000, 1000
p_pooled = (p1*n1 + p2*n2) / (n1 + n2)
z_score = (p1 - p2) / sqrt(p_pooled * (1-p_pooled) * (1/n1 + 1/n2))"""
                    }
                ]
            },
            {
                "title": "第二章 A/B测试设计",
                "sections": [
                    {
                        "subtitle": "2.1 A/B测试流程",
                        "content": "完整的A/B测试流程包括：",
                        "points": ["确定测试目标", "假设设定", "样本量计算", "随机分组", "数据收集", "结果分析"],
                        "tip": "📌 样本量计算是A/B测试设计的关键，直接影响测试的统计功效。"
                    },
                    {
                        "subtitle": "2.2 样本量计算",
                        "content": "计算所需的最小样本量：",
                        "code": """import math
from scipy.stats import norm

# 参数设置
baseline = 0.10  # 基准转化率
min_effect = 0.02  # 最小可检测效果
alpha = 0.05  # 显著性水平
power = 0.80  # 统计功效

# 计算样本量
z_alpha = norm.ppf(1 - alpha/2)
z_beta = norm.ppf(power)

p1 = baseline
p2 = baseline + min_effect
p_avg = (p1 + p2) / 2

n = (z_alpha * math.sqrt(2 * p_avg * (1-p_avg)) + 
     z_beta * math.sqrt(p1*(1-p1) + p2*(1-p2)))**2 / min_effect**2

print(f"每组所需样本量: {math.ceil(n)}")"""
                    }
                ]
            },
            {
                "title": "第三章 A/B测试分析",
                "sections": [
                    {
                        "subtitle": "3.1 比例检验",
                        "content": "比较两组转化率差异：",
                        "code": """import pandas as pd
from scipy.stats import chi2_contingency

# 创建列联表
data = [[150, 850],  # 实验组：转化数, 未转化数
        [120, 880]]  # 对照组：转化数, 未转化数

# 卡方检验
chi2, p_value, dof, expected = chi2_contingency(data)
print(f"卡方值: {chi2:.4f}")
print(f"p值: {p_value:.4f}")

# 判断结果
alpha = 0.05
if p_value < alpha:
    print("拒绝原假设：两组转化率存在显著差异")
else:
    print("不拒绝原假设：两组转化率无显著差异")"""
                    },
                    {
                        "subtitle": "3.2 均值检验",
                        "content": "比较两组均值差异：",
                        "code": """from scipy.stats import ttest_ind

# 模拟数据
group_a = [45, 52, 48, 55, 50, 49, 53, 47, 51, 54]
group_b = [48, 55, 52, 58, 53, 51, 56, 50, 54, 57]

# 独立样本t检验
t_stat, p_value = ttest_ind(group_a, group_b)
print(f"t统计量: {t_stat:.4f}")
print(f"p值: {p_value:.4f}")"""
                    }
                ]
            },
            {
                "title": "第四章 实战案例",
                "sections": [
                    {
                        "subtitle": "4.1 网页优化测试",
                        "content": "分析网页改版对转化率的影响：",
                        "code": """# 加载A/B测试数据
ab_data = pd.read_csv('ab_test_data.csv')

# 计算各组转化率
conversion_a = ab_data[ab_data['group'] == 'A']['converted'].mean()
conversion_b = ab_data[ab_data['group'] == 'B']['converted'].mean()

print(f"对照组转化率: {conversion_a:.4%}")
print(f"实验组转化率: {conversion_b:.4%}")
print(f"提升幅度: {(conversion_b-conversion_a)/conversion_a:.2%}")

# 进行卡方检验
table = pd.crosstab(ab_data['group'], ab_data['converted'])
chi2, p_value, _, _ = chi2_contingency(table)
print(f"\\n卡方检验p值: {p_value:.4f}")"""
                    }
                ]
            }
        ],
        "practice_tasks": [
            {
                "title": "练习 1：假设检验基础",
                "description": "理解假设检验的基本概念并进行简单计算。",
                "template": """import math
from scipy.stats import norm

# 计算Z分数
sample_mean = 52
pop_mean = 50
pop_std = 10
n = 25

z_score = (sample_mean - pop_mean) / (pop_std / math.sqrt(n))
print(f"Z分数: {z_score:.2f}")

# 计算p值
p_value = 2 * (1 - norm.cdf(z_score))
print(f"双尾p值: {p_value:.4f}")

# 判断是否拒绝原假设
alpha = 0.05
if p_value < alpha:
    print("拒绝原假设")
else:
    print("不拒绝原假设")"""
            },
            {
                "title": "练习 2：样本量计算",
                "description": "计算A/B测试所需的最小样本量。",
                "template": """import math
from scipy.stats import norm

# 参数
baseline = 0.15  # 基准转化率
min_effect = 0.03  # 最小可检测效果
alpha = 0.05
power = 0.8

# 计算Z值
z_alpha = norm.ppf(1 - alpha/2)
z_beta = norm.ppf(power)

# 计算样本量
p1 = baseline
p2 = baseline + min_effect
p_avg = (p1 + p2) / 2

n = (z_alpha * math.sqrt(2 * p_avg * (1-p_avg)) + 
     z_beta * math.sqrt(p1*(1-p1) + p2*(1-p2)))**2 / min_effect**2

print(f"每组所需样本量: {math.ceil(n)}")"""
            },
            {
                "title": "练习 3：卡方检验",
                "description": "使用卡方检验比较两组转化率。",
                "template": """from scipy.stats import chi2_contingency

# A/B测试数据
# 行: 实验组/对照组, 列: 转化/未转化
data = [[180, 820],  # 实验组
        [150, 850]]  # 对照组

# 卡方检验
chi2, p_value, dof, expected = chi2_contingency(data)
print(f"卡方值: {chi2:.4f}")
print(f"p值: {p_value:.4f}")

# 计算转化率
conv_a = 180 / (180 + 820)
conv_b = 150 / (150 + 850)
print(f"\\n实验组转化率: {conv_a:.2%}")
print(f"对照组转化率: {conv_b:.2%}")"""
            },
            {
                "title": "练习 4：t检验",
                "description": "使用t检验比较两组均值。",
                "template": """from scipy.stats import ttest_ind
import numpy as np

# 模拟两组数据
np.random.seed(42)
group_a = np.random.normal(100, 15, 50)
group_b = np.random.normal(105, 15, 50)

# 独立样本t检验
t_stat, p_value = ttest_ind(group_a, group_b)
print(f"t统计量: {t_stat:.4f}")
print(f"p值: {p_value:.4f}")

# 计算均值
print(f"\\nA组均值: {group_a.mean():.2f}")
print(f"B组均值: {group_b.mean():.2f}")"""
            },
            {
                "title": "练习 5：完整A/B测试分析",
                "description": "综合分析A/B测试结果。",
                "template": """import pandas as pd
from scipy.stats import chi2_contingency

# 创建模拟A/B测试数据
data = pd.DataFrame({
    'group': ['A']*1000 + ['B']*1000,
    'converted': [1]*120 + [0]*880 + [1]*150 + [0]*850
})

# 计算转化率
conv_a = data[data['group']=='A']['converted'].mean()
conv_b = data[data['group']=='B']['converted'].mean()

print(f"A组转化率: {conv_a:.2%}")
print(f"B组转化率: {conv_b:.2%}")
print(f"提升: {(conv_b-conv_a)/conv_a:.2%}")

# 卡方检验
table = pd.crosstab(data['group'], data['converted'])
chi2, p_value, _, _ = chi2_contingency(table)
print(f"\\n卡方检验p值: {p_value:.4f}")

# 结论
alpha = 0.05
if p_value < alpha:
    print("结论：B组显著优于A组")
else:
    print("结论：两组无显著差异")"""
            }
        ],
        "test_questions": [
            {"q": "A/B测试中，原假设通常是什么？", "options": ["两组有差异", "两组无差异", "实验组更好", "对照组更好"], "answer": "B"},
            {"q": "p值小于0.05意味着什么？", "options": ["接受原假设", "拒绝原假设", "无法判断", "计算错误"], "answer": "B"},
            {"q": "计算样本量需要哪些参数？", "options": ["基准率、最小效果、显著性水平、功效", "仅样本数量", "仅转化率", "仅效果大小"], "answer": "A"},
            {"q": "比较两组转化率应该使用什么检验？", "options": ["t检验", "卡方检验", "Z检验", "F检验"], "answer": "B"},
            {"q": "统计功效(power)通常设置为多少？", "options": ["0.5", "0.8", "0.95", "0.99"], "answer": "B"}
        ],
        "homework": {
            "title": "A/B测试分析作业",
            "tasks": ["1. 设计一个A/B测试方案", "2. 计算所需样本量", "3. 模拟测试数据", "4. 进行假设检验并得出结论"],
            "template": """import pandas as pd
from scipy.stats import chi2_contingency

# 1. 定义测试参数


# 2. 计算样本量


# 3. 模拟测试数据


# 4. 进行假设检验"""
        }
    },
    {
        "id": "project7",
        "title": "时间序列分析",
        "icon": "⏰",
        "description": "学习时间序列数据的处理方法，掌握趋势分析和预测技术。",
        "difficulty": "badge-hard",
        "difficulty_label": "高级",
        "dataset": "time_series_data.csv",
        "chapters": [
            {
                "title": "第一章 时间序列基础",
                "sections": [
                    {
                        "subtitle": "1.1 时间序列概念",
                        "content": "时间序列是按时间顺序排列的数据序列，广泛应用于金融、销售、气象等领域。",
                        "points": ["趋势 (Trend)", "季节性 (Seasonality)", "周期性 (Cycle)", "噪声 (Noise)"],
                        "info": "💡 时间序列分析的核心是识别模式并进行预测。"
                    },
                    {
                        "subtitle": "1.2 Pandas时间处理",
                        "content": "使用Pandas处理时间序列数据：",
                        "code": """import pandas as pd

# 创建时间序列数据
dates = pd.date_range('2023-01-01', periods=365, freq='D')
data = pd.DataFrame({
    'date': dates,
    'value': [100 + i*0.5 + pd.np.sin(i*0.1)*10 for i in range(365)]
})

# 设置日期索引
data.set_index('date', inplace=True)

# 查看月度数据
monthly_data = data.resample('M').mean()
print(monthly_data.head())"""
                    }
                ]
            },
            {
                "title": "第二章 趋势分析",
                "sections": [
                    {
                        "subtitle": "2.1 移动平均",
                        "content": "使用移动平均平滑数据并识别趋势：",
                        "code": """# 计算7日移动平均
data['MA7'] = data['value'].rolling(window=7).mean()

# 计算30日移动平均
data['MA30'] = data['value'].rolling(window=30).mean()

# 可视化
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(data['value'], label='原始数据')
plt.plot(data['MA7'], label='7日MA')
plt.plot(data['MA30'], label='30日MA')
plt.legend()
plt.show()"""
                    },
                    {
                        "subtitle": "2.2 指数平滑",
                        "content": "指数平滑给近期数据更高的权重：",
                        "code": """# 简单指数平滑
data['EWMA'] = data['value'].ewm(alpha=0.1).mean()

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(data['value'], label='原始数据', alpha=0.5)
plt.plot(data['EWMA'], label='指数平滑')
plt.legend()
plt.show()"""
                    }
                ]
            },
            {
                "title": "第三章 ARIMA模型",
                "sections": [
                    {
                        "subtitle": "3.1 ARIMA介绍",
                        "content": "ARIMA是常用的时间序列预测模型：",
                        "points": ["AR (自回归)", "I (差分)", "MA (移动平均)"],
                        "tip": "📌 ARIMA模型需要确定p、d、q三个参数。"
                    },
                    {
                        "subtitle": "3.2 使用ARIMA预测",
                        "content": "使用statsmodels实现ARIMA：",
                        "code": """from statsmodels.tsa.arima.model import ARIMA

# 创建模型
model = ARIMA(data['value'], order=(5, 1, 0))
result = model.fit()

# 预测
forecast = result.get_forecast(steps=30)
forecast_df = forecast.summary_frame()

print("预测结果:")
print(forecast_df[['mean', 'mean_lower', 'mean_upper']].head())"""
                    }
                ]
            },
            {
                "title": "第四章 实战案例",
                "sections": [
                    {
                        "subtitle": "4.1 销售预测",
                        "content": "预测未来销售趋势：",
                        "code": """# 加载销售数据
sales_data = pd.read_csv('sales_data.csv', parse_dates=['date'], index_col='date')

# 训练ARIMA模型
model = ARIMA(sales_data['revenue'], order=(2, 1, 1))
result = model.fit()

# 预测未来3个月
forecast = result.get_forecast(steps=90)

# 可视化结果
plt.figure(figsize=(12, 6))
plt.plot(sales_data['revenue'], label='历史数据')
plt.plot(forecast.predicted_mean, label='预测值', color='red')
plt.fill_between(forecast.predicted_mean.index,
                 forecast.conf_int()['lower revenue'],
                 forecast.conf_int()['upper revenue'],
                 color='pink', alpha=0.3)
plt.legend()
plt.show()"""
                    }
                ]
            }
        ],
        "practice_tasks": [
            {
                "title": "练习 1：创建时间序列",
                "description": "使用Pandas创建时间序列数据。",
                "template": """import pandas as pd
import numpy as np

# 创建时间序列数据
dates = pd.date_range('2023-01-01', periods=100, freq='D')
values = np.random.randn(100).cumsum() + 100

ts = pd.Series(values, index=dates)
print("时间序列数据:")
print(ts.head())

# 绘制时间序列
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
ts.plot()
plt.title('时间序列示例')
plt.show()"""
            },
            {
                "title": "练习 2：移动平均",
                "description": "计算并可视化移动平均。",
                "template": """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
dates = pd.date_range('2023-01-01', periods=100, freq='D')
values = 100 + np.arange(100)*0.5 + np.sin(np.arange(100)*0.2)*10
ts = pd.Series(values, index=dates)

# 计算移动平均
ts_ma5 = ts.rolling(window=5).mean()
ts_ma10 = ts.rolling(window=10).mean()

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(ts, label='原始数据', alpha=0.5)
plt.plot(ts_ma5, label='5日MA')
plt.plot(ts_ma10, label='10日MA')
plt.legend()
plt.show()"""
            },
            {
                "title": "练习 3：指数平滑",
                "description": "应用指数平滑技术。",
                "template": """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
dates = pd.date_range('2023-01-01', periods=100, freq='D')
values = 100 + np.random.randn(100).cumsum()
ts = pd.Series(values, index=dates)

# 指数平滑
ts_ewma = ts.ewm(alpha=0.2).mean()

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(ts, label='原始数据', alpha=0.5)
plt.plot(ts_ewma, label='EWMA (α=0.2)')
plt.legend()
plt.show()"""
            },
            {
                "title": "练习 4：数据重采样",
                "description": "对时间序列进行不同频率的重采样。",
                "template": """import pandas as pd
import numpy as np

# 创建日数据
dates = pd.date_range('2023-01-01', periods=365, freq='D')
values = 100 + np.random.randn(365).cumsum()
ts = pd.Series(values, index=dates)

# 转换为周数据
weekly = ts.resample('W').mean()
print("周数据:")
print(weekly.head())

# 转换为月数据
monthly = ts.resample('M').sum()
print("\\n月数据:")
print(monthly)"""
            },
            {
                "title": "练习 5：时间序列预测",
                "description": "使用ARIMA进行简单预测。",
                "template": """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 创建模拟数据
dates = pd.date_range('2023-01-01', periods=200, freq='D')
values = 100 + np.arange(200)*0.3 + np.sin(np.arange(200)*0.1)*5 + np.random.randn(200)*2
ts = pd.Series(values, index=dates)

# 拟合ARIMA模型
model = ARIMA(ts, order=(2, 1, 1))
result = model.fit()

# 预测未来14天
forecast = result.get_forecast(steps=14)

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(ts, label='历史数据')
plt.plot(forecast.predicted_mean, label='预测值', color='red')
plt.fill_between(forecast.predicted_mean.index,
                 forecast.conf_int()['lower predicted_mean'],
                 forecast.conf_int()['upper predicted_mean'],
                 color='pink', alpha=0.3)
plt.legend()
plt.show()"""
            }
        ],
        "test_questions": [
            {"q": "时间序列数据的四个组成部分不包括？", "options": ["趋势", "季节性", "周期性", "相关性"], "answer": "D"},
            {"q": "移动平均的主要作用是什么？", "options": ["增加数据噪声", "平滑数据、识别趋势", "预测未来值", "计算标准差"], "answer": "B"},
            {"q": "ARIMA模型中的I代表什么？", "options": ["自回归", "差分", "移动平均", "积分"], "answer": "B"},
            {"q": "指数平滑与简单移动平均的区别是？", "options": ["计算更简单", "给近期数据更高权重", "只使用过去3个数据点", "不需要参数"], "answer": "B"},
            {"q": "Pandas中设置日期索引的方法是？", "options": ["set_index()", "to_datetime()", "resample()", "rolling()"], "answer": "A"}
        ],
        "homework": {
            "title": "时间序列分析作业",
            "tasks": ["1. 创建包含趋势和季节性的时间序列数据", "2. 计算移动平均和指数平滑", "3. 使用ARIMA模型进行预测", "4. 可视化展示分析结果"],
            "template": """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 1. 创建时间序列数据


# 2. 计算移动平均和指数平滑


# 3. ARIMA预测


# 4. 可视化"""
        }
    },
    {
        "id": "project8",
        "title": "特征工程",
        "icon": "🔧",
        "description": "学习特征提取、转换和编码技术，构建高质量的特征用于机器学习模型。",
        "difficulty": "badge-medium",
        "difficulty_label": "进阶",
        "dataset": "customer_data.csv",
        "chapters": [
            {
                "title": "第一章 特征工程概述",
                "sections": [
                    {
                        "subtitle": "1.1 什么是特征工程",
                        "content": "特征工程是将原始数据转换为机器学习模型可用特征的过程，是机器学习成功的关键。",
                        "points": ["特征提取", "特征转换", "特征选择", "特征编码"],
                        "info": "💡 好的特征比好的模型更重要。"
                    },
                    {
                        "subtitle": "1.2 数据类型与处理",
                        "content": "不同类型的数据需要不同的处理方法：",
                        "code": """import pandas as pd

# 数值型特征
numeric_features = ['age', 'income', 'score']

# 类别型特征
categorical_features = ['gender', 'education', 'occupation']

# 文本特征
text_features = ['description', 'review']"""
                    }
                ]
            },
            {
                "title": "第二章 类别特征编码",
                "sections": [
                    {
                        "subtitle": "2.1 独热编码",
                        "content": "将类别特征转换为二进制向量：",
                        "code": """import pandas as pd

data = pd.DataFrame({
    'color': ['红', '蓝', '绿', '红', '蓝'],
    'size': ['S', 'M', 'L', 'M', 'S']
})

# 独热编码
one_hot = pd.get_dummies(data, columns=['color', 'size'])
print(one_hot)"""
                    },
                    {
                        "subtitle": "2.2 标签编码与目标编码",
                        "content": "处理有序类别和高基数类别：",
                        "code": """from sklearn.preprocessing import LabelEncoder

# 标签编码（适合有序类别）
le = LabelEncoder()
data['size_code'] = le.fit_transform(data['size'])

# 目标编码（适合高基数类别）
target_mean = data.groupby('color')['target'].mean()
data['color_target_enc'] = data['color'].map(target_mean)"""
                    }
                ]
            },
            {
                "title": "第三章 特征提取",
                "sections": [
                    {
                        "subtitle": "3.1 数值特征处理",
                        "content": "处理数值特征：",
                        "code": """from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 标准化
scaler = StandardScaler()
data[['age', 'income']] = scaler.fit_transform(data[['age', 'income']])

# 归一化
minmax = MinMaxScaler()
data['score'] = minmax.fit_transform(data[['score']])

# 对数转换（处理偏态数据）
data['log_income'] = np.log(data['income'])"""
                    },
                    {
                        "subtitle": "3.2 文本特征提取",
                        "content": "从文本中提取特征：",
                        "code": """from sklearn.feature_extraction.text import TfidfVectorizer

texts = ['这是一个产品评论', '产品质量很好', '发货速度快']

# TF-IDF向量化
vectorizer = TfidfVectorizer()
text_features = vector