""" 多线程（python中多线程和多进程是几乎一样的步骤
【创建线程1】线程类创建线程
 区别于非阻塞式进程池，线程是靠调度算法抢占进程资源的。。。并且多线程是指在同一进程内，‌多个线程并发执行。
  ‌✔✔ 每个线程都拥有自己的执行栈和局部变量，‌但共享进程的全局变量、‌静态变量等资源。‌
  这意味着，‌多进程在执行不同任务时更加稳定，‌而多线程在处理大量数据或执行密集计算任务时可能会因为一个线程的问题而影响其他线程的执行
  并且进程间通信‌需要额外的同步和互斥手段来保证数据的一致性，‌而线程间可以直接读写进程数据段进行通信，‌无需额外的通信机制

import threading
 t = threading.Thread(target=task1,name='任务1',args=(1,))          # 创建子线程，将task1任务传入run方法，并指定名称（实际上python中和java一样，都是有主线程，即main线程的，并且java多线程也是重写run方法
                                                                       args参数可以往task1函数中传参，要求传入可迭代对象
 t.start()                                                 # 启动进程，并且执行任务(调用run方法)
 t.join()                                                  # 阻塞主线程，直到子线程p结束
 os.getpid()                                               # 得到一个当前进程id
 os.getppid()                                              # 得到当前进程的父进程id

【多线程同步问题】
 当多个线程操作共享数据时，一个线程还没有执行完，另一个线程参与进来执行。导致共享数据的错误，即为同步问题。
  不同于java需要手动加同步监视器！！！
  python中，只要使用了线程，默认都会加锁GIL（Global Interpreter Lock），也即默认不会出现多线程的同步问题，也就是python的多线程并不是真正的多线程
 GIL锁有一个特点，GIL会在解释器不间断运行了运行15毫秒‌后，‌该线程也会放弃GIL！！也即当计算量太大，也会出现多线程的同步问题
  为了解决GIL锁的缺陷，threading类同样支持人工加锁
----------------
lock = threading.Lock()                  # 得到锁对象
lock.acquire()                           # 请求得到锁，如果请求时锁对象被线程占用，则阻塞等待
....                                     # 产生同步问题的
lock.release()                           # 释放锁
----------------

【创建线程2 & 死锁问题】继承方式创建线程，python中继承方式创建线程和进程几乎是一样的
 当同时开启如下两个线程，就会发生经典死锁
 为了避免死锁，可以设置 lock.acquire(timeout=5) 超时时间，超时后会释放锁
----------------
lock1 = threading.Lock()
lock2 = threading.Lock()
class MyThread1 (Thread):
    # 重写run方法
    def run(self):
        if lock1.acquire():
            print(self.name + '获取了A锁')               # 这里没有像自定义线程那样重写__init__方法并传入name。因此这里会自动赋值一个线程名给name属性
            if lock2.acquire():
                print(self.name + '获取了B锁')
            lock2.release()
        lock1.release()

class MyThread2 (Thread):
    # 重写run方法
    def run(self):
        if lock2.acquire():
            print(self.name + '获取了B锁')
            if lock1.acquire():
                print(self.name + '获取了A锁')
            lock1.release()
        lock2.release()
----------------

"""
import threading
ticket = 0
lock = threading.Lock()


def sell_ticket():
    lock.acquire()
    global ticket
    for i in range(10000000):
        ticket -= 1
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=sell_ticket(), name="th1")
    t2 = threading.Thread(target=sell_ticket(), name="th2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()

print(ticket)
