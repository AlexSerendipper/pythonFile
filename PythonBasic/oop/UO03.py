""" 匿名函数
【匿名函数】匿名函数用于简化函数定义，感觉和java的lambda表达式很像
   格式： lambda 参数1,参数2...:运算       # 参数1、2为输入参数，运算为对输入参数进行运算后return的结果
   map(key1, list1)                       # 利用lambda匿名函数对可迭代体(list1)进行遍历操作
   reduce(key1, tuple1, initialValue)     # 对可迭代体(列表、元组等)中元素进行加减乘除运算的迭代操作的函数
-----------------
tuple1 = [1,2,3,4,5]
result = reduce(key1, tuple1, 30)          # 计算过程实际上就是 30-1 = 29
                                                               29-2 = 27...如此迭代运算
                                            如果没有初始值，就是1-2=-1
                                                              -1-3 = -4...如此迭代运算
-----------------
   filter(key1, iterable1)                # 对可迭代体进行筛选操作，注意函数返回值是布尔类型
   sorted(iterable1,key1,Reverse=True)    # 对可迭代体进行排序操作

【递归函数】和java是一样的，自己调用自己

"""

from functools import reduce

# 匿名函数示例1
list1 = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
result = max(list1, key=lambda x: x['a'])  # 由于每一项(字典)是无法进行直接比较的，因此取出每一项(字典)的a的值作为依据。从而实现比较
print(result)

# 匿名函数示例2
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = map(lambda x: x if x % 2 == 0 else x + 100, list2)  # 迭代器如果，list2中的数据为奇数，则加100
print(list(result))

# 匿名函数示例3
tuple1 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x - y, tuple1)
print(result)

# 匿名函数示例4
list3 = [{'name': 'zzj', 'age': 20},{'name': 'lzy', 'age': 19}, {'name':'hyq','age': 13}]
result2 = sorted(list3, key=lambda x : x['age'], reverse=True)
print(result2)

