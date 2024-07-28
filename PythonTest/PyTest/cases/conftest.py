"""         
@Decription:
@Time : 2024/7/23 22:07
@Author:alexzhong
"""
import pytest

@pytest.fixture(scope='package',autouse=True)
def emptyCases():
    print(f'\n#### 初始化-cases')
    yield

    print(f'\n#### 清除-cases')