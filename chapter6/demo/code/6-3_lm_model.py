  # -*- coding: utf-8 -*-

import pandas as pd
from random import shuffle

datafile = '../data/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

p = 0.8  # 设置训练数据比例
train = data[:int(len(data) * p), :]
test = data[int(len(data) * p):, :]

# 构建LM神经网络模型, 
# TODO: error here, tensorflow isn't work
from keras.models import Sequential  # 导入神经网络初始化函数
from keras.layers.core import Dense, Activation  # 导入神经网络层函数、激活函数

netfile = '../tmp/net.model'  # 构建的神经网络模型存储路径

net = Sequential()  # 建立神经网络
net.add(Dense(input_dim=3, output_dim=10))  # 添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Activation('relu'))  # 隐藏层使用relu激活函数
net.add(Dense(input_dim=10, output_dim=1))  # 添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid'))  # 输出层使用sigmoid激活函数
net.compile(loss='binary_crossentropy', optimizer='adam',
            class_mode="binary")  # 编译模型，使用adam方法求解

net.fit(train[:, :3], train[:, 3], nb_epoch=1000, batch_size=1)  # 训练模型，循环1000次
net.save_weights(netfile)  # 保存模型

predict_result = net.predict_classes(
    train[:, :3]).reshape(len(train))  # 预测结果变形
'''这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n'''

from plot import *  # 导入自行编写的混淆矩阵可视化函数
plot_cm(train[:, 3], predict_result).show()  # 显示混淆矩阵可视化结果

# show ROC
predict_result = net.predict(test[:, :3]).reshape(len(test))
plot_roc(test, predict_result, 'ROC of LM')
