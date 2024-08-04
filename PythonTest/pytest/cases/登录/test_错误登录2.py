"""         
@Decription:示例2
@Time : 2024/7/28 13:37
@Author:alexzhong
"""
import pytest
from PythonTest.pytest.lib.loginAndCheck import loginAndCheck

# 分开写：
class Test_错误登录:
    def test_UI_0001(self):
        alertText = loginAndCheck(None,'88888888')
        assert alertText == '请输入用户名'


    def test_UI_0002(self):
        alertText = loginAndCheck('byhy',None)
        assert alertText == '请输入密码'

    def test_UI_0003(self):
        alertText = loginAndCheck('byh','88888888')
        assert alertText == '登录失败 : 用户名或者密码错误'

# 一起写：数据驱动
class Test_错误登录2:
    @pytest.mark.parametrize('username, password, expectedalert', [
        (None, '88888888', '请输入用户名'),
        ('byhy', None, '请输入密码'),
        ('byh', '88888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '8888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '888888888', '登录失败 : 用户名或者密码错误'),
    ]
                             )
    def test_UI_0001_0005(self, username, password, expectedalert):
        alertText = loginAndCheck(username, password)
        assert alertText == expectedalert