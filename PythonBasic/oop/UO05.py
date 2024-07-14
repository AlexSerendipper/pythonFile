""" 继承
【继承】继承的思想和java是一样的
 子类无法继承父类的私有属性
class Subclass(SuperClass):
    pass

【多继承】java中只有接口有多继承，而python中类也可以多继承
class Parent1():
    pass
class Parent2():
    pass
class Child(Parent1,Parent2):
    pass

cc = Child
cc.__mro__               # 该方法能够查看搜索顺序
 多继承的搜索顺序：如果两个父类中有同名方法，采用 从左至右，广度优先 的原则进行搜索，
即在这种情况下，解释器首先搜索第一个父类，然后是第二个父类，依此类推，在完成一轮搜索后，才会去搜索父类的父类。

【方法重写】
 方法重写：在子类中可以根据需要对从父类中继承来的方法进行改造，也称为方法的重置、覆盖。在程序执行时，子类的方法将覆盖父类的方法。
 子类重写的方法必须和父类被重写的方法具有相同的方法名称、参数列表
"""


class Parent():
    def eat(self, food):
        print(food)


class Child(Parent):
    def eat(self, food):
        print(food)
        print("son")


zzj = Child()
zzj.eat('苹果')
