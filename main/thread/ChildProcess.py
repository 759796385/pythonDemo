# 子进程的控制
# 创建子进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])  # 直接在命令行运行命令
print('Exit code:', r)

# 控制子进程的输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# 进程间通信 提供 Queue、Pipes 来交换数据

from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('Process to write :%s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s to queue..' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    # 等待 write 结束
    pw.join()
    pr.terminate()
