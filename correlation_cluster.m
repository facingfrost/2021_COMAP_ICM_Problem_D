gj=csvread('data_by_artist (3) - cluster.csv')%把原始数据保存在纯文本文件 gj.txt 中
r=corrcoef(gj); %计算相关系数矩阵
d=tril(r); %取出相关系数矩阵的下三角元素
for i=1:12 %对角线元素化成零
 d(i,i)=0;
end
d=d(:);
d=nonzeros(d); %取出非零元素
d=d';d=1-d;
z=linkage(d)
dendrogram(z) 