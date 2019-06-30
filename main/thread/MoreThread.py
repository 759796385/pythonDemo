# 使用高级模块 threading  启动和 Process 一样
import time, threading


def loop():
    print('thread %s is running ....' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >> %s ' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)


print('thread %s is running .. ' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s end' % threading.current_thread().name)

# 和 java 类似 ，线程中变量共享，进程中同一变量各自拷贝
# 同 java 的 synchnied ，python 提供 loca来实现锁
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

#一个线程只能占满一个内核
#python 有点坑的是，多个线程实质只是交替串行执行，最多使用一个核，无法达到多核效果


