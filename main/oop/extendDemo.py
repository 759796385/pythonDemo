# python支持多继承  需要啥父类 就在类括号里加上就行
# 对应提供继承方法的类 一般加上MixIn后缀


# 重写str方法 等同java的tostring
class Student(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'student name:%s' % self._name


print(Student('doudou'))


# 实现自定义迭代器 实现__iter__()方法：返回一个可迭代对象。 for循环会不断调用迭代对象的__next__方法拿到下一个值
# 如果要像list一样获取指定下标元素 得实现__getitem__()方法
class DiyIterator(object):
    def __init__(self):
        self._num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._num += 10
        if self._num > 100:
            raise StopIteration()
        return self._num

    def __getitem__(self, item):
        if isinstance(item, int):
            return 10 * (item + 1)
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            L = []
            for x in range(stop):
                if x >= start:
                    L.append((x + 1) * 10)
            return L

    # __getattr__方法可让访问不存在属性时，动态返回一个属性
    def __getattr__(self, attr):
        if attr == 'abc':
            return 99

    # 实例本身作为一个方法调用用 __call__
    def __call__(self):
        print('hhahah')


for n in DiyIterator():
    print(n)

d = DiyIterator()
assert 100 == d[9]
print(d[5:10])

assert d.abc == 99
d()

# 可通过callable()函数 判断一个对象是否是可调用对象
assert callable(d())
assert callable(max) 
