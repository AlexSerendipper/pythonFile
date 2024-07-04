""" Python basic grammar
【python vs java】
  结构区别
 1）不同于java：project--module--package---class(.java)
   在python中：package--subpackage--module(.py)
   为保证结构相同，此处使用如下对应关系构建python项目,相当于少细分了一层
    如JavaBasic(project)--basicgrammar(module)--usearray(package)--xx.java
    PythonBasic(package)--basicgrammar(subpackage)--xx.py
 2）package中有一个_init.py文件，在包被导入时，包里的__init__.py会被执行。而directory表示文件夹，其中所有的文件同级，不存在子目录的概念
  内容区别
 1）二者都是面向对象
 2）python是解释型语言，java是编译型语言。
  （编译型表示针对不同的操作系统，将代码翻译成可被执行的机器码，因此针对不同的操作系统，需要对源码进行重新编译。编译型语言是一次性将所有代码编译成机器码的，因此执行效率高）
  （解释型语言是对源程序逐行解释成特定操作系统可执行的机器码并立即执行，因此每次解释性语言每次执行都需要进行一次编译，但其好处是跨平台容易）
（因此python执行效率低，但是当我们更看重产品的开发效率而不是执行效率的时候，python就是很好的选择。所以通常企业级的应用都使用java）
 3）python是弱类型的语言。python能用更少的代码做更多的事情，开发效率高。
  语法区别
 1）python语法中，是不需要封号作为结尾的

【python安装】
 官网安装python3.6.5解释器后，内含：doc(帮助文档) + lib(内置库) + scripts(外置库命令，内含有pip.exe包管理器)
 安装后，解释器中含有python.exe以及pip.exe，代表可执行命令，常见命令如下
   >python，因此在cmd中使用python命令进入python环境，写python程序
   >python 文件名，使用python解释器解释特定的python源文件
   >pip list，查看当前外置库中已安装的包
   >pip install 文件名，代表在当前python解释器中安装指定外部包（从网络中下载）。
    如pip install redis==3.2.0，表示安装redis，并指定版本号为3.2.0，不指定版本则默认安装最新版本
   >pip freeze > requirement.txt，把当前解释器中所有的外置库中的包及对应版本号以txt文件的形式输出（方便程序在不同系统间的迁移）
   >pip install -r requirements.txt，使用pip安装requirements,txt中依赖的文件
 注意：使用pip安装的外置包位于\Lib\site-packages中

【pycharm相关】
 使用pycharm创建项目需要指定编译器
   setting-project-python interpreter-new environment，创建一个新的python环境。。这样指定后会创建一个.venv文件在项目中，表示新的python解释环境
     建议使用existing interpreter，找到本机安装python时的python.exe，使用本地环境

【基础函数】
 type(变量名)                    // 返回变量类型
 print("内容",变量名)            // 输出，可以使用逗号输出多个参数，多个参数输出时默认分隔符为空格，结尾默认为\n
  print(变量名1,变量名2,sep="#")          // 输出，多个参数输出时指定分隔符
  print(变量名1,end=" ")          // 输出，多个参数输出时指定结尾！
 input("提示信息")               // 标准的输入流，相当于java中的sc.next()✔✔✔，区别是可以输入提示信息
 id(变量名)                      // 输出变量的内存地址，java中打印引用数据类型，默认打印的是地址值✔✔✔
                                     py中打印int、float、double、String、列表、字典、元组直接打印均为字面量。

【常用包】后续会总结
import random
random.randint(a,b)              # 产生[a,b]之间的随机数

"""
print("hello world")
