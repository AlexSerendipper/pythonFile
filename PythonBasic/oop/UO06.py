""" 多态..python的多态和java区别还是挺大的
 isinstance(obj,类1)               # 判断obj是类1的对象 或 obj是类1的子类的对象

----------------------------------
【在java中】多态体现在
 父类的引用指向子类的对象（或说子类的对象赋给父类的引用）
 多态的前提：
  1）需要存在继承或者实现关系
  2）有方法的重写
 多态性的体现
虚拟方法调用：这是java中多态性最具特点的体现，父类会根据赋给它的不同子类对象，动态调用属于子类的该方法。这样的方法调用在编译期是无法确定的，所以也称为动态绑定！！
---------------------------------
【在python中】多态体现在
 多态没有所谓的前提！！即
  1）只关心对象的实例方法是否同名，不关心对象所属的类型；
  2）对象所属的类之间，继承关系可有可无；
 多态性的体现
python中，多态性体现的是向同一个函数，传递不同参数后，可以实现不同功能.
---------------------------------
# 多态性经典示例如下
class Base():
    num = 10
    def display(self):
        print("Base", self.num)

class Sub1(object):                       # 可以发现python，多态的继承关系可有可无
    num = 20
    def display(self):
        print("sub1", self.num)

class Sub2(Base):
    num = 20
    def display(self):
        print("sub2", self.num)

def display(base):                        # 多态性体现的是向同一个函数，传递不同参数后，可以实现不同功能.
    base.display()

display(Base())                           # Base 10
display(Sub1())                           # sub1 20
display(Sub2())                           # sub2 20

---------------------------------
"""


