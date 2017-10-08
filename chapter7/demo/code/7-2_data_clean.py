#-*- coding: utf-8 -*-
# 数据清洗，过滤掉不符合规则的数据

import pandas as pd

datafile = '../data/air_data.csv'  # 航空原始数据,第一行为属性标签
cleanedfile = '../tmp/data_cleaned.csv'  # 数据清洗后保存的文件
cleanedfile2 = '../tmp/data_cleaned.xls' 

# 读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
data = pd.read_csv(datafile, encoding='utf-8')

# NOTE: * instead of &
data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()
            ]  # 票价非空值才保留

# 只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)  # 该规则是“与”
data = data[index1 | index2 | index3]  # 该规则是“或”

# to_csv
data.to_csv(cleanedfile, encoding='utf-8')  # 导出结果
data.to_excel(cleanedfile2)
print('END')
