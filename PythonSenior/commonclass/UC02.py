""" 系统层面模块
【functools】高阶函数模块
 map()
 reduce()
 filter()


【builtins】标准类库，可直接调用的函数
 type(变量名)                    // 返回变量类型
  isinstance(变量名, 类型)        // 判断变量类型
  isinstance(obj,类1)               判断obj是类1的对象 或 obj是类1的子类的对象
 print("内容",变量名)            // 输出，可以使用逗号输出多个参数，多个参数输出时默认分隔符为空格，结尾默认为\n
  print(变量名1,变量名2,sep="#")          // 输出，多个参数输出时指定分隔符
  print(变量名1,end=" ")          // 输出，多个参数输出时指定结尾！
 input("提示信息")               // 标准的输入流，相当于java中的sc.next()✔✔✔，区别是可以输入提示信息
 id(变量名)                      // 输出变量的内存地址，java中打印引用数据类型，默认打印的是地址值✔✔✔
                                     py中打印int、float、double、String、列表、字典、元组直接打印均为字面量。
 chr(int)                       // 传入数字，根据Unicode码转换为字母
  ord(char)                      // 传入字母，根据Unicode码转换为数字
 bin()/hex()/oct()              // 格式转换类...

【sys】python运行环境模块
 sys.path()               # 返回搜索路径，搜索时会按照列表中的路劲依次进行查找。
                             可以看出是先找自身包下的自定义模块，然后在去寻找系统路径下的
                             可以右键包，mark as source root，添加到系统的搜索路径当中
 sys.version()            # 打印python版本
 sys.argv()               # argument vector，获取命令行参数。这在编写需要与用户交互或需要外部输入的脚本时非常有用
                             java中也有这个传参，python中是在UC02-edit configurations-script parameters处进行传参


【logging手动版】java中使用log4j，python就是使用logging，进行记录日志以及调试
 日志级别： 没有指定默认为warning级别
  DEBUG（调试）：最低级别，通常用于调试问题。
  INFO（信息）：表明发生了预期的事件。
  WARNING（警告）：表明发生了可能需要注意的事件
  ERROR（错误）：表明发生了严重错误事件。
  CRITICAL（严重）：最高级别，表明发生了严重的错误，这可能导致应用程序的失败。
 logging.warning("这是warning日志")                                      # 默认只能输出强于warning级别的日志
 logging.exception(e)                                                   # 该方法能打印详细的错误信息
 logging.basicConfig(filename='demo.log',level=logging.DEBUG)           # filename会将日志信息输出到当前目录下的文件当中
                                                                           level调整日志输出级别，此时可以输出DEBUG级别的日志
                                                                           filemode可以设置为写入模式w，追加模式a等
                                   使用format参数可以指定输出格式，默认输出格式为WARNING:root:warning
                                   format=%(asctime)s %(levelname)s %(message)s %(filename)s %(lineno)s
                                   表述输出时间、级别、内容（即这是warning日志这段话、文件名、报错行号
                                                                          datefmt=%Y/%m/%d %H:%M:%S，可以指定输出时间的格式
【logging编程版】
 logging模块采用了模块化设计，包含了Loggers，Handlers，Filters，Formatters这个组件
  Loggers记录器，提供应用程序代码能直接使用的接口
  Handlers处理器，将记录器产生的日志发送至目的地（可以是文件、标准输出、邮件、或者通过socke、http等协议发送到任何地方。，
  Filters过滤器，提供更好的粒度控制，决定哪些日志会被输出;
  Formatters格式化器，设置日志内容的组成结构和消息字段。
 logger = logging.getLogger(__name__)          # 创建记录器，logger是单例的，不传入name，则默认使用root作为记录器名
  logger.setLevel(logging.INFO)                 # 设置日志记录的级别
  logger.addHandler(sh)                         # 将记录器与指定的handler相关联
  logger.removeHandler()                        # 解除handler关联
  logger.addFiler(flt)                          # 关联过滤器
 sh=logging.StreamHandler(stream=None)         # StreamHandler用于标准输出。默认在console输出
  sh.setLevel(logging.DEBUG)                    # 设置handler的告警级别，如果没有给handler指定告警级别，将使用记录器的级别
  fl=logging.FileHandler(filename, mode='a',encoding=None,delay=False)          # FileHandler用于将日志保存到磁盘文件，默认采用追加的方式
  sh.setFormatter(formatter1)                   # 给处理器设置当前handler对象使用的消息格式，需要传入Formatter对象。
  fl.addFilter(flt)                             # 关联过滤器
 还有一些其他的handler，如：
  RotatingFileHandler用于一定的方式来生成多个日志文件(如按大小
  TimedRotatingFileHandler用于按照时间的方式来生成多个日志文件
 如果为记录器和handler都设置了告警等级，那么会输出比二者的告警等级更高的日志，如上，会输出INFO及以上日志（注意logger默认级别为WARNING
 formatter1 = logging.Formatter("%()s", datefmt=None, style='', fmt=None)     # 创建formatter，首先指定手动logging中的format格式，其余参数可选
 logger.debug("this is a debug log")          # 使用logger来记录日志

 flt = logging.Filter("zzj.nb")               # 新增过滤器，要求 logger名/存储文件名 必须为zzj.nb. 开头，才能正常输出

【logging配置文件版】推荐使用，配置文件见logging.conf
import logging.config as log_config
 logging.config.fileConfig('logging.conf')    # 读取配置文件
 其余的使用方式与logging编程版相同
---------------------------------------------
#记录器：提供应用程序代码直接使用的接口
#设置记录器名称，root必须存在！！！
[loggers]
keys=root,zzj.nb.cls

#处理器，将记录器产生的日志发送至目的地
#设置处理器类型
[handlers]
keys=fileHandler,consoleHandler

#格式化器，设置日志内容的组成结构和消息字段
#设置格式化器的种类
[formatters]
keys=simpleFormatter

#设置记录器root的级别与handler种类
[logger_root]
level=DEBUG
handlers=consoleHandler

#设置记录器zzj.nb.cls的级别与种类
[logger_zzj.nb.cls]
level=DEBUG
handlers=fileHandler,consoleHandler
#起个对外的名字，调用时使用这个名字
qualname=zzjnb
#继承关系，一般不用
propagate=0

#设置
[handler_consoleHandler]
class=StreamHandler  # 父类
args=(sys.stdout,)  # 标准输出，即输出到console
level=DEBUG
formatter=simpleFormatter

[handler_fileHandler]
class=handlers.TimedRotatingFileHandler  # 在午夜1点（午夜12点后第3600s）开启下一个log文件，第四个参数0表示永久保留历史文件，如果输入10则保留历史文件10天
args=('zzj.nb.log1','midnight',3600,0)
level=DEBUG
formatter=simpleFormatter

[formatter_simpleFormatter]
format=%(asctime)s|%(levelname)+8s|%(filename)s[:%(lineno)d]|%(message)s
datefmt=%Y-%m-%d %H:%M:%S  #设置时间输出格式
---------------------------------------------

【logging字典文件配置】后续有需要在了解把
 logging.config.dictConfig({"logger":"root"....})             # 读取字典文件


"""

