# coding=utf-8
import pandas as pd
import numpy as np

df = pd.DataFrame({'key': ['foo', 'foo', 'a'], 'rvalx': [4, 5, 4], 'rvaly': [2, 3, 5]})
# 分組 每組求和 聚合的 key 还是单独作为一列 as_index
gourp = df.groupby('key', as_index=False).sum()
# 按多列分组
groupMore = df.groupby(['key', 'rvalx'], as_index=False).sum()

# 重塑 没看懂有啥用
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df1 = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df1[:4]
#将二维的压缩成一维的  对应解压时 unstack
stacked = df2.stack()

# 透视 从不同维度来解析数据
ts = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                 'B' : ['A', 'B', 'C'] * 4,
                       'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                       'D' : np.random.randn(12),
                      'E' : np.random.randn(12)})
# AB 为索引，C 为列 ，值是 D 列
ts1 = pd.pivot_table(ts, values='D', index=['A', 'B'], columns=['C'])

#分类 对内容进行对应转换
df3 = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
df3["grade"] = df3["raw_grade"].astype("category")
#将类别重命名
df3["grade"].cat.categories = ["very good", "good", "very bad"]
# 将类别重新排序
