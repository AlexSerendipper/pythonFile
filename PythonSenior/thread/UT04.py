""" 线程通信
【队列queue】
 进程间的通信的通过队列实现 from multiprocessing import Queue
 线程间的通信也是通过队列来实现 import queue
  线程间的通信通常可以称为，生产者和消费者
 queue模块中提供了同步的、线程安全的队列类，包裹FIFO(先入先出)的队列Queue
  LIFO(先入后出)的队列LifoQueue和优先级队列 PriorityQueue。这些队列都使用了锁，
  因此可以在多线程中直接使用，即可以使用队列来实现线程间的同步

【线程通信】
 线程间通信同样也是利用为两个线程传入同一个队列，利用队列的阻塞特性实现线程间的通信
 q = queue.Queue(maxsize=3)
 q.put(val, timeout=2)  # 往队列中存值，如果队列满了则阻塞等待，这里设置超时时间，如果超过2s则报错
 q.get(timeout=2)       # 每次取出一个队列中的值，先进先出，如果队列空了则阻塞等待
 q.full()               # 判断队列是否已满
 q.empty()              # 判断队列是否为空
 q.join()               # 队列中所有的元素都被接收和处理完毕之前，主线程会一直阻塞（因此，通常q.task_done的调用次数，是与队列中元素的个数一致的
 q.task_done            # 当消费者中，所有任务都被处理并且通过queue.task_done()标记为完成时，‌q.join()方法会解除阻塞状态
"""

import queue
import threading
import time


def producer(q):
    images = ["11.jpg", "22.png", "33.jpg", "44.jpg", "55.jpg"]
    for image in images:
        q.put(image)
        print("正在下载{}".format(image))
        time.sleep(1)
    q.put(None)


def consumer(q):
    while True:
        image = q.get(timeout=2)
        q.task_done()
        if image is None:
            print("保存结束")
            break
        print("{}保存成功".format(image))
        time.sleep(3)


if __name__ == '__main__':
    q = queue.Queue(maxsize=3)
    p1 = threading.Thread(target=producer, args=(q,))
    p2 = threading.Thread(target=consumer, args=(q,))
    p1.start()
    p2.start()

    p1.join()  # 阻塞主进程，这里也就是只有生产结束了，程序才会往下走！
    q.join()  # 只有队列中所有的元素都已经被标记为已处理，即都被q.task_done()标记了，程序才会往下走
    print("all done")
