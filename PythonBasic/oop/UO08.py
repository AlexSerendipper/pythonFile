""" 设计模式
【单例模式】实现内存优化
---------------
class Singleton():
    __instances__ = None
    def __new__(cls, *args, **kwargs):
        if cls.__instances__ is None:
            cls.__instances__ = super(Singleton, cls).__new__(cls)       # 如果实例为空，才发配地址空间给__init__
            return cls.__instances__
        else:
            return cls.__instances__

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
---------------


"""
