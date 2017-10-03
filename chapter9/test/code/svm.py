#-*- coding: utf-8 -*-
import pandas as pd

inputfile = '../data/moment.csv' #数据文件
outputfile1 = '../data/cm_train.xls' #训练样本混淆矩阵保存路径
outputfile2 = '../data/cm_test.xls' #测试样本混淆矩阵保存路径
data = pd.read_csv(inputfile, encoding = 'gbk') #读取数据，指定编码为gbk
data = data.as_matrix()

from numpy.random import shuffle #引入随机函数
shuffle(data) #随机打乱数据
data_train = data[:int(0.8*len(data)), :] #选取前80%为训练数据
data_test = data[int(0.8*len(data)):, :] #选取前20%为测试数据

#构造特征和标签
x_train = data_train[:, 2:]*30
y_train = data_train[:, 0].astype(int)
x_test = data_test[:, 2:]*30
y_test = data_test[:, 0].astype(int)

#导入模型相关的函数，建立并且训练模型
from sklearn import svm
model = svm.SVC()
model.fit(x_train, y_train)

#导入输出相关的库，生成混淆矩阵
from sklearn import metrics
cm_train = metrics.confusion_matrix(y_train, model.predict(x_train))
cm_test = metrics.confusion_matrix(y_test, model.predict(x_test))
pd.DataFrame(cm_train, index = range(1, 6), columns = range(1, 6)).to_excel('cm_train.xls')
