# -*- coding: utf-8 -*
import numpy as np #一般以np作为numpy的别名
a = np.array([2, 0, 1, 5]) #创建数组
print(a) #输出数组
print(a[:3]) #引用前三个数字（切片）
print(a.min()) #输出a的最小值
a.sort() #将a的元素从小到大排序，此操作直接修改a，因此这时候a为[0, 1, 2, 5]
b= np.array([[1, 2, 3], [4, 5, 6]]) #创建二维数组
print(b*b) #输出数组的平方阵，即[[1, 4, 9], [16, 25, 36]]
