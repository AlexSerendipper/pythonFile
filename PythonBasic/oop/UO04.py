""" 封装
【封装概述】
 实际上和定义一个javabean是非常像的，但是封装性没有java好，有带你伪私有
 在类属性和方法中，有名称修饰机制，利用该机制实现封装性
 __属性                   # ✔✔名称修饰（Name Mangling）机制：把属性/方法重命名
 __方法                     例如：如果一个属性名为__attr1，‌Python实际上会将其存储为_ClassName1__attr1的形式，‌其中ClassName1是当前类的名称。‌
                             这种机制用于防止 子类中的属性与方法 与 父类的隐藏属性或方法 发生冲突。。从而避免误重写和覆盖
                             同时保证了属性的私有性

------------
class Student:
    __score = 90
    def __init__(self, name, age):
        self.__name = name  # 设置了私有属性，只能在类的内部以__age的形式访问
        self.__age = age

    def setAge(self, age):
        self.__age = age    # 类的内部仍能以__age的形式访问

    def getAge(self):
        return self.__age


zzj = Student('zzj', 17)
print(zzj._Student__age)      # 可以看出，名称修饰机制的确是把属性以另一种名字来存储了，但调用者也不知道类名，所以保证了私有性
print(dir(zzj))               # dir函数，传入对象，返回该对象拥有的属性和方法
------------

"""
