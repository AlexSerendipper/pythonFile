""" 进程池
【进程池】如果有成百上千个进程，手动创建就会非常麻烦，因此使用进程池的概念
 注意，进程池的存活依赖于主进程！！所以需要阻塞主进程，让所有的子进程完成任务
 阻塞式进程池：添加一个任务执行一个，任务执行完成后才创建下一个任务（没有特别大的意义）
 非阻塞式进程池：将任务全部添加（直到线程池占满），任务完成立刻返回结果并调取回调函数，占用进程被释放立刻用于执行新任务
from multiprocessing import Pool
 p = Pool(num)                                # 创建进程池，并且容量为num
 p.apply_async(task1,args=(),callback)        # 非阻塞式进程池：传入任务，任务参数(元组形式，以及回调函数
                                                 回调函数会在每个子进程任务结束后自动调用，子任务的返回值作为回调函数的参数
 p.apply(task1,args=())                       # 阻塞式进程池，没有回调函数
 pool.close()                                 # 关闭进程池（pool），使其不在接受新的任务。
 pool.join()                                  # 阻塞主进程，直到所有子进程结束

【进程间通信】示例见下
from multiprocessing import Queue
 进程间通信主要就是利用为两个进程传入同一个队列，利用队列的阻塞特性实现线程间的通信
 q = Queue(maxsize=3)
 q.put(val, timeout=2)  # 往队列中存值，如果队列满了则阻塞等待，这里设置超时时间，如果超过2s则报错
 q.get(timeout=2)       # 每次取出一个队列中的值，先进先出，如果队列空了则阻塞等待
 q.full()               # 判断队列是否已满
 q.empty()              # 判断队列是否为空

"""
import os
import time
from multiprocessing import Pool, Queue, Process


# 1、进程池，可以看见当池中任务结束才放入新任务
# def task(task_name):
#     print("开始做任务：{}".format(task_name))
#     start = time.time()
#     time.sleep(2)
#     end = time.time()
#     print("做{}任务，花了{},进程id为{}".format(task_name, start - end,os.getpid()))
#     return task_name
#
#
# tasks = []
#
#
# def callback_func(tn):
#     tasks.append(tn)  # 每个子进程任务结束后自动调用，子任务的返回值作为回调函数的参数
#
#
# if __name__ == '__main__':
#     pool = Pool(2)
#     task_names = ["吃饭", "喝酒", "睡觉", "聊天"]
#     for task_name1 in task_names:
#         pool.apply_async(task, args=(task_name1,),callback=callback_func)
#
#     pool.close()
#     pool.join()
#     print(tasks)
#
#     pool2 = Pool(2)
#     task_names = ["吃饭", "喝酒", "睡觉", "聊天"]
#     for task_name1 in task_names:
#         pool2.apply(task, args=(task_name1,))
#
#     pool2.close()
#     pool2.join()
#     print("over")

# 2、线程间通信
def download(q):
    images = ["11.jpg", "22.png", "33.jpg"]
    for image in images:
        q.put(image)
        print("正在下载{}".format(image))
        time.sleep(2)


def save(q):
    while True:
        try:
            image = q.get(timeout=2)
            print("{}保存成功".format(image))
        except:
            print("保存结束")
            break



if __name__ == '__main__':
    q = Queue(3)
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=save,args=(q,))
    p1.start()
    p2.start()
    p1.join()