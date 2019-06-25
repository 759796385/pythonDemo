# 函数可赋值给对象，变相给函数改名了
a = abs
assert a(-10) == 10


# 支持将函数作为参数传入函数内
def add(x, y, function):
    return function(x) + function(y)


assert add(-10, -2, abs) == 12

l = list(map(abs, [-1, -2, -3, -4, -5, -6]))


def cheng(x, y):
    return x * y


from functools import reduce

l = reduce(cheng, [1, 2, 3, 4])
print(l)

print(sorted([36, 5, -12, 9, -21], key=abs, reverse=True))


# 函数还可作为返回值，返回的函数包含了外部函数的参数，是一个独立的函数

def lazy_sum(*args):
    def sum():
        total = 0
        for item in args:
            total += item
        return total

    return sum


f = lazy_sum(1, 2, 3)
f1 = lazy_sum(1, 2, 3)
assert f != f1
print(f())


# 闭包的引用是 地址引用，因此参数会受到后续修改而变化
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

assert f1() == f2() == f3()

# 匿名函数 使用lambda关键字 不用担心命名冲突
f = lambda x: x * x
assert f(2) == 4

print(f.__name__)


# 一个增强装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 这里等同 now=log(now) 将log函数别名为now
@log
def now():
    print('2019-06-22')


now()

# functools 支持偏函数 设置参数的默认值，封装更简洁
assert int('12345', base=8) == 5349
import functools

int2 = functools.partial(int, base=2)
assert int2('1000000')==64

