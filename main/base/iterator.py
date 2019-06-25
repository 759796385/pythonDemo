# 集合对象属于 能用for循环的 Iterable
from collections.abc import Iterable
assert isinstance({},Iterable)
assert isinstance('abc', Iterable)
assert isinstance(range(100),Iterable)

# 生成器这种能用next 属于Iterator