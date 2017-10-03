%% time_series测试代码
clear;
% 初始化参数：
filename='../data/time_data.xls';
index = 2;
forecastnum =5; % 要预测的个数；
lagnum =12; % 延迟个数
outputfile = '../tmp/forecast.xls';

%% 读取数据
data = xlsread(filename);
xdata=data(1:end-forecastnum,index);   % 输入的时间序列，列向量；
% xdata=xdata/1024/1024; % 转换数据格式；


%% 调用 arima 算法进行测试
[ydata,p,D,q] = time_series(xdata,forecastnum,lagnum);

disp(['ARIMA模型的p、D、q值分别为：' num2str(p) ',' num2str(D) ',' num2str(q)]);
disp(['预测值为：' num2str(ydata')]);

%% 计算误差百分比，并把数据写入文件
targetdata=data(end-forecastnum+1:end,index);
% 数据格式转换
targetdata=targetdata/1024/1024;
ydata =ydata/1024/1024;
% 计算误差
[mae_,rmse_,mape_]= cal_error(targetdata,ydata);
xlswrite(outputfile,[{'id','预测值','实际值'};...
    num2cell([[1:forecastnum]',ydata,targetdata])]);
disp(['平均绝对误差：' num2str(mae_) ', 均方根误差：' num2str(rmse_) ...
    ', 平均绝对百分误差：' num2str(mape_)]);
disp('时间序列测试完成！');