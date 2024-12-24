import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
def countsex(filename):
# 指定文件名
   
    man=0
    women=0
    nonsex=0
    # 读取 JSON 文件内容，指定 UTF-8 编码
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        if i['性别']=='男':
            man+=1
        elif i['性别']=='女':
            women+=1
        else:
            nonsex+=1
 

    ysex = np.array([man,women,nonsex])
    plt.pie(ysex,labels=['男','女','未知'],textprops={'fontproperties': myfont,'fontsize':18},autopct='%1.1f%%')
    plt.title(f'{filename}性别分布',fontProperties=myfont,fontsize=24)
    plt.show()