# 动态给实例添加方法 和 属性
class Student(object):
    pass


student1 = Student()
student1.name = 'xiaoli'
assert student1.name == 'xiaoli'


def set_age(self, age):
    self.age = age


# 动态添加方法
from types import MethodType

student1.set_age = MethodType(set_age, student1)
student1.set_age(12)
assert student1.age == 12

# 也可给class绑定方法,对所有实例起效
Student.set_age = set_age

#如果想限制实例能添加哪些属性 配置__slots__ 但无法对继承子类起作用
class SomeField(object):
    __slots__ = ('name','age')

s =SomeField()
# s.address = "dsada" 执行报错
