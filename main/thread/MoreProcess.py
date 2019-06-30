# python支持多进程
import os
print('Process (%s) start..' % os.getpid())  #获取父进程id
pid = os.fork() #创建子进程 子进程和父进程都会返回一个值  父进程返回子进程id  子进程返回父进程id
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


print('---------------------上面运行了两个进程 会把此行以下代码运行两次-------------------------')
# windos上没有fork调用，在windows上没法运行
# apache就是通过fork出子进程来进行http请求

# 跨平台的多进程
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')