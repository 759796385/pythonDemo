from collections import namedtuple

# nametuple是 创建自定义tuple对象，规定元素个数，方便使用对象而不是使用下标来调用
Point = namedtuple('Location', ['x', 'y'])
p = Point(1, 2)
assert p.x == 1 and p.y == 2
assert isinstance(p,tuple)

#deque 双端队列
# defaultdict 当获取key不存在时返回一个默认值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['abc'] = 'abc'
assert dd['key2'] == 'N/A'

#排序的map 按插入排序排序
from collections import OrderedDict
od = OrderedDict([('a', 1), ('c', 2), ('b', 3)])
print(od)

#