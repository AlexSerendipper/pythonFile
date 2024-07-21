"""
【程序、线程、进程】见java
D:\\IdeaWorkspace\\JavaSenior\\thread\\src\\usethread\\UseThread01.java

【创建进程1】 ✔✔✔ 进程无法共享全局变量的值！！！相当于为每个进程都创建了一份全局变量！！
from multiprocessing import Process                         # 导入进程模块
 p = Process(target=task1,name='任务1',args=(1,))          # 创建子进程，将task1任务传入run方法，并指定名称（实际上python中和java一样，都是有主进程，即main进程的，并且java多线程也是重写run方法
                                                               args参数可以往task1函数中传参，要求传入可迭代对象
 p.start()                                                 # 启动进程，并且执行任务(调用run方法)
 p.terminate()                                             # 中止p进程
 p.join()                                                  # 阻塞主进程，直到子进程p结束
 os.getpid()                                               # 得到一个当前进程id
 os.getppid()                                              # 得到当前进程的父进程id

【创建进程2】继承方式创建进程
----------------
class MyProcess(Process):
    # 重新定义一个构造器，因为这里多传了一个参数进来
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        n = 1
        while True:
            time.sleep(1)
            n -= 1
            print('当前进程名为:{},n={}'.format(self.name, n))


if __name__ == '__main__':
    mp = MyProcess('zzjProcess')
    mp.start()
----------------


"""
import os
import time
from multiprocessing import Process

# 1、用于验证进程之间无法共享全局变量
num = 1

def task1(s):
    while True:
        global num
        time.sleep(s)
        num += 1
        print('task1...当前进程号为：{}，父进程号为：{},num={}'.format(os.getpid(), os.getppid(), num))


def task2(s):
    while True:
        global num
        time.sleep(s)
        num -= 1
        print('task2...当前进程号为：{}，父进程号为：{},num={}'.format(os.getpid(), os.getppid(), num))


# 一个进程休眠后，就会进入另一个进程中，进程切换就是这样的
if __name__ == '__main__':
    p1 = Process(target=task1, name='任务1', args=[1, ])
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name='任务2', args=[2, ])
    print(p2.name)
    p2.start()
    while True:
        num = num * 10
        time.sleep(2)
        print('main...当前进程号为：{},num={}'.format(os.getpid(), num))

