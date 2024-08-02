""" 计算/匹配/格式转换 等其他层面模块
【math】
 数学常量：‌
math.pi          # ‌表示圆周率π的值。‌
math.e           # ‌表示自然对数的底数e的值。‌
math.inf         # ‌表示正无穷大的数。‌
 幂函数和对数函数：
math.exp(x)          # ‌返回e的x次方。‌
math.expm1(x)        # ‌返回e的x次方减1。‌
math.log(x, base)    # ‌返回x的对数，‌可选参数base指定对数的底数，‌默认为e。
 三角函数：‌
math.sin(x)、‌math.cos(x)、‌math.tan(x)：‌分别返回x的正弦、‌余弦、‌正切值。‌
 取整和求和函数：‌
math.floor(x)        # ‌返回小于或等于x的最大整数。‌
math.ceil(x)         # ‌返回大于或等于x的最小整数。‌
math.fabs(x)         # ‌返回x的绝对值。‌
math.fsum(iterable)  # ‌返回可迭代对象中所有值的精确浮点数和，‌避免了精度损失。‌

【random】
 random.random()                 # 产生一个随机0~1之间的随机小数
 random.randrange(a,b,step)      # 生成[a,b]之间的随机数，并且可以指定步长
 random.randint(a,b)             # 产生[a,b]之间的随机数
 random.choice(['zzj','lzy','hjy'])      # 从指定的范围内选择一个随机数
 random.shuffle(['zzj','lzy','hjy'])     # 打乱顺序

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

【json】编码和解码json对象。D:\\IdeaWorkspace\\JavaWeb\\ajax\\src\\main\\java\\ajax\\UA01.java
 json.dumps(data,skipkeys=,ensure_ascii=,ensure_ascii=,separators=,sort_keys=,)             # 将python对象序列化为json编码字符串，通常都不需要传参
                                                                                                skipkeys如果遇到某些非法格式的Python数据类型，则抛出TypeError异常。如果skipkeys为True，这些非法格式的数据类型将被跳过，不会引发TypeError异常，默认值为False。
                                                                                                ensure_ascii默认True，它保证输出的每个字符都是ASCII字符。如果有些字符不能被编码成ASCII字符，它们会被转义为Unicode转义字符。
                                                                                                ✔ indent顾名思义，这个参数用于控制缩进格式。如果它的值是一个非负整数，输出的JSON字符串就会分行缩进。如果它的值为None，默认不缩进。
                                                                                                separators序列化之后的字符串中不同部分的分隔符。默认为(','和':')。
                                                                                                ✔ sort_keys用于指定是否按照键进行排序，默认为False。
 json.loads(data)                                       # 将一个json格式的字符串解码为python对象（字典、列表、布尔型，具体取决于json格式字符串中包含的内容。。。通常都是解码为字典，因为json格式字符串长得和字典是很像的
 json.dump(data,fp)                                     # 将python对象序列化为json格式的字符串并写入到文件中（如果是列表、布尔型等其他类型，就是直接外边加双引号，如果是字典类型，会把原先的单引号改为双引号，进行一些格式化操作）
                                                            fp = open('文件名','w')
 json.load(fp)                                          # 从一个文件中读取json数据
 字典和json格式的字符串格式是很像的，区别在于字典的键是单引号，json格式字符串是双引号
  并且json格式的字符串会把原先布尔类型的大写转换为小写，True --> true
 json.JSONEncoder和json.JSONDecoder是json模块中用于自定义json编码和解码过程的类。如果需要将一个自定义类序列化为json字符串或将json字符串反序列化为自定义类对象，则可以通过继承json.JSONEncoder和json.JSONDecoder来实现自定义的转换过程。
  https://blog.csdn.net/Code_and516/article/details/131181532

"""
import json
import math
import random
import re



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


# math模块
print(math.log(2,2))


# random模块
ran1 = chr(random.randint(65, 90))  # 产生随机大写字母，chr是将ascill码转换为字母
ran2 = chr(random.randint(97, 122))  # 产生随机大写字母
print(ran1, ran2)


# json模块,将字典转换为json格式的字符串
data = {
    "name": "张三",
    'age': 18,
    "hobbies": ["reading", "music"],
    "info": {
        "address": "北京市朝阳区",
        "phone": "18888888888"
    }
}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)
print(type(data))
print(type(json_str))
json_obj = json.loads(json_str)
print(type(json_obj))


list = [1,2,3]
s = json.dumps(list)
print(s)
print(type(s))