""" 内部函数，即在函数里再定义一个函数
【内部函数】
a = 100
print(globals())  # 可以查看全局变量有哪些
def func():
    n = 100  # 声明局部变量
    list1 = [1,2,3]  # 声明局部变量

    # 声明内部函数，方便用于对局部变量进行操作！！
    # 内部函数中声明的变量仍属于令一层局部变量，因此在内部函数的局部域中，无法修改n(不可变类型)，但可以修改list1(可变类型)
      如果要修改外层局部变量n的值，需要在内部函数声明之初声明 nonlocal n
      如果要修改全局变量a的值，也是要在内部函数声明之初声明 global a
    def inner_func():
        pass

    # 调用内部函数
    inner_func()

    # 使用locals()内置函数，可以看到在当前函数中声明的内容有哪些，返回值为字典形式
    print(locals())

1）两个内部函数之间是可以相互调用的

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
"""


# 内部函数示例
def func():
    a = 11

    def inner_func():
        print(a)

    return inner_func


x = func()
x()


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