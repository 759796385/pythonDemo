utf8encode = '中文'.encode('utf-8')
utf8decode = utf8encode.decode('utf-8')
# print(utf8decode)

# 格式化字符串
# print('age : %s ,gender: %s' % (23,'男'))

# list
list = ['a', 'b', 'c']

assert len(list) == 3

assert list[1] == 'b'
assert list[-1] == 'c'

# 不可修改数组 tuple 用括号表示
unmodify = (1, 2)

# 条件语句
age = 24
if age >= 12:
    print('childen')
else:
    print('baby')

# 循环
for item in list:
    print(item)

# dict（map） 用大括号定义,和 hashmap 一样的实现
map = {
    'age': 12,
    'name': 'ada'
}
print(map['age'])

# set 集合 就是 hashSet
s = set([1, 3, 3])
s.add(3)
assert len(s) == 2

