# 生成器（迭代器）支持在循环过程中算出后续的元素，节省初试化时造成的大量空间占用
g = (x*x for x in range(10))
assert next(g)==0
for n in g:
    print(n)
