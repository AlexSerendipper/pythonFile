"""         
@Decription:
@Time : 2024/7/23 22:09
@Author:alexzhong
"""
import pytest

@pytest.fixture(scope='package',autouse=True)
def emptyLogin():
    print(f'\n#### 初始化-Login')
    yield

    print(f'\n#### 清除-Login')