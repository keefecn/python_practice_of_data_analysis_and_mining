function bic_p_q = construct_bic_p_q(bic)
%% 根据bic构造bic_p_q矩阵，同时按照bic的值按行从小到大排列

% 输入参数：
% bic ： bic矩阵

% 输出参数：
% bic_p_q ： 构造的bic矩阵；

[rows,cols]= size(bic);

bic_p_q = zeros(rows*cols,3); % [bic,p,q]
for i=1:rows
   for j=1:cols
      bic_p_q((i-1)*rows+j,:)=[bic(i,j),i-1,j-1]; 
   end
end

% 排序
[~,index] = sort(bic_p_q(:,1));
bic_p_q = bic_p_q(index,:);

end