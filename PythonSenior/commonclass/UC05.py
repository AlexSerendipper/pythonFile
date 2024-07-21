""" 第三方模块
【第三方模块】首先需要在下方terminal终端输入pip xxx，对第三方模块进行安装，安装后才能使用import进行导入
 pip freeze                             # 可以在终端输入后，查看当前环境所有的依赖项
  pip freeze > requirements.txt           # >输出重定向，把当前所有依赖项写到当前目录下的xxx.txt文件中
 pip install pymysql=0.9.2              # 安装第三方模块，并且可以指定版本号
  pip install -r requirements.txt         # 按照xxx.txt中的依赖项安装


"""