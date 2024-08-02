""" 第三方模块
【第三方模块】首先需要在下方terminal终端输入pip xxx，对第三方模块进行安装，安装后才能使用import进行导入
 pip freeze                             # 可以在终端输入后，查看当前环境所有的依赖项
  pip freeze > requirements.txt           # >输出重定向，把当前所有依赖项写到当前目录下的xxx.txt文件中
 pip install pymysql=0.9.2              # 安装第三方模块，并且可以指定版本号
  pip install -r requirements.txt         # 按照xxx.txt中的依赖项安装

【munch】用于代替字典的数据类型（继承自原生字典）~支持字典的全部操作
 pip install munch
 munch1 = Munch()
 munch1.name = "zzj"                     # 支持点幅值
   munch1["age"] = "18"                    # 支持中括号赋值
 munch1.get("key1")                      # 支持字典的所有操作
   munch1.update(key1=xxx)
   munch1.pop("key1")
 munch1.toDict()                         # 将Munch类型转换为字典类型
  Munch(dict1)                             # 将字典对象转换为Munch对象
"""
from munch import Munch

dict1 = Munch()
print(type(dict1))

dict1.name = "zzj"
dict1["age"] = "18"
dict1.update(age=101)
print(dict1)



test = {"dataset": [Munch({'business_id': 2143, 'award_id': 4320, 'prize_id': 50, 'entity_id': 1392,
                           'service_id': '7253e6841d75e08021c532c52e6aa7e5', 'prize_sign_key': ''}), Munch(
    {'business_id': 2143, 'award_id': 4320, 'prize_id': 50, 'entity_id': 1403,
     'service_id': '7253e6841d75e08021c532c52e6aa7e5', 'prize_sign_key': ''})]}


test = test["dataset"]
print(test)