#ARIMA时序模型
import pandas as pd
import numpy as np
import math
from numpy import array
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

forecastnum = 5
df = pd.read_csv("F:\\test.csv", encoding='gbk') 

def cal_avg(x):
    rows = x.index.size  # 行
    cols = x.columns.size  # 列
    x = x.apply(lambda x: x)
  
    x = array(x)
    nums=[0 for i in range(100)]
    w = [0 for i in range(100)]

    for i in range(0, rows):
        year=int(x[i][1]-1921)
        w[year]+=x[i][0]
        nums[year]+=1

    for i in range(100):
        if nums[i]==0:
            continue
        else :
            w[i]=w[i]/nums[i]
    
    return w

if __name__ == '__main__':
    x=[i for i in range(1921,2021)]
    j=0
    w=cal_avg(df)
   
    for i in range(100): 
        if w[j]==0:
            del w[j]
            del x[j]
        else:
            j+=1

    w = pd.DataFrame(w,index=x)
    w.columns = ['danceability']
    w.plot(label=u'danceability')
    plt.legend()
    plt.show
    
    
    from statsmodels.graphics.tsaplots import plot_acf #自相关图
    plot_acf(w).show()
    
    #ADF单位根检验
    from statsmodels.tsa.stattools import adfuller as ADF
    print(u'原始序列的ADF检验结果为：',ADF(w[u'danceability']))
    
    #差分
    D_data = w.diff().dropna() #差分
    D_data.columns = [u'Diff']
    D_data.plot() #时序图
    plt.show()
 
    plot_acf(D_data).show() #自相关图
 
    from statsmodels.graphics.tsaplots import plot_pacf
    plot_pacf(D_data).show() #偏自相关图
 
 



