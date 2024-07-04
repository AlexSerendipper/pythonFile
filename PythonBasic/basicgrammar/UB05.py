""" 列表[]
【列表】
 python中的列表类似于java中是数组，区别是py中的列表是不需要指定长度的
 与字符串的下标格式相同，索引从0开始，-1结尾
 列表中可以包含列表，即二维列表

【常用方法】
   str1 in list1           # 判断str1是否为列表中的元素
   max(list1)              # 找出列表中的最大值
    sum(list1)               # 对列表中的元素进行求和
   sorted(list1,reverse=True)          # 对列表中的元素进行排序，默认为升序。改变了原列表
    .sort()                             # 对列表中的元素进行排序，默认为升序。改变了原列表
   list1 * x               # 将列表中的元素复制x倍
   list(range(1,10,3))     # 将指定的内容转换为列表
     list(str1)             # 将字符串拆分成单个字符，并转换为列表。。。整型对象无法进行转换！
   .reverse()             # 反转列表元素(改变原列表！！！
   .count(element1)       # 判断列表中出现element1的次数
   enumerate(list1)       # 以(idx,val)的格式枚举列表

【添加】
 list1.append()             # 从list1尾部追加
 list1.extend(list2)        # 列表的合并。把list2中的内容合并到list1中
 list1 + list2              # 使用+能够实现与extend相同的效果
 list1.insert(idx,element1)             # 将element1插入到指定位置idx

【删除】
   del list1[0]            # 使用del关键字进行列表元素的删除
     .remove(element1)      # 删除列表中第一次出现的指定元素element1，返回值为none。找不到要删除的元素则报异常
     .pop(idx)              # 删除列表中指定下标的元素，默认弹出最后一个元素！，返回值为弹出的元素。
     .clear()               # 清除列表

【切片】与字符串一样，同样支持切片操作
   list1[idx]              # ✔✔✔ 切片，取出对应索引的元素（空格也算）
    list1[idx1:idx2]           输出对应索引范围[idx1,idx2)的元素，类似matlab，索引都是从0开始
    list1[idx1:]               省略后面索引，表示取到元素末尾。省略前面索引，表示从头开始截取
    list1[idx1:-1]             python中，-1表示的是字符串是最后一个元素！
    list1[idx1:idx2:step]      可以以固定步长进行切片，step=-1可以倒序输出（注意倒序时idx1要大于idx2）

【列表类型转换】
 list ====> set、tuple、dict(转换为字典时需要list成对出现)
  set、tuple、dict(字典转换为列表时，只会将key值放入列表中) ====> list
"""

# 在列表中删除元素，常出现漏删问题，值得注意
list1 = ['hello', 'goods', 'gooo', 'world', 'digot', "alphago"]
i = 0
l = len(list1)
while i < l:
    if 'go' in list1[i]:
        del list1[i]
        l -= 1
        i -= 1  # 为避免露删，或者使用continue。
    i += 1
print(list1)

# count的使用
print(list1.count('hello'))

# enumerate的使用
test = enumerate(list1)
for i in test:
    print(i)