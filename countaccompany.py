import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
a=[]
b=[]

def countaccompany(filename):
# 指定文件名
   

    # 读取 JSON 文件内容，指定 UTF-8 编码
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        a.append(i['排名'])
        b.append(i['陪伴天数'])
    x = np.array(a)
    y = np.array(b)

    plt.scatter(x,y)
    plt.title(f'{filename}大航海陪伴天数分布',fontProperties=myfont,fontsize=24)
    plt.show()