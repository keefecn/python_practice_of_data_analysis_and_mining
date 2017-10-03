function [ result ] = white_noise_test(data, bic,D,lagnum )
%% 白噪声检验

% 输入数据：
% data: 原始数据集
% bic：[bic,p,q]值的组合
% D：差分阶次
% lagnum : 延迟个数

% 输出参数：
% result：是否符合白噪声检验，1表示符合，0表示不符合

%% 构建模型
mod = arima(bic(1,2),D,bic(1,3));
[EstMdl,~,~] = estimate(mod,data,'print',false);
% 计算残差
res = infer(EstMdl,data);
stdRes = res/sqrt(EstMdl.Variance); % 标准化残差
% 白噪声检验
[h,~] = lbqtest(stdRes,'lags',1:lagnum);
% 计算不符合白噪声检验的个数
hsum = sum(h);
if hsum==0;
    result =1; % 符合白噪声检验
else
    result=0; % 不符合白噪声检验
end
    
end


