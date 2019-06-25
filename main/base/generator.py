# 生成器 支持在循环过程中算出后续的元素，节省初试化时造成的大量空间占用
g = (x*x for x in range(10))
assert next(g)==0
#for n in g:
#    print(n)

# yield 关键字，带记忆的return，将函数变为生成器，每次调用next从上次yield退出地执行
def func():
    print(1)
    yield '第一次next返回值'
    print(2)
    yield '第二次next返回值'
    print(3)
    yield '第三次next返回值'

f = func()
#print(next(f))
#print(next(f))
#print(next(f))
# 需要执行三次next 才能执行完整个生成器
for x in func():
    print(x)