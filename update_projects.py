import os

# 项目数据
projects = [
    {
        "id": 1,
        "name": "数据清洗实战",
        "difficulty": "入门",
        "badge_class": "badge-easy",
        "time": "30分钟",
        "dataset": "retail_orders.csv",
        "overview": "数据清洗是数据分析流程中的关键步骤，它直接影响后续分析结果的准确性。本项目将带你掌握Pandas数据清洗的核心技能。",
        "learnings": ["处理缺失值（NaN值）", "识别和删除重复数据", "检测和处理异常值", "数据类型转换", "数据标准化和规范化"],
        "code": """import pandas as pd

# 读取数据
df = pd.read_csv('retail_orders.csv')

# 查看数据基本信息
print(df.info())
print(df.head())

# 1. 处理缺失值
df_clean = df.dropna()
df['age'] = df['age'].fillna(df['age'].mean())

# 2. 处理重复值
df_clean = df.drop_duplicates()

# 3. 检测异常值（使用IQR方法）
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[(df['price'] >= Q1 - 1.5 * IQR) & (df['price'] <= Q3 + 1.5 * IQR)]

# 4. 数据类型转换
df['order_date'] = pd.to_datetime(df['order_date'])
df['amount'] = df['amount'].astype(float)""",
        "tips": ["dropna() vs fillna()：根据业务需求选择删除还是填充缺失值", "重复值检测：使用duplicated()查看重复行，drop_duplicates()删除", "异常值处理：IQR方法是常用的异常值检测手段", "数据类型：日期字段必须转换为datetime类型才能进行时间分析"],
        "practice1_title": "处理缺失值",
        "practice1_code": "def fill_missing_with_median(df):\n    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns\n    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())\n    return df",
        "practice2_title": "数据类型转换",
        "practice2_code": "def convert_date_format(df, date_column):\n    df[date_column] = pd.to_datetime(df[date_column])\n    return df",
        "test_q1": "以下哪个方法用于删除包含缺失值的行？",
        "test_a1": ["A. fillna()", "B. dropna()", "C. drop_duplicates()", "D. isnull()"],
        "test_a1_correct": "B",
        "test_exp1": "dropna() 用于删除包含缺失值的行或列。fillna() 用于填充缺失值，drop_duplicates() 用于删除重复行，isnull() 用于检测缺失值。",
        "test_q2": "以下哪个方法可以将字符串转换为日期类型？",
        "test_a2": ["A. pd.to_numeric()", "B. pd.to_datetime()", "C. pd.astype()", "D. pd.str()"],
        "test_a2_correct": "B",
        "test_exp2": "pd.to_datetime() 专门用于将字符串转换为datetime类型，是处理日期数据的首选方法。",
        "test_q3": "IQR方法中，异常值的判断标准是？",
        "test_a3": ["A. 超出均值±1倍标准差", "B. 超出Q1-1.5*IQR或Q3+1.5*IQR", "C. 超出中位数±1倍IQR", "D. 超出最大值或最小值"],
        "test_a3_correct": "B",
        "test_exp3": "IQR方法中，异常值定义为小于Q1-1.5*IQR或大于Q3+1.5*IQR的值，这是统计学中常用的异常值检测标准。"
    },
    {
        "id": 2,
        "name": "分组聚合分析",
        "difficulty": "入门",
        "badge_class": "badge-easy",
        "time": "30分钟",
        "dataset": "retail_orders.csv",
        "overview": "分组聚合是数据分析的核心技能，用于从多个维度分析数据。本项目将带你掌握Pandas的groupby和聚合操作。",
        "learnings": ["基本分组操作", "聚合函数应用", "多维度分组", "透视表和交叉表", "分组后的过滤"],
        "code": """import pandas as pd
import numpy as np

# 读取数据
df = pd.read_csv('retail_orders.csv')

# 1. 基本分组
# 按产品类别分组，计算销量总和
category_sales = df.groupby('category')['quantity'].sum()

# 2. 多聚合函数
category_stats = df.groupby('category').agg({
    'quantity': ['sum', 'mean', 'count'],
    'price': ['mean', 'max', 'min']
})

# 3. 多维度分组
region_category = df.groupby(['region', 'category'])['sales'].sum().unstack()

# 4. 透视表
pivot = pd.pivot_table(df, values='sales', index='region', columns='category', aggfunc='sum')

# 5. 分组过滤
# 筛选总销量大于1000的产品类别
big_categories = df.groupby('category').filter(lambda x: x['sales'].sum() > 1000)

# 6. 自定义聚合函数
def range_diff(x):
    return x.max() - x.min()

custom_agg = df.groupby('category')['price'].agg(['mean', range_diff])""",
        "tips": ["groupby()：分组操作，用于按某个或多个字段分组数据", "agg()：聚合函数，可同时应用多个聚合操作", "多维度分组：使用列表作为groupby参数", "透视表：pivot_table提供更灵活的数据汇总方式"],
        "practice1_title": "分组统计",
        "practice1_code": "def calculate_category_stats(df):\n    return df.groupby('category').agg({'quantity': 'sum', 'sales': ['mean', 'sum']})",
        "practice2_title": "多维度分析",
        "practice2_code": "def multi_dimension_analysis(df):\n    return df.groupby(['region', 'category'])['sales'].sum().unstack()",
        "test_q1": "以下哪个方法用于分组操作？",
        "test_a1": ["A. .aggregate()", "B. .groupby()", "C. .filter()", "D. .transform()"],
        "test_a1_correct": "B",
        "test_exp1": "groupby() 是Pandas中用于分组操作的核心方法，可以按一个或多个字段分组数据。",
        "test_q2": "agg()方法的作用是？",
        "test_a2": ["A. 聚合数据", "B. 过滤数据", "C. 转换数据", "D. 排序数据"],
        "test_a2_correct": "A",
        "test_exp2": "agg() 方法用于执行聚合操作，可以同时应用多个聚合函数。",
        "test_q3": "pivot_table的主要用途是？",
        "test_a3": ["A. 创建透视表", "B. 数据清洗", "C. 数据合并", "D. 数据可视化"],
        "test_a3_correct": "A",
        "test_exp3": "pivot_table() 用于创建透视表，提供灵活的数据汇总和展示方式。"
    },
    {
        "id": 3,
        "name": "购物篮分析",
        "difficulty": "进阶",
        "badge_class": "badge-medium",
        "time": "45分钟",
        "dataset": "market_basket.csv",
        "overview": "购物篮分析是发现商品关联关系的重要技术，广泛用于电商推荐系统。本项目将带你掌握购物篮分析的基本方法。",
        "learnings": ["数据准备和预处理", "商品组合分析", "Apriori算法基础", "关联规则挖掘", "结果可视化"],
        "code": """import pandas as pd
from itertools import combinations
from collections import defaultdict

# 读取数据
df = pd.read_csv('market_basket.csv')

# 1. 数据准备
# 将数据转换为交易格式
transactions = []
for order_id in df['order_id'].unique():
    items = df[df['order_id'] == order_id]['product'].tolist()
    transactions.append(items)

# 2. 统计商品出现频率
item_counts = defaultdict(int)
for tx in transactions:
    for item in tx:
        item_counts[item] += 1

# 3. 计算支持度（Support）
min_support = 0.02
total_txs = len(transactions)

# 4. 查找频繁项集（Frequent Itemsets）
def find_frequent_itemsets(transactions, min_support):
    # 单商品
    itemsets = {frozenset([item]): cnt/total_txs for item, cnt in item_counts.items() if cnt/total_txs >= min_support}
    
    # 多商品组合
    k = 2
    while True:
        candidates = set()
        for itemset in itemsets.keys():
            if len(itemset) == k-1:
                for item in item_counts.keys():
                    new_itemset = itemset | frozenset([item])
                    if len(new_itemset) == k:
                        candidates.add(new_itemset)
        
        if not candidates:
            break
        
        # 计算支持度
        new_itemsets = {}
        for itemset in candidates:
            count = 0
            for tx in transactions:
                if itemset.issubset(tx):
                    count += 1
            if count / total_txs >= min_support:
                new_itemsets[itemset] = count / total_txs
        
        if not new_itemsets:
            break
        
        itemsets.update(new_itemsets)
        k += 1
    
    return itemsets

frequent_itemsets = find_frequent_itemsets(transactions, min_support)

# 5. 关联规则挖掘（简单示例）
def generate_association_rules(frequent_itemsets, min_confidence=0.5):
    rules = []
    for itemset, support in frequent_itemsets.items():
        if len(itemset) >= 2:
            for k in range(1, len(itemset)):
                for antecedent in combinations(itemset, k):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    if antecedent in frequent_itemsets:
                        confidence = support / frequent_itemsets[antecedent]
                        if confidence >= min_confidence:
                            rules.append({
                                'antecedent': antecedent,
                                'consequent': consequent,
                                'support': support,
                                'confidence': confidence
                            })
    return rules

rules = generate_association_rules(frequent_itemsets)""",
        "tips": ["支持度（Support）：商品组合出现的频率", "置信度（Confidence）：购买A后购买B的概率", "提升度（Lift）：关联规则的有效性", "Apriori算法：经典的关联规则挖掘算法"],
        "practice1_title": "统计商品频率",
        "practice1_code": "def count_item_frequency(transactions):\n    counts = {}\n    for tx in transactions:\n        for item in tx:\n            counts[item] = counts.get(item, 0) + 1\n    return counts",
        "practice2_title": "计算支持度",
        "practice2_code": "def calculate_support(item, transactions):\n    count = 0\n    for tx in transactions:\n        if item in tx:\n            count += 1\n    return count / len(transactions)",
        "test_q1": "购物篮分析中，Support表示什么？",
        "test_a1": ["A. 置信度", "B. 支持度", "C. 提升度", "D. 覆盖率"],
        "test_a1_correct": "B",
        "test_exp1": "Support（支持度）表示商品组合在所有交易中出现的频率。",
        "test_q2": "置信度（Confidence）衡量什么？",
        "test_a2": ["A. 商品组合的频率", "B. 购买A后购买B的概率", "C. 关联规则的提升", "D. 数据的完整性"],
        "test_a2_correct": "B",
        "test_exp2": "置信度（Confidence）衡量购买A后购买B的条件概率。",
        "test_q3": "Apriori算法的核心思想是？",
        "test_a3": ["A. 先验知识", "B. 如果一个项集是频繁的，它的所有非空子集也是频繁的", "C. 深度学习", "D. 决策树"],
        "test_a3_correct": "B",
        "test_exp3": "Apriori算法的核心思想是：如果一个项集是频繁的，那么它的所有非空子集也一定是频繁的。"
    },
    {
        "id": 4,
        "name": "客户聚类分析",
        "difficulty": "进阶",
        "badge_class": "badge-medium",
        "time": "45分钟",
        "dataset": "customer_features.csv",
        "overview": "客户聚类是将客户分成不同群体的技术，用于制定差异化营销策略。本项目将带你掌握K-Means聚类方法。",
        "learnings": ["数据标准化", "K-Means算法原理", "特征工程", "聚类结果分析", "客户画像构建"],
        "code": """import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('customer_features.csv')

# 1. 特征选择
features = ['recency', 'frequency', 'monetary']  # RFM模型
X = df[features]

# 2. 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. 选择最佳K值（肘部法则）
inertias = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# 4. K-Means聚类
k = 4  # 选择合适的K值
kmeans = KMeans(n_clusters=k, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# 5. 分析聚类结果
cluster_analysis = df.groupby('cluster').agg({
    'recency': 'mean',
    'frequency': 'mean',
    'monetary': 'mean'
})

# 6. 客户画像
cluster_names = {
    0: '高价值客户',
    1: '潜在客户',
    2: '流失客户',
    3: '新客户'
}
df['cluster_name'] = df['cluster'].map(cluster_names)""",
        "tips": ["数据标准化：聚类前必须对特征进行标准化处理", "K值选择：肘部法则帮助选择最佳聚类数", "RFM模型：Recency（近度）、Frequency（频度）、Monetary（额度）", "结果解释：分析每个聚类的特征并命名"],
        "practice1_title": "数据标准化",
        "practice1_code": "def standardize_features(X):\n    scaler = StandardScaler()\n    return scaler.fit_transform(X)",
        "practice2_title": "K-Means聚类",
        "practice2_code": "def perform_clustering(X, n_clusters=4):\n    kmeans = KMeans(n_clusters=n_clusters, random_state=42)\n    return kmeans.fit_predict(X)",
        "test_q1": "K-Means算法的目标是？",
        "test_a1": ["A. 最大化类间距离，最小化类内距离", "B. 计算数据均值", "C. 数据分类", "D. 数据降维"],
        "test_a1_correct": "A",
        "test_exp1": "K-Means算法的目标是最大化类间距离，最小化类内距离，使每个聚类内的样本尽可能相似。",
        "test_q2": "聚类前为什么需要标准化数据？",
        "test_a2": ["A. 提高计算速度", "B. 不同量纲的特征对聚类的影响相同", "C. 增加数据量", "D. 减少内存使用"],
        "test_a2_correct": "B",
        "test_exp2": "数据标准化是为了让不同量纲的特征对聚类的影响相同，避免数值大的特征主导聚类结果。",
        "test_q3": "RFM模型中，F代表什么？",
        "test_a3": ["A. Recency", "B. Frequency", "C. Monetary", "D. Future"],
        "test_a3_correct": "B",
        "test_exp3": "RFM模型中，R代表Recency（近度），F代表Frequency（频度），M代表Monetary（额度）。"
    },
    {
        "id": 5,
        "name": "数据可视化",
        "difficulty": "进阶",
        "badge_class": "badge-medium",
        "time": "45分钟",
        "dataset": "retail_orders.csv",
        "overview": "数据可视化是展示分析结果的重要手段。本项目将带你掌握使用Matplotlib和Seaborn创建各类图表的方法。",
        "learnings": ["基本图表类型", "美化图表样式", "多子图布局", "时间序列可视化", "统计图表"],
        "code": """import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置样式
plt.style.use('seaborn-v0_8')
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('retail_orders.csv')
df['date'] = pd.to_datetime(df['date'])

# 1. 折线图 - 时间序列
fig, ax = plt.subplots(figsize=(12, 6))
daily_sales = df.groupby('date')['sales'].sum()
ax.plot(daily_sales.index, daily_sales.values, linewidth=2, color='#3b82f6')
ax.set_title('每日销售趋势', fontsize=16)
ax.set_xlabel('日期')
ax.set_ylabel('销售额')
plt.tight_layout()

# 2. 柱状图 - 类别比较
fig, ax = plt.subplots(figsize=(10, 6))
category_sales = df.groupby('category')['sales'].sum().sort_values(ascending=False)
category_sales.plot(kind='bar', ax=ax, color=['#3b82f6', '#8b5cf6', '#f59e0b'])
ax.set_title('各品类销售额对比', fontsize=14)
ax.set_xlabel('品类')
ax.set_ylabel('销售额')
plt.xticks(rotation=45)

# 3. 散点图 - 相关性
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['quantity'], df['sales'], alpha=0.6, color='#3b82f6')
ax.set_title('数量与销售额的关系', fontsize=14)
ax.set_xlabel('数量')
ax.set_ylabel('销售额')

# 4. 箱线图 - 分布和异常值
fig, ax = plt.subplots(figsize=(10, 6))
df.boxplot(column='sales', by='category', ax=ax)
ax.set_title('各品类销售分布', fontsize=14)
ax.set_xlabel('品类')
ax.set_ylabel('销售额')

# 5. 热力图 - 相关性矩阵
corr = df[['sales', 'quantity', 'price']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=ax)
ax.set_title('特征相关性矩阵', fontsize=14)

# 6. 多子图布局
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('综合分析报告', fontsize=16)

# 子图1
daily_sales.plot(ax=axes[0,0], color='#3b82f6')
axes[0,0].set_title('销售趋势')

# 子图2
category_sales.plot(kind='bar', ax=axes[0,1], color='#8b5cf6')
axes[0,1].set_title('品类分布')

# 子图3
axes[1,0].scatter(df['quantity'], df['sales'], alpha=0.5, color='#10b981')
axes[1,0].set_title('数量与销售额')

# 子图4
df['sales'].hist(bins=30, ax=axes[1,1], color='#f59e0b')
axes[1,1].set_title('销售额分布')

plt.tight_layout()
plt.show()""",
        "tips": ["选择合适的图表类型：折线看趋势，柱状看对比，散点看关系", "颜色搭配：使用和谐的配色方案", "标签和标题：清晰的图表说明", "美观性：网格、图例、边框样式的细节处理"],
        "practice1_title": "绘制折线图",
        "practice1_code": "def plot_time_series(df, date_col, value_col, title):\n    plt.figure(figsize=(12, 6))\n    data = df.groupby(date_col)[value_col].sum()\n    plt.plot(data.index, data.values)\n    plt.title(title)\n    plt.show()",
        "practice2_title": "绘制柱状图",
        "practice2_code": "def plot_bar_chart(df, category_col, value_col, title):\n    data = df.groupby(category_col)[value_col].sum().sort_values()\n    data.plot(kind='bar', figsize=(10, 6))\n    plt.title(title)\n    plt.show()",
        "test_q1": "以下哪种图表最适合展示时间序列趋势？",
        "test_a1": ["A. 散点图", "B. 折线图", "C. 饼图", "D. 热力图"],
        "test_a1_correct": "B",
        "test_exp1": "折线图最适合展示时间序列的趋势变化。",
        "test_q2": "箱线图（Box Plot）不能展示什么？",
        "test_a2": ["A. 中位数", "B. 四分位数", "C. 异常值", "D. 数据量"],
        "test_a2_correct": "D",
        "test_exp2": "箱线图展示中位数、四分位数、异常值等分布信息，但不直接展示数据量。",
        "test_q3": "热力图（Heatmap）主要用于？",
        "test_a3": ["A. 展示相关性", "B. 展示时间趋势", "C. 展示分类对比", "D. 展示分布情况"],
        "test_a3_correct": "A",
        "test_exp3": "热力图主要用于展示变量之间的相关性矩阵。"
    },
    {
        "id": 6,
        "name": "A/B测试分析",
        "difficulty": "进阶",
        "badge_class": "badge-medium",
        "time": "45分钟",
        "dataset": "ab_test.csv",
        "overview": "A/B测试是用于比较两个版本效果的方法，广泛用于产品优化。本项目将带你掌握A/B测试的统计分析方法。",
        "learnings": ["实验设计基础", "假设检验", "P值解读", "置信区间", "样本量计算"],
        "code": """import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('ab_test.csv')

# 1. 数据探索
print('实验组和对照组样本量:')
print(df['group'].value_counts())

print('\\n转化率:')
conversion_rates = df.groupby('group')['conversion'].mean()
print(conversion_rates)

# 2. 计算统计量
control = df[df['group'] == 'control']['conversion']
treatment = df[df['group'] == 'treatment']['conversion']

n_control = len(control)
n_treatment = len(treatment)
p_control = control.mean()
p_treatment = treatment.mean()

print(f'\\n对照组转化率: {p_control:.4f}')
print(f'实验组转化率: {p_treatment:.4f}')
print(f'提升幅度: {(p_treatment - p_control)/p_control:.2%}')

# 3. 双样本比例Z检验
from statsmodels.stats.proportion import proportions_ztest

successes = np.array([control.sum(), treatment.sum()])
nobs = np.array([n_control, n_treatment])

z_stat, p_value = proportions_ztest(successes, nobs)

print(f'\\nZ统计量: {z_stat:.4f}')
print(f'P值: {p_value:.4f}')

# 4. 结果解读
alpha = 0.05
if p_value < alpha:
    print('\\n✅ 结果显著：实验组效果优于对照组')
else:
    print('\\n❌ 结果不显著：两组效果无统计学差异')

# 5. 置信区间
from statsmodels.stats.proportion import proportion_confint

ci_control = proportion_confint(control.sum(), n_control, alpha=0.05)
ci_treatment = proportion_confint(treatment.sum(), n_treatment, alpha=0.05)

print(f'\\n对照组95%置信区间: [{ci_control[0]:.4f}, {ci_control[1]:.4f}]')
print(f'实验组95%置信区间: [{ci_treatment[0]:.4f}, {ci_treatment[1]:.4f}]')

# 6. 可视化对比
fig, ax = plt.subplots(figsize=(10, 6))
groups = ['对照组', '实验组']
rates = [p_control, p_treatment]
errors = [p_control - ci_control[0], p_treatment - ci_treatment[0]]

ax.bar(groups, rates, color=['#64748b', '#3b82f6'], yerr=errors, capsize=5)
ax.set_ylabel('转化率')
ax.set_title('A/B测试结果对比')
ax.set_ylim(0, max(rates) + 0.05)

# 添加数值标签
for i, (rate, err) in enumerate(zip(rates, errors)):
    ax.text(i, rate + 0.01, f'{rate:.2%}', ha='center')

plt.show()""",
        "tips": ["P值小于0.05通常认为结果显著", "置信区间：展示结果的不确定性范围", "样本量：足够的样本量才能得到可靠结果", "不要偷看：A/B测试结束后再分析结果"],
        "practice1_title": "计算转化率",
        "practice1_code": "def calculate_conversion(df, group_col, outcome_col):\n    return df.groupby(group_col)[outcome_col].mean()",
        "practice2_title": "比例检验",
        "practice2_code": "def ab_test_analysis(control_success, control_total, treat_success, treat_total):\n    from statsmodels.stats.proportion import proportions_ztest\n    successes = np.array([control_success, treat_success])\n    nobs = np.array([control_total, treat_total])\n    z_stat, p_value = proportions_ztest(successes, nobs)\n    return z_stat, p_value",
        "test_q1": "A/B测试中，P值表示什么？",
        "test_a1": ["A. 实验组比对照组好的概率", "B. 观测到当前差异的概率", "C. 统计显著性", "D. 置信度"],
        "test_a1_correct": "B",
        "test_exp1": "P值表示在零假设成立的情况下，观测到当前或更极端差异的概率。",
        "test_q2": "通常显著性水平alpha设置为多少？",
        "test_a2": ["A. 0.01", "B. 0.05", "C. 0.10", "D. 0.50"],
        "test_a2_correct": "B",
        "test_exp2": "通常显著性水平alpha设置为0.05，即5%。",
        "test_q3": "置信区间表示什么？",
        "test_a3": ["A. 确定的结果", "B. 结果可能的范围", "C. 标准差", "D. 平均值"],
        "test_a3_correct": "B",
        "test_exp3": "置信区间表示真实值可能的范围，体现了结果的不确定性。"
    },
    {
        "id": 8,
        "name": "特征工程",
        "difficulty": "高级",
        "badge_class": "badge-hard",
        "time": "60分钟",
        "dataset": "customer_features.csv",
        "overview": "特征工程是机器学习的关键步骤，好的特征能显著提升模型性能。本项目将带你掌握特征工程的核心技术。",
        "learnings": ["特征构造", "特征变换", "特征选择", "编码方法", "特征标准化"],
        "code": """import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
import category_encoders as ce

# 读取数据
df = pd.read_csv('customer_features.csv')

# 1. 特征构造
# 从日期构造特征
if 'signup_date' in df.columns:
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['signup_year'] = df['signup_date'].dt.year
    df['signup_month'] = df['signup_date'].dt.month
    df['signup_dayofweek'] = df['signup_date'].dt.dayofweek
    df['days_since_signup'] = (pd.Timestamp.now() - df['signup_date']).dt.days

# 数值特征构造
df['total_amount'] = df['quantity'] * df['price']
df['average_order_value'] = df['total_amount'] / df['orders']
df['log_amount'] = np.log1p(df['amount'])

# 2. 特征变换
# 分箱
df['age_group'] = pd.cut(df['age'], bins=[0, 20, 30, 40, 50, 100], 
                          labels=['<20', '20-30', '30-40', '40-50', '50+'])

# 标准化
scaler = StandardScaler()
numerical_features = ['age', 'income', 'tenure']
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# 归一化
minmax = MinMaxScaler()
df[['amount_scaled']] = minmax.fit_transform(df[['amount']])

# 3. 特征编码
# 标签编码
if 'category' in df.columns:
    le = LabelEncoder()
    df['category_encoded'] = le.fit_transform(df['category'])

# 独热编码
df_onehot = pd.get_dummies(df, columns=['gender'])

# 4. 特征选择
# 相关性筛选
corr = df.select_dtypes(include=[np.number]).corr()
high_corr_features = []
for i in range(len(corr.columns)):
    for j in range(i+1, len(corr.columns)):
        if abs(corr.iloc[i, j]) > 0.7:
            high_corr_features.append(corr.columns[j])

print('高相关性特征:', high_corr_features)

# 5. 特征重要性（示例）
from sklearn.ensemble import RandomForestRegressor

X = df.drop(['target'], axis=1, errors='ignore')
y = df.get('target', df['amount'])

rf = RandomForestRegressor(n_estimators=100)
rf.fit(X.select_dtypes(include=[np.number]), y)

feature_importance = pd.DataFrame({
    'feature': X.select_dtypes(include=[np.number]).columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print('\\n特征重要性:')
print(feature_importance.head(10))""",
        "tips": ["业务理解：特征工程需要结合业务知识", "不要过度拟合：避免构造过多的特征", "特征选择：去除无用特征，提高模型效率", "可解释性：保持特征的可解释性"],
        "practice1_title": "构造时间特征",
        "practice1_code": "def extract_date_features(df, date_col):\n    df = df.copy()\n    df[date_col] = pd.to_datetime(df[date_col])\n    df['year'] = df[date_col].dt.year\n    df['month'] = df[date_col].dt.month\n    df['dayofweek'] = df[date_col].dt.dayofweek\n    return df",
        "practice2_title": "特征标准化",
        "practice2_code": "def standardize_features(df, features):\n    scaler = StandardScaler()\n    df = df.copy()\n    df[features] = scaler.fit_transform(df[features])\n    return df",
        "test_q1": "特征工程的主要目的是？",
        "test_a1": ["A. 增加数据量", "B. 创建和改进特征以提高模型性能", "C. 数据可视化", "D. 数据清洗"],
        "test_a1_correct": "B",
        "test_exp1": "特征工程的主要目的是创建和改进特征，以提高机器学习模型的性能。",
        "test_q2": "独热编码（One-Hot Encoding）用于处理什么类型的特征？",
        "test_a2": ["A. 数值特征", "B. 分类特征", "C. 时间特征", "D. 文本特征"],
        "test_a2_correct": "B",
        "test_exp2": "独热编码主要用于处理分类特征。",
        "test_q3": "特征缩放的目的是？",
        "test_a3": ["A. 减少数据量", "B. 让特征在相同的尺度上", "C. 数据可视化", "D. 数据加密"],
        "test_a3_correct": "B",
        "test_exp3": "特征缩放的目的是让不同量纲的特征在相同的尺度上，避免某些特征主导计算。"
    },
    {
        "id": 9,
        "name": "异常值检测",
        "difficulty": "高级",
        "badge_class": "badge-hard",
        "time": "45分钟",
        "dataset": "customer_features.csv",
        "overview": "异常值会严重影响分析结果的准确性。本项目将带你掌握多种异常值检测方法。",
        "learnings": ["统计方法（IQR）", "Z-score方法", "可视化方法", "异常值处理策略"],
        "code": """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
df = pd.read_csv('customer_features.csv')

# 1. IQR方法
def detect_outliers_iqr(df, feature):
    Q1 = df[feature].quantile(0.25)
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = (df[feature] < lower_bound) | (df[feature] > upper_bound)
    return outliers, lower_bound, upper_bound

# 2. Z-score方法
def detect_outliers_zscore(df, feature, threshold=3):
    z_scores = (df[feature] - df[feature].mean()) / df[feature].std()
    outliers = abs(z_scores) > threshold
    return outliers, -threshold, threshold

# 3. 应用到数据
feature = 'amount'

outliers_iqr, lower_iqr, upper_iqr = detect_outliers_iqr(df, feature)
outliers_z, lower_z, upper_z = detect_outliers_zscore(df, feature)

print(f'IQR方法检测到 {outliers_iqr.sum()} 个异常值')
print(f'Z-score方法检测到 {outliers_z.sum()} 个异常值')

# 4. 可视化
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# 箱线图
ax1.boxplot(df[feature])
ax1.set_title(f'{feature} 的箱线图')
ax1.set_ylabel(feature)

# 散点图
ax2.scatter(range(len(df)), df[feature], c=outliers_iqr, cmap='coolwarm')
ax2.set_title(f'{feature} 的异常值分布 (IQR方法)')
ax2.set_xlabel('索引')
ax2.set_ylabel(feature)
plt.tight_layout()

# 5. 异常值处理
# 方法1: 删除
df_clean = df[~outliers_iqr].copy()

# 方法2: 截断
df_cap = df.copy()
df_cap[feature] = np.where(df[feature] < lower_iqr, lower_iqr, df[feature])
df_cap[feature] = np.where(df[feature] > upper_iqr, upper_iqr, df[feature])

# 方法3: 用分位数代替
q_low = df[feature].quantile(0.01)
q_high = df[feature].quantile(0.99)
df_quantile = df.copy()
df_quantile[feature] = np.where(df[feature] < q_low, q_low, df[feature])
df_quantile[feature] = np.where(df[feature] > q_high, q_high, df[feature])

print(f'\\n处理后的统计:')
print(f'原始: 均值 = {df[feature].mean():.2f}, 标准差 = {df[feature].std():.2f}')
print(f'删除后: 均值 = {df_clean[feature].mean():.2f}, 标准差 = {df_clean[feature].std():.2f}')
print(f'截断后: 均值 = {df_cap[feature].mean():.2f}, 标准差 = {df_cap[feature].std():.2f}')""",
        "tips": ["IQR方法：适合大多数情况，不受极端值影响", "Z-score：适合正态分布数据", "可视化：直观展示异常值的分布", "处理策略：根据业务场景选择合适的处理方式"],
        "practice1_title": "IQR检测",
        "practice1_code": "def iqr_outliers(series):\n    Q1 = series.quantile(0.25)\n    Q3 = series.quantile(0.75)\n    IQR = Q3 - Q1\n    return (series < Q1 - 1.5*IQR) | (series > Q3 + 1.5*IQR)",
        "practice2_title": "截断处理",
        "practice2_code": "def cap_outliers(series, lower, upper):\n    return np.clip(series, lower, upper)",
        "test_q1": "IQR方法中，通常使用什么倍数作为边界？",
        "test_a1": ["A. 1.0", "B. 1.5", "C. 2.0", "D. 3.0"],
        "test_a1_correct": "B",
        "test_exp1": "IQR方法中，通常使用1.5倍IQR作为异常值判断边界。",
        "test_q2": "Z-score方法中，通常用什么作为阈值？",
        "test_a2": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "test_a2_correct": "C",
        "test_exp2": "Z-score方法中，通常使用3作为阈值，即超出均值±3个标准差视为异常值。",
        "test_q3": "以下哪种不是异常值的处理方法？",
        "test_a3": ["A. 删除", "B. 截断", "C. 忽略", "D. 转置"],
        "test_a3_correct": "D",
        "test_exp3": "转置不是异常值处理方法，其他都是常见的处理策略。"
    },
    {
        "id": 10,
        "name": "多数据集合并",
        "difficulty": "进阶",
        "badge_class": "badge-medium",
        "time": "45分钟",
        "dataset": "retail_orders.csv",
        "overview": "实际业务中，数据往往分散在多个表中。本项目将带你掌握数据合并的各种方法。",
        "learnings": ["各种连接（Join）类型", "横向合并", "纵向合并", "复杂合并策略"],
        "code": """import pandas as pd
import numpy as np

# 创建示例数据
orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5],
    'customer_id': [101, 102, 103, 101, 104],
    'product_id': [201, 202, 203, 201, 202],
    'quantity': [2, 1, 3, 1, 2],
    'order_date': pd.date_range('2024-01-01', periods=5)
})

customers = pd.DataFrame({
    'customer_id': [101, 102, 103, 105],
    'name': ['张三', '李四', '王五', '赵六'],
    'level': ['黄金', '白银', '青铜', '黄金'],
    'signup_date': pd.date_range('2023-01-01', periods=4)
})

products = pd.DataFrame({
    'product_id': [201, 202, 203, 204],
    'name': ['T恤', '裤子', '鞋子', '帽子'],
    'price': [100, 200, 300, 50],
    'category': ['衣服', '衣服', '鞋子', '配饰']
})

# 1. 内连接（Inner Join）
# 只保留两个表都有的记录
merged_inner = pd.merge(orders, customers, on='customer_id', how='inner')

# 2. 左连接（Left Join）
# 保留左表所有记录，右表没有的填NaN
merged_left = pd.merge(orders, customers, on='customer_id', how='left')

# 3. 右连接（Right Join）
merged_right = pd.merge(orders, customers, on='customer_id', how='right')

# 4. 外连接（Outer Join）
# 保留两个表的所有记录
merged_outer = pd.merge(orders, customers, on='customer_id', how='outer')

# 5. 多表连接
# 先合并订单和客户，再合并产品
temp = pd.merge(orders, customers, on='customer_id', how='left')
full_data = pd.merge(temp, products, on='product_id', how='left')

# 6. 纵向合并（Concatenate）
orders_jan = orders[orders['order_date'].dt.month == 1]
orders_feb = orders[orders['order_date'].dt.month == 2]

all_orders = pd.concat([orders_jan, orders_feb], axis=0, ignore_index=True)

# 7. 连接键不一致的情况
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
df2 = pd.DataFrame({'C': [1, 2, 4], 'D': ['p', 'q', 'r']})

merged_diff = pd.merge(df1, df2, left_on='A', right_on='C', how='left')

# 8. 多键连接
df_a = pd.DataFrame({
    'country': ['CN', 'CN', 'US', 'US'],
    'year': [2023, 2024, 2023, 2024],
    'value': [100, 110, 200, 210]
})

df_b = pd.DataFrame({
    'country': ['CN', 'CN', 'US'],
    'year': [2023, 2024, 2023],
    'metric': [0.5, 0.6, 0.7]
})

merged_multi = pd.merge(df_a, df_b, on=['country', 'year'])

# 9. 计算销售额
full_data['amount'] = full_data['quantity'] * full_data['price']
print('完整数据集:')
print(full_data[['name', 'order_date', 'name', 'quantity', 'price', 'amount']])""",
        "tips": ["理解连接类型：inner、left、right、outer的区别", "确认连接键：确保连接的字段正确对应", "处理重复列：多表合并时注意列名冲突", "检查数据质量：合并后验证数据完整性"],
        "practice1_title": "多表合并",
        "practice1_code": "def merge_orders_products_customers(orders, products, customers):\n    temp = pd.merge(orders, customers, on='customer_id', how='left')\n    return pd.merge(temp, products, on='product_id', how='left')",
        "practice2_title": "纵向追加",
        "practice2_code": "def append_dataframes(df_list):\n    return pd.concat(df_list, axis=0, ignore_index=True)",
        "test_q1": "只保留两个表中都有的记录，用哪种连接？",
        "test_a1": ["A. Inner Join", "B. Left Join", "C. Right Join", "D. Outer Join"],
        "test_a1_correct": "A",
        "test_exp1": "Inner Join（内连接）只保留两个表中都有的记录。",
        "test_q2": "保留左表所有记录，右表没有的填NaN，用哪种连接？",
        "test_a2": ["A. Inner Join", "B. Left Join", "C. Right Join", "D. Outer Join"],
        "test_a2_correct": "B",
        "test_exp2": "Left Join（左连接）保留左表所有记录。",
        "test_q3": "pd.concat主要用于？",
        "test_a3": ["A. 横向合并", "B. 纵向合并", "C. 表连接", "D. 数据透视"],
        "test_a3_correct": "B",
        "test_exp3": "pd.concat主要用于纵向合并（追加）数据。"
    }
]

