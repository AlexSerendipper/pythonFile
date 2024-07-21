""" 类
【面向对象】面向对象思想见java处，同样有属性和方法
 所有类名要求首字母大写，如TypeError
 所有的类都继承自Object类
class 类名:                # 创建类
    属性
    方法

对象1 = 类名()              # 创建对象

【类属性】
 python只分为对象属性和类属性不像，java中还有静态属性，常量等
  在类中声明的属性称为类属性
  生成对象后添加的属性称为对象属性
 对象1.属性 = x            # 调用当前对象的属性，与java很大的区别是：
                             如果不存在相关属性。这样操作可以往当前对象中添加属性，而不会报错


【普通类方法】
def func(self)             # 此处的self相当于java的this，用于指向当前对象。主要用途也相同，用来区分类的属性 和 局部变量的
    pass

【方法的重载！！】python中没有方法的重载
 java中在同一个类中，允许存在一个以上的同名方法，只要它们的参数个数或者参数类型不同即可。
   python中，后创建的同名方法 会 覆盖先创建的同名方法！！！！！！

【构造器方法】python中把  __xxx__  这种格式的方法都叫魔术方法，无语
1) 初始化魔术方法，这个就完全相当于java的构造器了！！！但是python中只允许单构造器
def __init__(self,name,age):
    self.name = name
    self.age = age
    pass

2) 实例化魔术方法
def __new__(cls,*args,**kwargs):       // __new__是魔术方法 在类的实例化过程中被首先调用，负责创建对象并返回一个实例给后续的__init__方法进行初始化。
    return object.__new__(cls)            当__new__方法创建了一个对象后，Python解释器会将这个新创建的对象作为第一个参数传递给__init__方法，以便进行进一步的初始化操作。
                                          具体来说__new__方法主要负责对象的创建，包括在内存中为对象分配空间。它至少需要一个参数cls，代表要实例化的类，并且必须返回一个实例对象。
                                          如果类中没有重写__new__方法，Python会默认调用父类的__new__方法来构造该实例。
                                          __new__魔术方法经常用于单例模式的创建
3) 函数式魔术方法
def __call__(self,x):                  //  __call__方法允许类的实例像函数一样被调用。
    print("__call__")                     通过在类中定义__call__方法，‌你可以使类的实例表现出类似函数的行为。即能够实现对象被调用时，所传入的参数传递给__call__方法。‌

4) 析构魔术方法
def __del__(self):                     //  __del__方法用于在对象被销毁之前执行一些清理操作。它通常用于释放对象占用的资源，如文件句柄、网络连接或其他外部资源
    print("__del__")                      程序结束时，python执行垃圾回收机制，回收本次执行过程中使用到的空间。从而也会触发析构魔术方法

5) 双下划线模式方法，完成类似于java的toString方法
def __str__(self):                     //  print()函数打印一个对象或者使用str()函数将对象转换为字符串时，‌Python会自动调用该对象的__str__方法。‌
    return self.name                       __str__方法应该返回一个字符串，‌这个字符串描述了对象的状态或者提供了关于对象的有用信

【类方法】类似于java的静态方法
 类方法随着类的创建而创建，类方法中能访问该类原本就有的属性！
  和java的静态方法还不完全一样，java的静态方法只能访问静态属性，python都没有静态属性这个说法
@classmethod
def func(cls):
    pass

【静态方法】类似于java的静态方法一样，
 静态方法不能直接访问或修改类或实例的属性或方法。静态方法通常用于执行与类和实例无关的操作，例如执行一些工具函数或辅助操作。
  和java的静态方法还不完全一样，java的静态方法只能访问静态属性，python都没有静态属性这个说法

@staticmethod
def func():                    # 没有cls
    pass

【静态方法与类方法的区别】
不同:
1、装饰器不同
2、类方法是有参数的，静态方法没有参数
3、静态方法不能直接访问或修改类或实例的属性或方法，类方法可以
相同.
2、都可以通过 类名/对象名 调用访问
3、都可以在创建对象之前使用
"""


class Person:
    __name = 'zzj'
    __age = 23

    def __init__(self, name, age):
        print("__init__")
        self.__name = name
        self.__age = age

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls)  # 返回一个实例化对象

    def __call__(self, x):
        print('__call__')

    def __del__(self):
        print('__del__')

    def getname(self):
        print(self.__name)
        self.address = '深圳'

    def setname(self, name):
        self.__name = name

    @classmethod
    def func(cls):
        print(cls.__name)

    @staticmethod
    def fuc():
        print('hhh')
        # print(__name)


lzy = Person('lzy', 19)
lzy.getname()
lzy.setname('zzj')
lzy.getname()
lzy(666)
del lzy  # 删除lzy对地址的引用
