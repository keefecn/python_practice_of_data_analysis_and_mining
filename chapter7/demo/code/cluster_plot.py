# -*- coding: utf-8 -*-
# 画出特征雷达图，代码接KMeans_cluster.py

def print_cluster_result(data, kmodel):
    import pandas as pd
    # 简单打印结果
    r1 = pd.Series(kmodel.labels_).value_counts()  # 统计各个类别的数目
    r2 = pd.DataFrame(kmodel.cluster_centers_)  # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)  # 横向连接（0是纵向），得到聚类中心对应的类别下的数目
    r.columns = list(data.columns) + [u'类别数目']  # 重命名表头
    print(r)
    
    # print(kmodel.cluster_centers_)  # 查看聚类中心
    # print('labels_=', kmodel.labels_)  # 查看各样本对应的类别

def plot_cluster(data, kmodel):
    import numpy as np
    import matplotlib.pyplot as plt    
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    labels = data.columns  # 标签
    k = 5  # 数据个数
    plot_data = kmodel.cluster_centers_
    color = ['b', 'g', 'r', 'c', 'y']  # 指定颜色
    
    angles = np.linspace(0, 2 * np.pi, k, endpoint=False)
    plot_data = np.concatenate((plot_data, plot_data[:, [0]]), axis=1)  # 闭合
    angles = np.concatenate((angles, [angles[0]]))  # 闭合
    
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)  # polar参数！！
    for i in range(len(plot_data)):
        ax.plot(angles, plot_data[i], 'o-', color=color[i],
                label=u'客户群' + str(i), linewidth=2)  # 画线
    
    ax.set_rgrids(np.arange(0.01, 3.5, 0.5),
                  np.arange(-1, 2.5, 0.5), fontproperties="SimHei")
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties="SimHei")
    plt.legend(loc=4)
    plt.show()
