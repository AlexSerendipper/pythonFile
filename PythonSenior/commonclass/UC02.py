"""
【常用模块】
builtins               内建函数库，默认加载
math                   数学库
random                 生成随机数
time
datetime
calendar
hashlib                加密函数
copy                   拷贝
functools              常用工具
os                     操作系统
re                     字符串正则
sys                    python运行环境
multiprocessing        多进程
threading              多线程
json                   编码和解码json对象
logging                记录日志，调试


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

【sys】
 sys.path()               # 返回搜索路径，搜索时会按照列表中的路劲依次进行查找。
                             可以看出是先找自身包下的自定义模块，然后在去寻找系统路径下的
                             可以右键包，mark as source root，添加到系统的搜索路径当中
 sys.version()            # 打印python版本
 sys.argv()               # argument vector，获取命令行参数。这在编写需要与用户交互或需要外部输入的脚本时非常有用
                             java中也有这个传参，python中是在UC02-edit configurations-script parameters处进行传参


【time】
 time.time()              # 返回当前时间的时间戳
  time.ctime()             # 传入时间戳，返回时间的字符串格式
 time.sleep(seconds)      # 睡眠几s
 TT = time.localtime()    # 传入时间戳，不传入默认为当前时间。返回时间的元组格式
  time.mktime()            # 传入元组，转换为时间戳
  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())      # 将时间的元组格式转换为指定格式
 TT.tm_year              # 得到元组时间后，可以很方便得到年月日信息
  TT.tm_mon
 time.strptime('2019/06/20', '%Y/%m/%d')                   # 将字符串时间转换为元组时间


【datetime】time模块的升级版，底层还是使用time
 datetime.time.hour(12:00:00)  # 得到时间对象（类型是datetime.time类
 datetime.date(2024,7,14)      # 得到日期对象
  datetime.date.today()         # 返回当前日期，如2024-07-14（类型是datetime.date类
 datetime.datetime.now()       # 返回当前 日期及时间，（类型是datetime.datetime类
 datetime.timedelta(hours=2)   # 创建一个时间间隔，datetime.date对象以及datetime.datetime对象都可以与该时间间隔进行加减运算，‌得到新的日期


【random】
 random.random()                 # 产生一个随机0~1之间的随机小数
 random.randrange(a,b,step)      # 生成[a,b]之间的随机数，并且可以指定步长
 random.randint(a,b)             # 产生[a,b]之间的随机数
 random.choice(['zzj','lzy','hjy'])      # 从指定的范围内选择一个随机数
 random.shuffle(['zzj','lzy','hjy'])     # 打乱顺序


【hashlib】加密函数，其中md5、sha1、sha256是不可逆的。。。base64加密是可逆的
 md55 = hashlib.md5(str1.encode('utf-8'))       # 以md5的加密方式对中文进行加密。首先必须要对中文进行utf-8编码，返回值为哈希类型
 md55.update(str1.encode('utf-8'))              # 可以使用update()函数补充需要哈希的数据。。重复调用update()方法相当于单次调用并传入所有参数的拼接结果
 md55.hexdigest()                               # 将哈希对象转换为16进制的字符串

【第三方模块】首先需要在下方terminal终端输入pip xxx，对第三方模块进行安装，安装后才能使用import进行导入

【re模块】正则表达式，javaweb中，js的dom处讲到了这部分内容
 正则规则见java
 re.match(pattern1，str1)                      # 用于从字符串的 起始位置 匹配一个模式，如果匹配成功，则返回一个匹配的对象，否则返回None
 result = re.search(pattern1，str1)            # 从头到尾匹配模式，找到一个符合条件的就不会继续往下找
   result.span()                                # 返回被匹配内容的位置。
   result.group()                               # 返回被匹配到的内容
   result.group(2)                              # 如果正则中进行了分组匹配()，可以从结果中拿到不同组的匹配结果。如使用(\d{3})-(\d{8})去匹配 010-12345678，则result.group(2)的结果为12345678
 result = re.find(pattern1，str1)              # 从头到尾匹配模式，将所有符号条件的内容放到列表中返回
 re.sub('pattern1','新内容',str3)              # 替换功能，在str3中，只要匹配到符合的pattern1，都替换为新内容
                                                  新内容处可以传入函数，函数入参为匹配的结果，对匹配结果进行一些操作
 re.split('pattern1',str3)                     # 只要在str3中匹配到pattern1，就进行切割。切割结果以列表的形式返回

"""

import datetime
import hashlib
import re
import sys
import time
import random
# sys模块
print(sys.path)
print(sys.argv)

# random模块
ran1 = chr(random.randint(65, 90))  # 产生随机大写字母，chr是将ascill码转换为字母
ran2 = chr(random.randint(97, 122))  # 产生随机大写字母
print(ran1, ran2)

# hashlib模块
str1 = "我草你的"
print(hashlib.md5(str1.encode('utf-8')).hexdigest())

# re模块，匹配标签中的内容
str2 = "<h3>999<h3>"
result = re.match(r'<([\w]+)>(.+)<\1>', str2)
print(result)
print(result.group(2))
print(type(result.group(2)))

# def func(res):
#     num1 = res.group(2)
#     num2 = int(num1)+1
#     return str(num2)

res = re.sub(r'<([\w]+)>(.+)<\1>',lambda res:str(int(res.group(2))+1),str2)
print(res)