#-*- coding: utf-8 -*-
import numpy as np
import pandas as pd
inputfile = '../data/data1.csv' #输入的数据文件
data = pd.read_csv(inputfile) #读取数据
np.round(data.corr(method = 'pearson'), 2) #计算相关系数矩阵，保留两位小数