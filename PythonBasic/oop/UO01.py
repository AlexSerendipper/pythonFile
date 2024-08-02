""" 函数（java里没有单独的函数，都是用方法）
【定义】可为形参设置默认值，赋值时若未传参则使用默认值
def 函数名([参数1,参数2...])
    函数体


 print(函数名)         # 打印函数名和地址
 函数名()              # 调用函数

【可变参数类型】
 形式像元组拆包。实际上此处是在底层提供了一个空元组，多余参数就是往元组中添加值
 注意可变参数*args如果和固定参数结合时要往后放
def 函数名(参数1, *args)
    函数体

【关键字参数类型】当设置默认值，调用时默认是是依次赋值，若有需要可指定形参赋值，即关键字参数赋值~~见示例
def 函数名1(x,y=default1,z=default2):
    函数体

def 函数名1(**kwargs):          # 可变参数类型2，实际上此处是在底层提供了一个字典，多余参数就是往字典中添加val。
    函数体                        必须使用关键字参数赋值的方式进行赋值，将关键字作为key值
                                  √字典类型需要先进行拆包后才能传入**kwargs。。。字典类型拆包为**dict1

【特殊关键字的使用】
0)return
  python中return的功能是用于返回值！！！
    如果返回值为多个值，会把这多个值放到元组中（可以用多个值接收，自动拆包）！！！
    如果未设返回值，使用变量接收到的值是none
   (java中return的功能是结束一个方法。当一个方法执行到一个return语句时，这个方法将被结束)
1）break()
  break语句用于终止某个语句块的执行
  主要用于switch语句和循环语句中
  break语句出现在多层嵌套的语句块中时，默认退出最近一层循环
  break语句出现在多层嵌套的语句块中时，可以通过标签指明要终止的是哪一层语句块。见下方例子
2）continue()
  continue只能使用在循环结构中
  continue语句用于跳过其所在循环语句块的一次执行，继续下一次循环
  continue语句出现在多层嵌套的语句块中时，默认退出最近一层循环的当此循环
  continue语句出现在多层嵌套的循环语句体中时，可以通过标签指明要跳过的是哪一层循环

【匿名函数】匿名函数用于简化函数定义，感觉和java的lambda表达式很像。。。。map、reduce属于functools高阶函数模块
   格式： lambda 参数1,参数2...:运算        # 参数1、2为输入参数，运算结果作为匿名函数的返回值
   map(key1, list1)                       # 利用lambda匿名函数对可迭代体(list1)进行遍历操作
   reduce(key1, tuple1, initialValue)     # 对可迭代体(列表、元组等)中元素进行加减乘除运算的迭代操作的函数
-----------------
tuple1 = [1,2,3,4,5]
result = reduce(lambda x, y: x - y, tuple1, 30)          # 计算过程实际上就是 30-1 = 29
                                                               29-2 = 27...如此迭代运算
                                                           如果没有初始值，就是1-2=-1
                                                              -1-3 = -4...如此迭代运算
-----------------
   filter( , iterable1)                  # 对可迭代体进行筛选操作，注意函数返回值是布尔类型
   sorted(iterable1,key1,Reverse=True)   # 对可迭代体进行排序操作

【递归函数】和java是一样的，自己调用自己
"""


# 可变参数类型
def change(name, *args):
    print(name)
    print(args)


change('zzj')
change('zzj', 1, 1)


# 关键字参数
def key1(a, b=10, c=6):
    print(a + b + c)


key1(10, 20)
key1(10, c=20)


# 可变参数类型+关键字参数
def key2(**kwargs):
    print(kwargs)


key2()
key2(a=1, b=2, c=3)
dict1 = {'zzj': 100, 'lzy': 666}
key2(**dict1)  # 拆包后即为zzj=100,lzy=666的格式。。这样才能装到**kwargs底层的字典当中


from functools import reduce
# 匿名函数示例1
list1 = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
result = max(list1, key=lambda x: x['a'])  # 由于每一项(字典)是无法进行直接比较的，因此取出每一项(字典)的a的值作为依据。从而实现比较
print(result)

# 匿名函数示例2
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = map(lambda x: x if x % 2 == 0 else x + 100, list2)  # 便历操作，如果list2中的数据为奇数，则加100
print(list(result))

# 匿名函数示例3
tuple1 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x - y, tuple1)  # 迭代操作
print(result)

# 匿名函数示例4
list3 = [{'name': 'zzj', 'age': 20},{'name': 'lzy', 'age': 19}, {'name':'hyq','age': 13}]
result2 = sorted(list3, key=lambda x : x['age'], reverse=True)  # 排序操作
print(result2)