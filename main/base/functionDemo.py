def add(a, b):
    return a + b


assert add(3, 4) == 7


def void():
    print("do")
    return


void()

if add(4, 5) > 1:
    pass


# 多返回值 返回是一个不可修改数组tuple
def moreReturn():
    return 'h', 'no'


assert moreReturn()[1] == 'no'


# 默认参数可在方法上赋值，不传为默认值 注意默认参数也是个对象引用，定义时就初试化了
def defaultArgs(a=11):
    return a


assert defaultArgs(12) == 12
assert defaultArgs() == 11


# 数组参数 加个*号即可
def handleList(*list):
    sum = 0
    for item in list:
        sum += item
    return sum


assert handleList(1, 2) == 3


#  map参数，加**
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# name: Michael age: 30 other: {'gender': 'M', 'job': 'Engineer'}
person('Michael', 30, gender='M', job='Engineer')
