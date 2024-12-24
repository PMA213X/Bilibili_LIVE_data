import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties

# 指定文件名
filename = '弥希Miki1735045086.json'

# 读取 JSON 文件内容，指定 UTF-8 编码
with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 将 JSON 数据转换为 DataFrame
df = pd.DataFrame(data)

# 清洗数据：移除值为 "未知a" 或 -9999 的行
df_cleaned = df[(df['性别'] != '未知a') & (df['VIP类型'] != -9999) & (df['官方认证类型'] != -9999)]

# 强制转换数据类型
df_cleaned['uid'] = pd.to_numeric(df_cleaned['uid'], errors='coerce')
df_cleaned['粉丝牌等级'] = pd.to_numeric(df_cleaned['粉丝牌等级'], errors='coerce')
df_cleaned['陪伴天数'] = pd.to_numeric(df_cleaned['陪伴天数'], errors='coerce')

# 设置中文字体以确保中文可以正确显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# 创建散点图函数
def create_scatter_plot(x_data, y_data, x_label, y_label, title, filename):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_data, y=y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()

# 分别为 粉丝牌等级 和 陪伴天数 创建散点图
create_scatter_plot(df_cleaned.index, df_cleaned['粉丝牌等级'], '索引', '粉丝牌等级', '粉丝牌等级分布', 'scatter_fans_level.png')
create_scatter_plot(df_cleaned.index, df_cleaned['陪伴天数'], '索引', '陪伴天数', '陪伴天数分布', 'scatter_days.png')

# 饼图：性别、等级、VIP类型、官方认证类型
categories = ['性别', '等级', 'VIP类型', '官方认证类型']

for category in categories:
    plt.figure(figsize=(6, 6))
    counts = df_cleaned[category].value_counts()
    if not counts.empty:  # 确保有数据绘制饼图
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
        plt.title(f'{category} 分布')
    else:
        plt.text(0.5, 0.5, 'No Data Available', ha='center', va='center')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.savefig(f'pie_{category}.png', dpi=300)
    plt.show()