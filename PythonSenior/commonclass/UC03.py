""" 工具模块
【hashlib】加密函数，其中md5、sha1、sha256是不可逆的。。。base64加密是可逆的
 md55 = hashlib.md5(str1.encode('utf-8'))       # 以md5的加密方式对中文进行加密。首先必须要对中文进行utf-8编码，返回值为哈希类型
 md55.update(str1.encode('utf-8'))              # 可以使用update()函数补充需要哈希的数据。。重复调用update()方法相当于单次调用并传入所有参数的拼接结果
 md55.hexdigest()                               # 将哈希对象转换为16进制的字符串

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

【calendar】日历模块，用的较少
 calendar.month(2021, 1)       # 输出2021年01月日历

【copy】
 copy.copy()               # 浅复制。它复制了对象的容器(list,set,dict)，对于容器中的元素，如果是不可变类型(string，int，元组)，则创建这些元素的新实例.
                              如果是可变类型（如列表、字典），则进行浅复制，即仍然会使用原始容器中元素的引用
 copy.deepcopy()           # 深复制。不管元素是可变还是不可变类型，都创建这些元素的新实例.

"""
import hashlib
import copy

# hashlib模块
str1 = "我草你的"
print(hashlib.md5(str1.encode('utf-8')).hexdigest())


# 浅复制示例
original_list = [1, 2, [3, 4]]
copied_list = copy.copy(original_list)

original_list.append(5)
original_list[0] = 5
original_list[2].append(5)

print(original_list)  # 输出: [1, 2, [3, 4, 5], 5]
print(copied_list)  # 输出: [1, 2, [3, 4, 5]]

# 深复制示例
original_dict = {'a': 1, 'b': [2, 3]}
deep_copied_dict = copy.deepcopy(original_dict)

original_dict['b'].append(4)
print(original_dict)  # 输出: {'a': 1, 'b': [2, 3, 4]}
print(deep_copied_dict)  # 输出: {'a': 1, 'b': [2, 3]}
