# 列表操作
l = ['a', 'b', 'c', 'd']

# 切片 从 0 开始取到下标 3 [start,end),第一下标是 0 可省略,到数组末尾也可省略
assert l[0:3] == l[:3]

# 第三个参数是步长
l = list(range(100))
print(l[:10:2])


# 迭代可用在 list 或 map 上，
d= {'a':1,'b':2}
for key in d:
    print(key)



