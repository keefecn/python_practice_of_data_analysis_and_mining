#-*- coding: utf-8 -*-
import pandas as pd
inputfile = '../data/data4.csv' #输入的数据文件
data = pd.read_csv(inputfile) #读取数据

#导入AdaptiveLasso算法，要在较新的Scikit-Learn才有。
from sklearn.linear_model import AdaptiveLasso
model = AdaptiveLasso(gamma=1)
model.fit(data.iloc[:,0:10],data['y'])
model.coef_ #各个特征的系数