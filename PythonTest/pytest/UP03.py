"""         
@Decription:数据驱动，测试用例（具体用例见env文件），示例见错误登录2
@Time : 2024/7/28 13:38
@Author:alexzhong

【python -m pytest的使用】
 python -m pytest                     # 会自动把当前工作目录作为模块搜索路径
-------------------------
文件目录为 "D:\PycharmWorkspace\PythonTest\pytest\lib\loginAndCheck.py"

在文件"D:\PycharmWorkspace\PythonTest\pytest\cases\登录\test_错误登录2.py"中
去from pytest.lib.loginAndCheck import loginAndCheck

终端中当前目录为 D:\PycharmWorkspace
若直接使用pytest去执行(和直接使用python一样) pytest .pytest\cases\登录\test_错误登录2.py 的搜索路径是一样的，都是只将xxx.py文件的父目录添加到搜索路径中
也即[D:\PycharmWorkspace\PythonTest\pytest\cases\登录]

而我们导入时，希望的搜索目录是 D:\PycharmWorkspace！！

所以使用python -m pytest .pytest\cases\登录\test_错误登录2.py，

python -m pytest会将当前目录，也即D:\PycharmWorkspace 添加到搜索路径当中，所以能导入成功
-------------------------

【数据驱动】见test_错误登录2
 @pytest.mark.parametrize()          # 使用该装饰器传递参数，可以一次性传入多组参数，可以进一步简化流程

【调试】
 左上角+号，选择edit configurations，添加python tests，选择module - pytest
                                                        additional arguments - PythonTest\pytest\cases\登录\test_错误登录.py::Test_错误登录
                                                        working directory - D:\PycharmWorkspace\
"""
