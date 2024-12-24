import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
def countLv(filename):
    Lv0=0
    Lv1=0
    Lv2=0
    Lv3=0
    Lv4=0
    Lv5=0
    Lv6=0
    
        # 读取 JSON 文件内容，指定 UTF-8 编码
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in data:
        if i['VIP类型']==0:
            Lv0+=1
        elif i['VIP类型']==1:
            Lv1+=1
        elif i['VIP类型']==2:
            Lv2+=1
        elif i['VIP类型']==3:
            Lv3+=1
        elif i['VIP类型']==4:
            Lv4+=1
        elif i['VIP类型']==5:
            Lv5+=1
        elif i['VIP类型']==6:
            Lv6+=1
       
        else:
            Lv0+=1
  

    ysex = np.array([Lv0,Lv1,Lv2,Lv3,Lv4,Lv5,Lv6])
    plt.pie(ysex,labels=['Lv0','Lv1','Lv2','Lv3','Lv4','Lv5','Lv6'],textprops={'fontproperties': myfont,'fontsize':18},autopct='%1.1f%%')
    plt.title(f'{filename}等级分布',fontProperties=myfont,fontsize=24)
    plt.show()