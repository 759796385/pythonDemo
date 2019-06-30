# 本地线程变量
import threading

local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello,%s ( in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


#进程还是 线程？
#多进程优点稳定性高：子进程崩溃了不会影响其它进程  缺点是*nix fork 还行，windows 下开销太大，进程数有限
#多线程稍微轻一点，但任一个线程崩溃都会造成整个进程崩溃

#有限使用进程，进程可以分布式到不同机器