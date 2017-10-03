function [ydata,p,D,q] = time_series(xdata,forecastnum,lagnum)
%% 使用ARIMA模型进行时序预测

% 输入参数：
% xdata： 输入的时间序列，列向量；
% forecastnum： 要预测的个数；
% lagnum：延迟个数；

% 输出参数：
% ydata： 预测的结果值；


%% 确定最佳p、q值
[p,D,q,~] = find_optimal_pq(xdata,lagnum);

%% 使用arima模型进行预测
ydata = arima_forecast(p,D,q,xdata,forecastnum);





end