# HTML模板
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Pandas 数据分析实战训练营</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b; line-height: 1.6; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
        
        header {{ background: white; border-bottom: 1px solid #e2e8f0; padding: 16px 0; }}
        header .container {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-weight: 700; color: #3b82f6; font-size: 18px; }}
        header a {{ color: #64748b; text-decoration: none; font-size: 14px; }}
        header a:hover {{ color: #3b82f6; }}
        
        .project-header {{ padding: 40px 0; }}
        .project-title {{ font-size: 32px; font-weight: 700; color: #0f172a; margin-bottom: 12px; }}
        .project-meta {{ display: flex; gap: 16px; color: #64748b; font-size: 14px; }}
        .badge {{ padding: 4px 12px; border-radius: 10px; font-size: 12px; font-weight: 600; }}
        .{badge_class} {{ background: {bg_color}; color: {text_color}; }}
        .badge-time {{ background: #f1f5f9; color: #64748b; }}
        
        .tabs {{ display: flex; gap: 8px; margin-bottom: 24px; background: #f1f5f9; padding: 6px; border-radius: 12px; }}
        .tab {{ padding: 10px 20px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; border: none; background: transparent; color: #64748b; }}
        .tab.active {{ background: white; color: #3b82f6; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}
        
        .tab-content {{ display: none; }}
        .tab-content.active {{ display: block; }}
        
        .content-card {{ background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; margin-bottom: 24px; }}
        .content-card h3 {{ font-size: 20px; font-weight: 600; color: #0f172a; margin-bottom: 16px; }}
        .content-card p {{ color: #64748b; line-height: 1.6; margin-bottom: 12px; }}
        .content-card ul {{ list-style: disc; padding-left: 20px; color: #64748b; }}
        .content-card ul li {{ margin-bottom: 8px; }}
        
        .code-box {{ background: #1e1e1e; border-radius: 12px; padding: 20px; overflow-x: auto; margin: 16px 0; }}
        .code-box pre {{ color: #d4d4d4; font-family: 'Monaco', 'Consolas', monospace; font-size: 14px; line-height: 1.6; white-space: pre; }}
        
        .question-box {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; margin-bottom: 16px; }}
        .question-box h4 {{ font-size: 16px; font-weight: 600; color: #0f172a; margin-bottom: 12px; }}
        .question-box p {{ color: #64748b; margin-bottom: 12px; }}
        
        .option-btn {{ display: block; width: 100%; padding: 14px 16px; margin-bottom: 10px; border: 1px solid #e2e8f0; border-radius: 10px; background: white; cursor: pointer; text-align: left; font-size: 14px; color: #334155; transition: all 0.2s; }}
        .option-btn:hover {{ border-color: #3b82f6; background: #eff6ff; }}
        .option-btn.selected {{ border-color: #3b82f6; background: #eff6ff; }}
        .option-btn.correct {{ border-color: #16a34a; background: #ecfdf5; color: #16a34a; }}
        .option-btn.wrong {{ border-color: #ef4444; background: #fef2f2; color: #ef4444; }}
        
        .explanation {{ background: #fefce8; border-left: 4px solid #eab308; padding: 16px; margin-top: 16px; border-radius: 0 8px 8px 0; display: none; }}
        .explanation p {{ color: #854d0e; }}
        .explanation strong {{ color: #a16207; }}
        
        .btn {{ padding: 12px 24px; border-radius: 10px; font-weight: 600; font-size: 14px; text-decoration: none; transition: all 0.2s; }}
        .btn-primary {{ background: #3b82f6; color: white; border: none; cursor: pointer; }}
        .btn-primary:hover {{ background: #2563eb; }}
        .btn-outline {{ border: 1px solid #e2e8f0; color: #64748b; background: white; }}
        .btn-outline:hover {{ border-color: #3b82f6; color: #3b82f6; }}
        
        .test-result {{ background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 32px; text-align: center; margin-top: 24px; display: none; }}
        .test-result h3 {{ font-size: 24px; font-weight: 700; margin-bottom: 16px; }}
        .test-result .score {{ font-size: 48px; font-weight: 700; color: #3b82f6; margin-bottom: 24px; }}
        
        footer {{ text-align: center; padding: 32px 0; border-top: 1px solid #e2e8f0; color: #94a3b8; font-size: 14px; }}
        
        @media (max-width: 768px) {{
            .project-title {{ font-size: 24px; }}
            .project-meta {{ flex-wrap: wrap; }}
            .tabs {{ flex-wrap: wrap; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">TT's Learning</div>
            <a href="../../index.html">← 返回首页</a>
        </div>
    </header>

    <div class="container">
        <div class="project-header">
            <h1 class="project-title">{name}</h1>
            <div class="project-meta">
                <span class="badge {badge_class}">{difficulty}</span>
                <span class="badge badge-time">{time}</span>
                <span>📁 {dataset}</span>
            </div>
        </div>

        <div class="tabs">
            <button class="tab active" onclick="showTab('learn')">📚 学习</button>
            <button class="tab" onclick="showTab('practice')">✏️ 练习</button>
            <button class="tab" onclick="showTab('test')">📝 测试</button>
        </div>

        <div id="learn-tab" class="tab-content active">
            <div class="content-card">
                <h3>📌 项目概述</h3>
                <p>{overview}</p>
                <ul>
                    {learnings_html}
                </ul>
            </div>

            <div class="content-card">
                <h3>🔧 核心代码</h3>
                <p>以下是本项目常用的代码示例：</p>
                <div class="code-box">
                    <pre>{code}</pre>
                </div>
            </div>

            <div class="content-card">
                <h3>💡 学习要点</h3>
                <ul>
                    {tips_html}
                </ul>
            </div>
        </div>

        <div id="practice-tab" class="tab-content">
            <div class="content-card">
                <h3>✏️ 编程练习</h3>
                
                <div class="question-box">
                    <h4>练习1：{practice1_title}</h4>
                    <p>请完善下面的代码：</p>
                    <div class="code-box">
                        <pre>{practice1_stub}</pre>
                    </div>
                    <button class="btn btn-primary" onclick="showAnswer(1)">查看答案</button>
                </div>

                <div class="question-box">
                    <h4>练习2：{practice2_title}</h4>
                    <p>请完善下面的代码：</p>
                    <div class="code-box">
                        <pre>{practice2_stub}</pre>
                    </div>
                    <button class="btn btn-primary" onclick="showAnswer(2)">查看答案</button>
                </div>
            </div>
        </div>

        <div id="test-tab" class="tab-content">
            <div class="content-card">
                <h3>📝 知识测试</h3>
                
                <div class="question-box">
                    <h4>问题1：{test_q1}</h4>
                    <button class="option-btn" onclick="selectOption(1, 'A')">{test_a1_0}</button>
                    <button class="option-btn" onclick="selectOption(1, 'B')">{test_a1_1}</button>
                    <button class="option-btn" onclick="selectOption(1, 'C')">{test_a1_2}</button>
                    <button class="option-btn" onclick="selectOption(1, 'D')">{test_a1_3}</button>
                    <div class="explanation" id="exp1">
                        <p><strong>正确答案：{test_a1_correct}</strong></p>
                        <p>{test_exp1}</p>
                    </div>
                </div>

                <div class="question-box">
                    <h4>问题2：{test_q2}</h4>
                    <button class="option-btn" onclick="selectOption(2, 'A')">{test_a2_0}</button>
                    <button class="option-btn" onclick="selectOption(2, 'B')">{test_a2_1}</button>
                    <button class="option-btn" onclick="selectOption(2, 'C')">{test_a2_2}</button>
                    <button class="option-btn" onclick="selectOption(2, 'D')">{test_a2_3}</button>
                    <div class="explanation" id="exp2">
                        <p><strong>正确答案：{test_a2_correct}</strong></p>
                        <p>{test_exp2}</p>
                    </div>
                </div>

                <div class="question-box">
                    <h4>问题3：{test_q3}</h4>
                    <button class="option-btn" onclick="selectOption(3, 'A')">{test_a3_0}</button>
                    <button class="option-btn" onclick="selectOption(3, 'B')">{test_a3_1}</button>
                    <button class="option-btn" onclick="selectOption(3, 'C')">{test_a3_2}</button>
                    <button class="option-btn" onclick="selectOption(3, 'D')">{test_a3_3}</button>
                    <div class="explanation" id="exp3">
                        <p><strong>正确答案：{test_a3_correct}</strong></p>
                        <p>{test_exp3}</p>
                    </div>
                </div>

                <div style="text-align: center; margin-top: 24px;">
                    <button class="btn btn-primary" onclick="checkAnswers()">提交答案</button>
                </div>

                <div class="test-result" id="result">
                    <h3 id="result-title"></h3>
                    <div class="score" id="score"></div>
                    <button class="btn btn-outline" onclick="resetTest()">重新测试</button>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>© 2024 TT's Learning Space · Pandas 数据分析实战训练营</p>
    </footer>

    <script>
        const correctAnswers = {{1: '{test_a1_correct}', 2: '{test_a2_correct}', 3: '{test_a3_correct}'}};
        const userAnswers = {{}};
        const answerData = {{
            1: `{practice1_code}`,
            2: `{practice2_code}`
        }};

        function showTab(tabName) {{
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelector(`button[onclick="showTab('${{tabName}}')"]`).classList.add('active');
            document.getElementById(`${{tabName}}-tab`).classList.add('active');
        }}

        function showAnswer(num) {{
            alert('练习' + num + '答案：\\n\\n' + answerData[num]);
        }}

        function selectOption(qNum, answer) {{
            const options = document.querySelectorAll(`#test-tab .question-box:nth-child(${{qNum+1}}) .option-btn`);
            options.forEach(o => o.classList.remove('selected'));
            event.target.classList.add('selected');
            userAnswers[qNum] = answer;
        }}

        function checkAnswers() {{
            let correct = 0;
            Object.keys(correctAnswers).forEach(q => {{
                const options = document.querySelectorAll(`#test-tab .question-box:nth-child(${{parseInt(q)+1}}) .option-btn`);
                options.forEach(opt => {{
                    const optAnswer = opt.textContent.trim()[0];
                    if (optAnswer === correctAnswers[q]) {{
                        opt.classList.add('correct');
                    }} else if (opt.classList.contains('selected') && optAnswer !== correctAnswers[q]) {{
                        opt.classList.add('wrong');
                    }}
                }});
                document.getElementById(`exp${{q}}`).style.display = 'block';
                if (userAnswers[q] === correctAnswers[q]) correct++;
            }});
            
            const score = Math.round((correct / Object.keys(correctAnswers).length) * 100);
            document.getElementById('score').textContent = `${{score}}分`;
            document.getElementById('result-title').textContent = score >= 60 ? '🎉 测试通过！' : '💪 继续加油！';
            document.getElementById('result').style.display = 'block';
        }}

        function resetTest() {{
            document.querySelectorAll('.option-btn').forEach(o => o.classList.remove('selected', 'correct', 'wrong'));
            document.querySelectorAll('.explanation').forEach(e => e.style.display = 'none');
            document.getElementById('result').style.display = 'none';
            Object.keys(userAnswers).forEach(k => delete userAnswers[k]);
        }}
    </script>
</body>
</html>"""

# 生成每个项目的HTML
for proj in projects:
    # 难度颜色
    if proj['badge_class'] == 'badge-easy':
        bg_color = '#dcfce7'
        text_color = '#16a34a'
    elif proj['badge_class'] == 'badge-medium':
        bg_color = '#dbeafe'
        text_color = '#2563eb'
    else:  # badge-hard
        bg_color = '#fce7f3'
        text_color = '#db2777'
    
    # 学习要点HTML
    learnings_html = '\n'.join([f'<li>{item}</li>' for item in proj['learnings']])
    tips_html = '\n'.join([f'<li><strong>{item.split("：")[0]}：</strong>{item.split("：")[1] if "：" in item else item}</li>' for item in proj['tips']])
    
    # 练习代码占位符
    practice1_stub = proj['practice1_code'].split('\n')[0] + '\n    # 请在此处编写代码\n    \n    return ' + proj['practice1_code'].split('return ')[1].strip()
    if len(proj['practice1_code'].split('\n')) > 2:
        practice1_stub = '\n'.join(proj['practice1_code'].split('\n')[:2]) + '\n    # 请在此处编写代码\n    \n    ' + '\n'.join(proj['practice1_code'].split('\n')[2:])
    
    practice2_stub = proj['practice2_code'].split('\n')[0] + '\n    # 请在此处编写代码\n    \n    return ' + proj['practice2_code'].split('return ')[1].strip()
    if len(proj['practice2_code'].split('\n')) > 2:
        practice2_stub = '\n'.join(proj['practice2_code'].split('\n')[:2]) + '\n    # 请在此处编写代码\n    \n    ' + '\n'.join(proj['practice2_code'].split('\n')[2:])
    
    # 生成HTML
    html_content = html_template.format(
        name=proj['name'],
        difficulty=proj['difficulty'],
        badge_class=proj['badge_class'],
        bg_color=bg_color,
        text_color=text_color,
        time=proj['time'],
        dataset=proj['dataset'],
        overview=proj['overview'],
        learnings_html=learnings_html,
        code=proj['code'].replace('`', '\\`'),
        tips_html=tips_html,
        practice1_title=proj['practice1_title'],
        practice1_stub=practice1_stub.replace('`', '\\`'),
        practice1_code=proj['practice1_code'].replace('`', '\\`'),
        practice2_title=proj['practice2_title'],
        practice2_stub=practice2_stub.replace('`', '\\`'),
        practice2_code=proj['practice2_code'].replace('`', '\\`'),
        test_q1=proj['test_q1'],
        test_a1_0=proj['test_a1'][0],
        test_a1_1=