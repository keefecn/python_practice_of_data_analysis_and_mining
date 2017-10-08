#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt  

def plot_cm(y, yp):

    from sklearn.metrics import confusion_matrix  # 导入混淆矩阵函数
    cm = confusion_matrix(y, yp)  # 混淆矩阵

    plt.matshow(cm, cmap=plt.cm.Greens)  # 画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
    plt.colorbar()  # 颜色标签

    for x in range(len(cm)):  # 数据标签
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(
                x, y), horizontalalignment='center', verticalalignment='center')

    plt.ylabel('True label')  # 坐标轴标签
    plt.xlabel('Predicted label')  # 坐标轴标签
    return plt

def plot_roc(test, predict_result, label_name):
    
    from sklearn.metrics import roc_curve  # 导入ROC曲线函数
    
    fpr, tpr, thresholds = roc_curve(
        test[:, 3], predict_result, pos_label=1)
    plt.plot(fpr, tpr, linewidth=2, label='ROC of CART', color='green')  # 作出ROC曲线
    plt.xlabel('False Positive Rate')  # 坐标轴标签
    plt.ylabel('True Positive Rate')  # 坐标轴标签
    plt.ylim(0, 1.05)  # 边界范围
    plt.xlim(0, 1.05)  # 边界范围
    plt.legend(loc=4)  # 图例
    plt.show()  # 显示作图结果    
    return plt