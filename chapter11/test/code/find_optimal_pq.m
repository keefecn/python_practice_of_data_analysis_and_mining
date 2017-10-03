function [pvalue,D,qvalue,bicvalue] = find_optimal_pq(xdata,lagnum)
%% 确定最佳p、d,q值

% 输入参数：
% xdata: 原始数据， 列向量
% lagnum : 延迟个数

% 输出参数：
% pvalue：AMIMA模型的p值；
% D：AMIMA模型的d值；
% qvalue：AMIMA模型的q值；

%% 初始化参数：
length_=length(xdata);
pmin=0;
pmax=round(length_/10); % 一般阶数不超过length/10
qmin=0;
qmax=round(length_/10); % 一般阶数不超过length/10

%% D 定阶
disp('正在进行D定阶...');
% xdata=detrend(xdata);  % 去趋势线
H=adftest(xdata);
D=0; % 差分阶数
original_data=xdata;
while ~H
    xdata=diff(xdata); % 差分，平稳化时间序列
    D=D+1;                   % 差分次数
    H=adftest(xdata);     % adf检验，判断时间序列是否平稳化
end

%% p、q定阶
disp('D定阶完成，正在进行p、q定阶...');
LOGL = zeros(pmax+1,qmax+1); %Initialize
PQ = zeros(pmax+1,qmax+1);

for p = pmin:pmax
    for q = qmin:qmax
        mod = arima(p,D,q);
        [~,~,logL] = estimate(mod,original_data,'print',false);
        LOGL(p+1,q+1) = logL;
        PQ(p+1,q+1) = p+q;
     end
end
% 计算BIC的值
LOGL = reshape(LOGL,(qmax+1)*(pmax+1),1);
PQ = reshape(PQ,(qmax+1)*(pmax+1),1);
[~,bic] = aicbic(LOGL,PQ+1,length_);
bic=reshape(bic,pmax+1,qmax+1);

% 构造bic、p、q矩阵
bic = construct_bic_p_q(bic);

% 按照BIC值从小到大检验残差是否符合白噪声
pvalue=-1;
qvalue=-1;
bicvalue =-1;
rows = size(bic,1);
for i= 1:rows
    if(white_noise_test(original_data,bic(i,:),D,lagnum)==1)
        bicvalue = bic(i,1);
        pvalue = bic(i,2);
        qvalue = bic(i,3);
        disp(['p值为：' num2str(pvalue) ',q值为：' num2str(qvalue),...
        ',BIC值为:' num2str(bicvalue)]);
        
        break; % 跳出for循环
    end
end
disp('p、q定阶完成！');
end

