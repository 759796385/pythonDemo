import os
assert os.name == 'posix' #系统是*nix

print(os.uname()) # 系统详细信息
print(os.environ) #系统环境变量


print(os.path.abspath('.')) #获取当前文件绝对路径

#当前目录下所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 序列化使用pickle模块 序列化后放到文件里
import pickle
d = dict(name='ab',age=22)
s = pickle.dumps(d)
print(s)


#json
import json
jsonstr = json.dumps(d)
#解析json
h  = json.loads(jsonstr)
print(h)

#解析对象 需要写一个专门的转换器  太麻烦了
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        s = Student('Bob', 20, 88)
