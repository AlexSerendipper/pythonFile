"""         
@Decription:示例1
@Time : 2024/7/22 20:54
@Author:alexzhong

"""
import sys

import pytest

pytestmark = pytest.mark.名字2
def setup_module():
    print('\n *** 初始化-模块 ***')


def teardown_module():
    print('\n ***   清除-模块 ***')


class Test_错误密码:
    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除-类 ===')

    def setup_method(self):
        print('\n --- 初始化-方法  ---')

    def teardown_method(self):
        print('\n --- 清除-方法 ---')

    def test_C001001(self):
        print('\n用例C001001')
        assert 1 == 1

    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2

    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2


class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1

    def test_C001022(self):
        print('\n用例C001022')
        assert 2 == 2


