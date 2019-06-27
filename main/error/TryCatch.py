import logging
try:
    print('start try')
    r =231/0
    print('do nothing')
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except',e)
    logging.exception(e)
#当没有异常发生 执行else
else:
    print('no error!')
finally:
    print('finally')
print('end')

#python的异常都继承自BaseException

class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')