import logging
import logging.config as log_config
import sys

# sys模块
print(sys.path)
print(sys.argv)


# logging模块（编程版
def code_log():
    # 记录器
    logger = logging.getLogger('zzj.nb.cls')
    logger.setLevel(logging.DEBUG)
    # 必须设置为两个handler中级别更低的

    # 处理器handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)

    # 没有给handler指定日志级别，将使用logger的级别
    fileHandler = logging.FileHandler(filename='zzj.nb.log')
    consoleHandler.setLevel(logging.INFO)

    # formatter格式
    formatter = logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)-10s:%(lineno)s|%(message)s")
    # 里面的8，10实现了占位对齐

    # 给处理器设置格式
    consoleHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    # 记录器要设置处理器
    logger.addHandler(consoleHandler)
    logger.addHandler(fileHandler)

    # 定义一个过滤器
    flt = logging.Filter("zzj.nb")

    # 关联过滤器
    logger.addFilter(flt)
    fileHandler.addFilter(flt)

    # 打印日志的代码
    # logging.debug()#不能使用这个了！！！会使用WARNING的版本，不会用之前的记录器
    logger.debug("this is a debug log")
    logger.info("this is a info log")
    logger.warning("this is a warning log")
    logger.error("this is a error log")


# logging模块（配置版
def config_log():
    logging.config.fileConfig('logging1.conf')
    logger = logging.getLogger('zzjnb')
    try:
        int("abc")
    except Exception as e:
        logger.error(e)  # 打印简单错误信息
        logger.exception(e)  # 打印详细的错误信息 ✔✔


if __name__ == '__main__':
    config_log()
