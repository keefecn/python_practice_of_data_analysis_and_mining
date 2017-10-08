# -*- coding: utf-8 -*-
# K-Means聚类算法

import pandas as pd
from sklearn.cluster import KMeans  # 导入K均值聚类算法

inputfile = '../tmp/zscoreddata.xls'  # 待聚类的数据文件
k = 5  # 需要进行的聚类类别数，需结合业务的理解和分析来确定客户的类别数量

# 读取数据并进行聚类分析
data = pd.read_excel(inputfile)  # 读取数据

# 调用k-means算法，进行聚类分析
# TODO: error here
# n_jobs是并行数，一般等于CPU数较好 , window下多进程 跑失败
kmodel = KMeans(n_clusters=k, n_jobs=1)  
kmodel.fit(data)  # 训练模型

from cluster_plot import print_cluster_result, plot_cluster
print_cluster_result(data, kmodel)
plot_cluster(data, kmodel)
print('END')
