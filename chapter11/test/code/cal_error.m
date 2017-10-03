function [mae_,rmse_,mape_]= cal_error(targetdata,ydata)
%% 计算误差百分比

% 输入参数：
% targetdata： 目标值；
% ydata： 模型输出值；

% 输出参数：
% mae_： 平均绝对误差；
% rmse： 均方根误差；
% mape: 平均绝对百分误差；

%% 计算误差
abs_ =abs(targetdata-ydata);
% mae
mae_=mean(abs_);
% rmse
rmse_ = mean(power(abs_,2));
% mape
mape_ = mean(abs_./targetdata);
end