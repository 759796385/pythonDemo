# import pandas as pd
import numpy as np
import pandas as pd

a = [['a', 1, 'ss'], ['b', 2, 'dd'], ['c', 2, 'ss'], ['d', 2, 'dd'], ['e', 4, 'ss'], ['f', 5, 'dd'], ['g', 6, 'ss'],
     ['h', 7, 'dd'], ['i', 8, 'ss'], ['k', 9, 'dd']]

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

# 按 region和value 排名 并加上第三列排名列
s = b.groupby(['value', 'type'], as_index=False).region.rank(ascending=False, method='first')
print(s)
