#-*- coding: utf-8 -*-
# 数据规范化
import pandas as pd
import numpy as np

datafile = '../data/normalization_data.xls'  # 参数初始化
data = pd.read_excel(datafile, header=None)  # 读取数据
print(data)

data1 = (data - data.min()) / (data.max() - data.min())  # 最小-最大规范化
data2 = (data - data.mean()) / data.std()  # 零-均值规范化
data3 = data / 10 ** np.ceil(np.log10(data.abs().max()))  # 小数定标规范化
print(data1)
print(data2)
print(data3)
