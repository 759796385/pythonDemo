import pandas as pd
import numpy as np
#很多地方没有打印 是用了 Pycharm 的 ScientificMode
# Series 数据结构
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

# DataFrame数据结构
df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))
df
#一般使用 dict 对象来创建 DateFrame 对于每列，固定长度的每列都要一样长
df = pd.DataFrame({'A':1,
                   'B':pd.Timestamp('20130102'),
                  'C':pd.Series(1,index=list(range(5)),dtype='float32'),
                  'D':np.array([3]*5,dtype='int32'),
                   'E':pd.Categorical(['test','train','test','train','aaa']),
                   'F':'foo'})

# df.info()
# print('我是分割线')
#查看顶部数据
# print(df.head())
#查看指定底部数据
# print(df.tail(3))
#展示横向索引
# print(df.index)

#展示列名
# print(df.columns)
# 横竖转换
# print(df.T)
t = df.T

# dataFrame 的每行就是一个 Series
# print(df['E'])

#选择行 时也可以切片,行索引 列索引都行
#print(df[0:3])

df2 = df.copy()
df2['F'] = ['one','one','two','three','four']
# print(df2)
#筛选符合指定列
# print(df2[df2['F'].isin(['two','four'])])

#添加新列将根据索引自动对齐数据
s1 = pd.Series([1,2,3,4,5])
df2['G'] = s1
#使用 Numpy 数组赋值
df2['H'] = np.array([5]*len(df2))
# print(df2.info())

# 缺失值，使用 np.nan
# reindex 重建索引用于修改索引数据,返回一个副本，不对原对象影响
new = df.reindex(index=df[0:4],columns=list(df2.columns)+['E'])

# shift 列数据上下移动， period 移动幅度-正数下移负数上移，移动后空位置以 nan 填充。
#   axis 移动方向 {0, 1, ‘index’, ‘columns’} 0 index 表示上下移动  1 columns 左右移动
s = pd.Series([1,3,5,np.nan,6,8], index=list([0,1,2,3,4,5])).shift(2)

ss = s.apply(lambda x:x+1)
# dataframe 每次遍历的就是一个 Series

#数据统计
print(s.value_counts())

#
s1 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s1.str.lower())

# merge
df3 = pd.DataFrame(np.random.randn(10,4))
pieces = [df3[:3],df3[3:7],df3[7:]]
#将 series 用 concat 拼接起来
df3con = pd.concat(pieces)

#一般更适用于 sql 风格的拼接
left = pd.DataFrame({'key':['foo','foo'],'rvalx':[4,5]})
right =pd.DataFrame({'key':['foo','foo'],'rvaly':[1,2]})
# merge 笛卡尔积
merge = pd.merge(left,right,on='key')
line = pd.DataFrame({'key':['E'],'rvalx':[9],'rvaly':[10]})
#追加一行
mergeAppend = merge.append(line, ignore_index=True)

