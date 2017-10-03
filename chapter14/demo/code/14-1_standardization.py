#-*- coding: utf-8 -*-
#数据标准化到[0,1]
import pandas as pd

#参数初始化
filename = '../data/business_circle.xls' #原始数据文件
standardizedfile = '../tmp/standardized.xls' #标准化后数据保存路径

data = pd.read_excel(filename, index_col = u'基站编号') #读取数据

data = (data - data.min())/(data.max() - data.min()) #离差标准化
data = data.reset_index()

data.to_excel(standardizedfile, index = False) #保存结果