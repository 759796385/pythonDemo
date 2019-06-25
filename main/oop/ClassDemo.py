# 也是使用class定义类 self表示实例本身,无需传递  给实例绑定属性是通过self来定义  直接定义就是类属性
class Student(object):
    staticField = '类属性'
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def info(self):
        print('name :%s score:%s' % (self.__name, self.__score))


xiaoli = Student('xiaoli', 50)
xiaoli.info()
assert xiaoli.staticField == '类属性'
# 私有属性无法直接在类外部访问 要访问还是得加getset方法

# 可通过命名逻辑来访问内部变量 _ClassName__field
print(xiaoli._Student__name)
print(xiaoli._Student__score)


class Animal(object):
    def run(self):
        print("i can run")


# 猫继承animal 并重写run方法 , run方法不能重载
class Cat(Animal):
    def eat(self):
        print("I'm like food")


cat = Cat()
cat.run()
cat.eat()

assert isinstance(cat, Animal)

# python是动态语言，无法限定传进的类型，保证有同样的方法就行了

# 获取对象类型
assert type(cat) == Cat
assert type(213) == int
assert type("dasd") == str
import types

assert type(abs) == types.BuiltinFunctionType
assert type(lambda x: x)==types.LambdaType


#获取对象所有属性和方法 使用dir()函数
print(dir(cat))
#判断是否有属性
assert hasattr(cat, '__class__')