""" 内部函数，即在函数里再定义一个函数
【内部函数】
1）两个内部函数之间是可以相互调用的
-----------------------
n = 1                             # 全局变量n
print(globals())                  # 可以查看全局变量有哪些
def a():
    n = 'a内'                     # 局部变量n。。如果要修改全局变量a的值，也是要在内部函数声明之初声明 global n
    list1 = [1,2,3]
    def b():
        nonlocal n                # nonlocal即声明该内部函数的局部变量，与其最近的一个外层函数的同名局部变量 引用同一个地址
        n = 'b内'
        print(n)
        def c():
            n = 11                # 没有声明nonlocal，相当于重新申请了一个局部变量n
            list1.append(6)       # 对于可变类型数据，是可以直接修改的~
            print(locals())       # 使用locals()内置函数，可以看到在当前函数中声明的内容有哪些，返回值为字典形式
            print(n)
        c()
    b()
    print(n)
    print(list1)
a()
输出结果如下：
b内
11
b内
[1, 2, 3, 1]
-----------------------

【闭包】
# 定义了内部函数后，并且内部函数引用了外部函数的变量值，使用return将内部函数抛出，称为闭包
def func(a):
    b = 0
    def inner_func():
        print(a+b)   # 引用a或b都算闭包
        pass
    return inner_func

x = func(5)
x()   # 调用内部函数


1) 闭包的作用是能够保存状态，如上x = func(5)，实际上就保存了a=5这个状态。这个x就不会再受到a值变化的影响
  下次在调用x1 = func(7)。这个x1存储的就是a=7的状态
2) 由于闭包引用了外部变量没有及时释放，所以略微消耗内存
3) 由于每次调用内部函数都会重新读取一次外部局部变量b=0。。因此可以利用该特性完成一些功能(如计数器)，如将外部局部变量设置为可变型变量(如列表)

【装饰器】
# python的装饰器实现的功能和java中的动态代理(AOP一致)，在改变原函数的基础上新增功能
# 装饰器和闭包类似，即在内部函数中引用了外部函数中的输入函数作为参数，并使用return将内部函数抛出，称为装饰器
  调用装饰器时，即在函数上添加@decorate即可
----------------------------------
def decorate(func):
    a = 100
    print(11111)
    def wrapper():
        print("USB准备连接..")
        func()
        print("USB连接完成..")

    print(22222)
    return wrapper


@decorate
def usb()
    print("USB正在连接..")

usb()
----------------------------------
def outer2(x):                          # 接收装饰器参数
    def decorate2(func):                # 接收被装饰函数
        a = 100
        print(11111)
        print(x)
        def wrapper2():                 # 接收函数实参
            print("USB准备连接..")
            func()
            print("USB连接完成..")
        print(22222)
        return wrapper2
    return decorate2

@outer2("带参装饰器的使用")
def usb():
    print("USB正在连接..")

usb()
----------------------------------
1) 当使用@decorate时，首先将被装饰函数usb作为参数传递给装饰器decorate
2) 然后将依次将装饰器中的变量以及内部函数加载到内存中。所以只要使用了@decorate，11111和22222就会被打印
   同时会把内部函数wrapper返回给被装饰函数usb接收，因此在调用usb时，会实现AOP的效果
   注意：如果被装饰函数中有入参，则装饰器的内部函数中也需要添加入参 (建议使用*args以及**args增加拓展性
3) 可以对被装饰函数添加多个装饰器，执行顺序为越靠近被装饰函数声明位置的越先被执行
4) 如果"新增加的功能"是动态的，也可以给装饰器传参数，@decoration(参数1)
   此时需要在原有的装饰函数外再嵌套一层（负责接收装饰器参数），并将原装饰函数抛出，才能实现相关功能


【常用装饰器】
1) @property：使一个类方法可以像属性一样被使用，而不需要在调用的时候带上()
-----------------------------

class Person():
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    @property                                                 # 让fullname这个方法可以以属性的方式被调用
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter                                          # setter方法需要和 @property修饰的方法具有相同的名字
    def fullname(self, name):                                   它会将用户传给.fullname属性的值，作为参数参数这个函数（在此处就实现了根据传入的fullname，自动修改first和lastname
        first_name, last_name = name.split(' ')
        self.first = first_name
        self.last = last_name


zzj = Person('钟', '郑建')
print(zzj.fullname)
zzj.fullname = '钟 郑淮'
print(zzj.fullname)
-----------------------------
"""


# 装饰器示例
def decorate(func):
    a = 100
    print(111111)

    def wrapper():
        print("USB准备连接..")
        func()
        print("USB连接完成..")

    print(222222)
    return wrapper


@decorate
def usb():
    print("USB正在连接..")


usb()

# 带参装饰器示例
print("-----------------------------")


def outer2(x):
    def decorate2(func):
        a = 100
        print(11111)
        print(x)

        def wrapper2():
            print("USB准备连接..")
            func()
            print("USB连接完成..")

        print(22222)
        return wrapper2

    return decorate2


@outer2("带参装饰器的使用")
def usb():
    print("USB正在连接..")


usb()



