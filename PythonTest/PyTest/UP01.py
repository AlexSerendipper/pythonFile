"""
@Decription: Pytest概述
@Time : 2024/7/22 20:29
@Author:alexzhong

【Pytest概述】
 pytest 可以用来做系统测试的自动化， 它的特点有
  用 Python 编写测试用例，简便易用
  可以用 文件系统目录层次 对应 手工测试用例 层次结构
  灵活的 初始化清除 机制
  可以灵活挑选测试用例执行
  利用第三方插件，可以生成不错的报表
 pip install pytest                  # 安装pytest

【Pytest命名约束】pytest寻找测试项的 具体规则
 编写的测试用例代码文件，必须以 test_ 开头，或者以 _test 结尾
   测试用例文件命名为 test_*.py 或 *_test.py 文件
   会自动搜索测试项，如以 test为前缀 的函数，或以 Test为前缀 的类里面的 test为前缀 的方法
   执行pytest时，会自动寻找当前目录以及其子目录下所符合以上命名规则的文件或代码进行执行
 如果未指定命令行参数，则从 testpath（如果已配置）或当前目录开始收集。
   如果命令行参数， 指定了 目录、文件名 或 node id 的任何组合，则按参数来找
 寻找过程会递归到目录中，除非它们匹配上 norecursedirs。

【pytest启动】
 Terminal终端
   pytest            # 切换到当前根目录后，使用该命令，会执行根据命名约束执行所有根目录下所有测试文件
    pytest cases      # 执行根目录下，cases文件夹中所有满足命名约束的测试文件
    pytest cases1 case2\\登录        # 可以指定多个目录
    pytest 文件名.py::类名::方法名   # 也可以只执行测试文件中的某个类，某个方法
                                       如pytest cases/登录/test_错误登录.py::Test_错误密码2::test_C001021
   pytest -s         # -s 显示测试代码中print的内容，主要用于调试，默认是不显示的
   pytest -v         # -v 可以得到更详细的执行信息，包括每个测试类、测试函数的名字
   pytest -k xxx     # ✔✔ 使用命令行参数-k加名字来挑选要执行的用例
                         xxx可以是测试函数的所有执行单元的部分名字(函数、类、模块、目录
                         xxx大小敏感
                         "not xxx" 表示名字中不包含
                         "xxx1 and xxx2" 表示同时包含多个关键字
                         "xxx1 or xxx2" 表示包含指定关键字之一即可

【pytest-html测试报告】
 解决pytest-html测试报告中文乱码问题
    1) Lib\\site-packages\\pytest_html下找result.py文件,19行左右
    # self.test_id = report.nodeid.encode("utf-8").decode("unicode_escape") 改为==> self.test_id = report.nodeid
    2) Lib\\site-packages\\pytest_html下找html_report.py这个文件,117行左右修改如下
    # head = html.head(html.meta(charset="utf-8"), html.title(self.title), html_css) 改为==> head = html.head(html.meta(charset="GB2312"), html.title(self.title), html_css)
 pip install pytest-html                                     # 测试报表插件，pytest-html，这里3.2.0版本有中文乱码问题
 pytest cases --html=report.html --self-contained-html       # 生成html形式的pytest报告，报告名为report.html，并且采用内嵌（self-contained）形式，不产生额外的文件(css等

【使用规范】
 在项目根目录下创建directory，命名为cases用于存放测试用例

【pytest标签】
import pytest
 @pytest.mark.名字1                # 可以为指定的方法、类、函数设置标签，依据标签来执行用例
                                       注意可以为方法、类、函数设置多个标签
 pytestmark = pytest.mark.名字2                       # 可以这样定义一个全局变量pytestmark为整个模块文件 设定标签
  pytestmark = [pytest.mark.名字1, pytest.mark.名字2]   #  为模块设置多个标签
 pytest -m 名字1 -s                # 执行所有名字1标签的用例



"""
import sys
print(sys.path)