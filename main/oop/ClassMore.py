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
# s.address = "dsada" 执行报错~~

# @property装饰器负责把一个方法变成属性调用. @score.setter 负责把一个setter方法变成属性赋值
class Man(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value >100:
            raise ValueError('score must be range!')
        self._score = value
# age
    @property
    def age(self):
        return 21

s = Man()
s.score = 100
assert s.age==21


