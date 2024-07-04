""" String
【String类】
 与java相同，字符串仍具有不可变性，即字符串之间的赋值，变更的是地址值指向
 python中没有变量的作用域，在循环中的局部变量仍能被外部使用

【常用方法】
【格式化输出】
（1）字符串中使用三引号可以保持格式输出，这个在java中也有~
print('''
    hello
    this fucking world
''')
（2）格式化输出
 格式化输出1
    print('%s说：' % name)
   %s表示字符串，底层会对其他格式变量进行强转
   %d表示数字int，不会强转，要求变量必须为int,float。若输入为浮点数，会被截断
   %f表示浮点数，不会强转，可以使用%.2f，表示四舍五入保留两位有效数字
 格式化输出2
    print('{0}今年{1}岁了'.format(n1,n2))      # 可以指定使用format中的第几个元素，不指定则按顺序默认排序
   String.format(变量名)                      # 使用字符串函数进行格式化输出，能够自动根据输入的变量类型进行输出。

【常用】
   +，*                   # +实现字符串拼接效果,*实现字符串复制
   print(r'\'哈哈哈\'')   # 在字符串前加r，可以保证转义字符不被转义，保留原格式输出
   str1 in str2           # 判断str1是否在str2中出现（连续出现），python中没有char类型，因此str1也可以是单词字符
    str1 not in str2
   .capitalize()           # 将字符串是第一个首字母转换为大写
     .title()                  将字符串中，每个单词的首字母大写
     .istitle()                判断字符串中的每个单词的首字母是否大写
     .upper()                  将字符串所有字母大写
     .lower()                  将字符串所有字母小写
   .encode('gbk')          # 将字符串按照指定格式编码，如utf-8,gbk等（转换为字节流，方便传输）
    .decode('gbk')          # 将字符串按照指定格式解码，如utf-8,gbk等
   .isalpha()              # 判断字符串是否是字母
     .isdigit()             # 判断字符串是否是数字(全由数字组成)
     .isnumeric()           # 判断字符串能否被转换为数字(字符串包含空格等也能转换为数字)
     .isspace()             # 判断字符串是否只包含空白
   seq.join(str2)          # 以seq为分割符，将str2进行连接(也可以对列表list中的元素以分隔符连接)。
   strip                   # 截掉字符串两端的空格或指定字符串
     lstrip()                # 截掉字符串左边的空格或指定字符串
     rstrip()
   list = split('seq',num)   # 以seq分割字符串，同java。可以指定分割的次数num
     .count(str2)              # 求字符串中指定字符串str2的个数
   .expandtabs(20)           # 字符串中默认制表符\t代表8个空格，使用该函数可以修改制表符所代表的空格数

【切片】
   str1[idx]              # ✔✔✔ 切片，取出字符串对应索引的字符（空格也算），类似与java的charAt方法
    str1[idx1:idx2]           输出对应索引范围[idx1,idx2)的字符串，类似matlab，索引都是从0开始
    str1[idx1:]               省略后面索引，表示取到字符串末尾。省略前面索引，表示从头开始截取
    str1[idx1:-1]             python中，-1表示的是字符串是最后一个字符！
    str1[idx1:idx2:step]      可以以固定步长进行切片，step=-1可以倒序输出（注意倒序时idx1要大于idx2）

【查找与替换】
   idx = str1.find(str2,beg,end)      # 在指定范围[beg,end)内查找是否有子字符串str2，如不输入范围，则全部查找。-1表示查找失败
    .rfind(str2)                        # 从右侧开始查找指定字符串，并返回索引
    .lfind(str2)                        # 从左侧开始查找指定字符串，并返回索引
    .index(str2)                        # index方法与find方法相同，区别是如果查找失败会报异常
    .rindex()
    .lindex()
    .startswith(str2)                   # 判断字符串是否以str2开头
    .endswith(str2)                     # 判断字符串是否以str2结尾
    .replace(str2,str3)                 # 将所有的str2替换为str3

【String类型转换】
 string ====> int、list、set、tuple类型，转换为list、set、tuple时则按照字符拆分
 int、list、set、tuple、dict、set类型  ====>  string类型，只不过list、set、tuple、dict、set转换时就是直接在其外边加了双引号
"""

# 0. 基础数据类型，在python中也是引用型变量
a = 5
b = 4
print(id(a))
b = a
print(id(b))


# 2. 格式化输出1(占位符形式)，不清楚java中有没有。。。可以解决int类型变量无法被拼接的问题，如下所示
person = "zzj"
address = "xxx"
num = 5
n = 18.55
print('收件人是：' + person + '，地址为：' + address)
print('收件人是：%s, 地址为：%s, 商品数量为%s' % (person, address, num))
print('几岁了哥%.1f' % n)
print()

# 3. 格式化输出2(format)
print('zzj今年{}岁了'.format(n))
