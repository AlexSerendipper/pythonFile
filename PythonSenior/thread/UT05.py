""" 协程，是python中独有的，java中没有
 一个操作系统中可以有多个进程；一个进程可以有多个线程；同理，一个线程可以有多个协程。
  协程是一个特殊的函数，这个函数可以在某个地方挂起，并且可以重新在挂起处继续运行。
 Python协程适用于IO密集型任务和需要反复调用的函数。‌协程的主要优势在于它们能够有效地处理IO密集型任务，‌如磁盘IO和网络IO。‌
  由于协程只有一个线程，‌只能使用一个CPU核，‌因此它们特别适合于需要频繁等待外部资源（‌如数据库、‌网络等）‌响应的场景。‌只要出现耗时操作，就进行切换
  这种情况下，‌协程能够避免线程间的上下文切换开销，‌提高程序的执行效率。‌

【协程实现1】yield关键字实现
利用生成器函数，yield的暂停功能，实现协程的效果

【协程实现2】greenlet实现（需要下载
 g1 = greenlet(task1)           # 创建任务
 g1.switch()                    # 切换到g1协程（如果还未启动过任务，则执行任务
------------------
def task1(n):
    for i in range(n):
        g2.switch(10)                                 # 首次调用，传参
        print("正在听第{}首歌".format(i))


def task2(n):
    for i in range(n):
        g1.switch()
        print("正在搬第{}块砖".format(i))


if __name__ == '__main__':
    g1 = greenlet(task1)
    g2 = greenlet(task2)
    g1.switch(10)                                     # 首次调用，传参
------------------

【协程实现3】greenlet实现的协程是人工切换，特别麻烦，gevent模块能够在遇到耗时IO时，自动切换greenlet(因此gevent是依赖greenlet模块的，再适当的时候自动切换回来继续执行
 gevent.monkey.patch_all()                           # 因为没法检测到耗时IO，所以需要补丁，这个方法会将后续所有time.sleep()等操作视为耗时IO
 g1 = gevent.spawn(task1)                            # 创建任务并执行
 gevent.joinall([g1, g2])                            # 阻塞主进程，直到g1,g2执行结束。相当于g1.join()+g2.join()
--------------------
gevent.monkey.patch_all()
def task1(n):
    for i in range(n):
        print("正在听第{}首歌".format(i))
        time.sleep(1)


def task2(n):
    for i in range(n):
        print("正在搬第{}块砖".format(i))
        time.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(task1, 5)
    g2 = gevent.spawn(task2, 5)
    gevent.joinall([g1, g2])  # 相当于    g1.join()   g2.join()
--------------------

"""
import time

from greenlet import greenlet
import gevent
from gevent import monkey

# 线程通信(协程)示例
# def task1(n):
#     for i in range(n):
#         print("正在听第{}首歌".format(i))
#         yield None  # 只是用yield的暂停功能
#
#
# def task2(n):
#     for i in range(n):
#         print("正在搬第{}块砖".format(i))
#         yield None  # 只是用yield的暂停功能
#
#
# if __name__ == '__main__':
#     g1 = task1(10)
#     g2 = task2(10)
#
#     while True:
#         try:
#             next(g1)
#             next(g2)
#         except Exception as e:
#             break




