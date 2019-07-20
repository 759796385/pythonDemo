import pandas as pd
import numpy as np

# DataFrame（x轴，y轴）
left = pd.DataFrame({'logistics_code': [], 'sku_code': [], 'inventory': []})
right = pd.DataFrame({'warehouse_code': ['1011', '1011', '1011'], 'area': ['华北', '华北', '华北'],
                      'sku_code': ['30010001', '30010010', '30010100'], 'logistics_sku_status': ['01', '02', '03'],
                      'start_date': ['2019-07-18', '2019-07-18', '2019-07-18']})

print(left.info())
print('我是分割线')
print(right.info())
# 合并
region_warehouse_inv = left.merge(right, left_on=['logistics_code', 'sku_code'],
                                  right_on=['warehouse_code', 'sku_code'])
print('------------mergerResult \n', region_warehouse_inv)
# 按指定列分组聚合，输出一个矩阵，as_index =false 保留分组列索引
region_warehouse_inv = region_warehouse_inv.groupby(['area', 'sku_code'], as_index=False).inventory.sum()
print('------------sumResult \n', region_warehouse_inv)
# as_index = true 行索引被取消
# sumResult1 = region_warehouse_inv.groupby(['area','sku_code'], as_index= True).inventory.sum()
# print('------------sumResult true \n',sumResult1)
# 给列名 重新赋值
if len(region_warehouse_inv.columns) == 0:
    region_warehouse_inv = pd.DataFrame({'region': [], 'sku_code': [], 'warehouse_inventory': []})
else:
    region_warehouse_inv.columns = ['region', 'sku_code', 'warehouse_inventory']
region_warehouse_inv.info()
print(region_warehouse_inv)

# drop_duplicates
df = pd.DataFrame({'a': [1, 2, 3, 2, 1], 'b': ['c', 'b', 'b', 'b', 'a']})
# 对ab行相同的去重， inplace表示是否在原来DataFrame基础上修改， keep表示重复数据取哪一条
df.drop_duplicates(['a','b'],inplace=True,keep='first')
print(df)
