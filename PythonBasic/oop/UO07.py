"""
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
 __属性                   # ✔✔通过在属性前加双杠，把属性变为私有（相当于java的private)

【普通类方法】
def func(self)             # 此处的self相当于java的this，用于指向当前对象。主要用途也相同，用来区分类的属性 和 局部变量的
    pass

【构造器方法】python中把  __xxx__  这种格式的方法都叫魔术方法，无语
def __init__(self,name,age):
    self.name = name
    self.age = age
    pass

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
1、只能访问类的属性和方法，对象的是无法访问的
2、都可以通过类名调用访问aj
3、都可以在创建对象之前使用

"""


class Person:
    __name = 'zzj'
    __age = 23

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getname(self):
        print(self.__name)
        self.address = '深圳'
        print("实例方法")

    def setname(self, name):
        self.__name = name

    @classmethod
    def func(cls):
        print(cls.__name)

    @staticmethod
    def fuc():
        print(__name)


lzy = Person('lzy', 19)
lzy.getname()
lzy.setname('zzj')
lzy.getname()
