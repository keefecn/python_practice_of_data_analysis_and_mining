function ydata = arima_forecast(p,D,q,xdata,forecastnum)
%% ARIMA时间序列模型

% 输入参数：
% pvalue：AMIMA模型的p值；
% D：AMIMA模型的d值；
% qvalue：AMIMA模型的q值；
% xdata： 输入的时间序列，列向量；
% forecastnum： 要预测的个数；

% 输出参数：
% ydata： 预测的结果值；

Mdl = arima(p,D,q); % 创建ARIMA模型，初始化模型参数

EstMdl = estimate(Mdl,xdata); % 确定模型参数

[ydata] = forecast(EstMdl,forecastnum,'Y0',xdata);

end