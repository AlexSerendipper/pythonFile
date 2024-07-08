""" 生成器和迭代器
集合推导式也差不多
list1 = [1,1,2,3,4,5]
{x+2 for x in list1 if x>=1}        结果就会把list1的元素取出来加2放到set中，即完成去重

字典推导式
result = {value:key for key,value in dict1.item}         结果就会把key和字典颠倒


【生成器概述】
通过列表生成式(列表推导式)，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢?这样就不必创建完整的list。
从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器:generator

【得到生成器的方式】
1. 用列表推导式得到生成器
   把列表推导式的外层换成小括号
g1 = (表达式 for x in range())
   g1.__next__()                         # 调用一次打印一个元素，依次产生
   next(g1)                                相同功能，next为内置函数，如果超出了产生的范围，则抛出异常StopIteration
   g1.send(None)                         # 调用一次打印一个元素，并往生成器中传值。使用前必须先send一个None值。因为yield相当于直接return，然后暂停
    g1.send('value')                      # 第二次调用时，将value赋值给yield所赋值的元素

2. 利用函数得到生成器
# 只要函数中出现yield关键字，函数就变成生成器了
# 调用函数，接收调用的结果就是生成器。继而使用next函数即可
def func()
   n = 0
   while True:
        n += 1
        yield n                            # 生成器标志，实际上调用时运行到这里就会return，下一次调用从这里开始
   return xxx                              # 当生成器结束了，返回的提示可以写在这
                                             即如果超出限制还在调用，返回该提示信息

【生成器的应用】线程通信(多个任务之间的切换)


"""

# 利用生成器产生斐波那契数列
def func(len):
    a = 0
    b = 1
    for i in range(len):  # 产生八个数
        yield b
        a, b = b, a + b  # b的值给a作为上一个数，a+b的值赋值给b，作为当前的数
    return '结束了'  # 当生成器结束了，返回的提示可以写在这
    # 即如果超出限制还在调用，返回该提示信息


g1 = func(8)
n = 0
while n < 8:
    print(next(g1))
    n = n + 1


# g1.send的使用, 可以断点查看
def gen():
    i = 0
    while i < 10:
        temp = yield i
        print('temp：', temp)
        i += 1
    return '结束了'


g2 = gen()
g2.send(None)
g2.send('敏敏')
g2.send('健健')


# 线程通信示例
def task1(n):
    for i in range(n):
        print("正在听第{}首歌".format(i))
        yield None  # 只是用yild的暂停功能


def task2(n):
    for i in range(n):
        print("正在搬第{}块砖".format(i))
        yield None  # 只是用yild的暂停功能


g1 = task1(10)
g2 = task2(10)

while True:
    try:
        next(g1)
        next(g2)
    except Exception as e:
        pass
