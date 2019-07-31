# coding=utf-8
import numpy as np
import pandas as pd

a = [['a', 1, 'aa'], ['b', 2, 'bb'], ['c', 2, 'cc'], ['d', 2, 'dd'], ['a', 4, 'aa'], ['b', 5, 'bb'], ['c', 6, 'cc'],
     ['d', 7, 'dd'], ['a', 8, 'aa'], ['b', 9, 'bb']]

b = pd.DataFrame(a, columns=['region', 'value', 'type'])
# method : {‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}
#              average: average rank of group
#              min: lowest rank in group
#              max: highest rank in group
#              first: ranks assigned in order they appear in the array 排名由数组中下标决定，即使同一阶人再多，也有先后
#              dense: like ‘min’, but rank always increases by 1 between groups  每个阶段差只有1，哪怕这一阶人再多
#   ascending  false 1最高
# print(b["value"].rank(ascending =False,method='first'))

# 每个阶段差只有1，哪怕这一阶人再多
# print(b["value"].rank(ascending =False,method='dense'))

# 按 region和type 排名 并加上第三列排名列, 对应操作的列，如果是数学运算 一定要是数字
newCol = b.groupby(['region', 'type'], as_index=False).value.rank(ascending=False, method='first')
b['rank'] = newCol.reset_index(level=0, drop=True)

df = pd.DataFrame([[False, 1], [True, 2], [False, 3]], columns=['column', 'another_column'])


def function(x):
    return x.column == False


df['add'] = df.apply(function, axis=1)

t = pd.DataFrame({'column': [True,False], '翻译': ['真', '假']})
new =pd.merge(df,t,on='column',how='left')
