gj=csvread('data_by_artist (3) - cluster.csv')%��ԭʼ���ݱ����ڴ��ı��ļ� gj.txt ��
r=corrcoef(gj); %�������ϵ������
d=tril(r); %ȡ�����ϵ�������������Ԫ��
for i=1:12 %�Խ���Ԫ�ػ�����
 d(i,i)=0;
end
d=d(:);
d=nonzeros(d); %ȡ������Ԫ��
d=d';d=1-d;
z=linkage(d)
dendrogram(z) 