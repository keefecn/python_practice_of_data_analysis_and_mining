#-*- coding: utf-8 -*-
import pandas as pd

#参数初始化
inputfile1 = '../data/meidi_jd_process_end_负面情感结果.txt'
inputfile2 = '../data/meidi_jd_process_end_正面情感结果.txt'
outputfile1 = '../data/meidi_jd_neg.txt'
outputfile2 = '../data/meidi_jd_pos.txt'

data1 = pd.read_csv(inputfile1, encoding = 'utf-8', header = None) #读入数据
data2 = pd.read_csv(inputfile2, encoding = 'utf-8', header = None)

data1 = pd.DataFrame(data1[0].str.replace('.*?\d+?\\t ', '')) #用正则表达式修改数据
data2 = pd.DataFrame(data2[0].str.replace('.*?\d+?\\t ', ''))

data1.to_csv(outputfile1, index = False, header = False, encoding = 'utf-8') #保存结果
data2.to_csv(outputfile2, index = False, header = False, encoding = 'utf-8')
