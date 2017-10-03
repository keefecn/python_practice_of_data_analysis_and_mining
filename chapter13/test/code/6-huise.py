#-*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
import pandas as pd
from GM11 import GM11 #引入自己编写的灰色预测函数

x0 = np.array([3152063, 2213050, 4050122, 5265142	,5556619, 4772843,	9463330])
f, a, b, x00, C, P = GM11(x0)
print(u'2014年、2015年的预测结果分别为：\n%0.2f万元和%0.2f万元' %(f(8), f(9)))
print(u'后验差比值为：%0.4f' %C)
p = pd.DataFrame(x0, columns = ['y'], index = range(2007, 2014))
p.loc[2014] = None
p.loc[2015] = None
p['y_pred'] = [f(i) for i in range(1,10)]
p['y_pred'] = p['y_pred'].round(2)
p.index = pd.to_datetime(p.index, format='%Y')

import matplotlib.pylab as plt
p.plot(style=['b-o','r-*'], xticks = p.index)
plt.show()