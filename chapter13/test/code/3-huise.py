#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from GM11 import GM11 #引入自己编写的灰色预测函数

inputfile = '../data/data3.csv' #输入的数据文件
outputfile = '../tmp/data3_GM11.xls' #灰色预测后保存的路径
data = pd.read_csv(inputfile) #读取数据
data.index = range(1999, 2014)

data.loc[2014] = None
data.loc[2015] = None
l = ['x3', 'x4', 'x6', 'x8']
for i in l:
  f = GM11(data[i][range(1999, 2014)].as_matrix())[0]
  data[i][2014] = f(len(data)-1) #2014年预测结果
  data[i][2015] = f(len(data)) #2015年预测结果
  data[i] = data[i].round() #取整

data[l+['y']].to_excel(outputfile) #结果输出