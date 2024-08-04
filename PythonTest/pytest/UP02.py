"""         
@Decription: 初始化清除，见test_错误登录.py
@Time : 2024/7/23 21:39
@Author:alexzhong

 对自动化测试框架来说，初始化清除功能 至关重要
 初始化清除功能可以分为四个级别

【1、模块级别】
 模块级别的初始化、清除在整个模块所有用例 执行前后 分别执行1次
  它主要是用来为该 模块 中 所有的测试用例做公共的 初始化 和 清除
 def setup_module():          # 模块级别初始化，通常写在模块头部
 def teardown_module():       # 模块级别清除，通常写在模块头部

【2、类级别】
 类级别的初始化、清除在整个类的所有用例 执行前后 分别执行1次 。
  它主要是用来为该类中的所有测试用例做公共的初始化和清除
 @classmethod                 # 类级别的初始化，在对应类中定义此类方法
  def setup_class(cls):
 @classmethod
  def teardown_class(cls):     # 类级别的清除，在对应类中定义此类方法

【3、方法级别】
 方法级别的初始化、清除 在整个类的每一个用例 执行前后 分别执行1次
 def setup_method(self):      # 方法级别的初始化，在对应类中定义该方法
 def teardown_method(self):   # 方法级别的清除，在对应类中定义该方法

【4、目录级别】
 目标级别的初始化、清除，就是针对整个目录执行的初始化、清除。
  我们在需要 初始化、清除 的目录下面创建 一个名为 conftest.py 的文件，里面内容如下所示
--------------------------
import pytest

@pytest.fixture(scope='package',autouse=True)
def 函数名1():
    print(f'\n#### 初始化-目录甲')
    yield

    print(f'\n#### 清除-目录甲')
---------------------------

【】
前面讲初始化清除时，主要用的是 unittest 风格的初始化清除方法。
pytest里面有更灵活方便的初始化、清除 方法，就是使用 fixture
具体可以查看白月黑羽文档https://www.byhy.net/auto/pyatframework/pytest-01/#pytest_1

"""
