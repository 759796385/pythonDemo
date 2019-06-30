from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name,os.getpid()))
    start =time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end-start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) #建立一个大小为4的进程池，超过就等待  默认大小cpu核心数
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done ...')
    p.close()# close之后就不能加新的进程了
    p.join()
    print('All subprocess done')

