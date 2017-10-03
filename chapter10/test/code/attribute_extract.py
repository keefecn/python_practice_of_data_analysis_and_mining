#-*- coding: utf-8 -*-
#用水事件属性构造
import pandas as pd

threshold = pd.Timedelta('4 min') #阈值为分钟
inputfile = '../data/water_heater.xls' #输入数据路径,需要使用Excel格式
outputfile = '../tmp/attribute_extract.xls' #输入数据路径,需要使用Excel格式

data = pd.read_excel(inputfile)
data[u'发生时间'] = pd.to_datetime(data[u'发生时间'], format = '%Y%m%d%H%M%S')
data = data[data[u'水流量'] > 0] #只要流量大于0的记录
d = data[u'发生时间'].diff() > threshold #相邻时间作差分，比较是否大于阈值
data[u'事件编号'] = d.cumsum() + 1 #通过累积求和的方式为事件编号

data_g = data.groupby(u'事件编号')
result = pd.DataFrame()

for n,g in data_g:
  dt = pd.Timedelta(seconds=2)
  temp = pd.DataFrame(index = [0])
  tstart = g[u'发生时间'].min()
  tend = g[u'发生时间'].max()
  temp[u'用水事件时长(Min)'] = (dt + tend - tstart).total_seconds()/60
  temp[u'开关机切换次数'] = (pd.rolling_sum(g[u'开关机状态']==u'关', 2) == 1).sum()
  temp[u'总用水量(L)'] = g[u'水流量'].sum()
  tdiff = g[u'发生时间'].diff()
  if len(g[u'发生时间']) == 1:
    temp[u'总用水时长(Min)'] = dt.total_seconds()/60
  else:
    temp[u'总用水时长(Min)'] = (tdiff.sum() - tdiff.iloc[1]/2 - tdiff.iloc[len(tdiff)-1]/2).total_seconds()/60
  temp[u'平均水流量(L/min)'] = temp[u'总用水量(L)']/temp[u'总用水时长(Min)']
  result = result.append(temp, ignore_index = True)

result.to_excel(outputfile)