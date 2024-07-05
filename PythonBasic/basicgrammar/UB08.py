""" 集合set{}
 与java中的set相同，用于存储无序且不重复的元素
 注意set和dict都是使用{}，空集合表示的是字典
  区别是 set：{元素1,元素2,元素3,...}   而  字典：{key:value,key:value,...}

【常用方法】
【符号运算】
   set1 == set2             # 判断set1和set2中的元素是否完全一致（只有元素一直即相等，无需顺序一直
   set1 - set2              # 差集。返回set1中，与set2不同的元素（区别是谁减谁）
    set1.difference(set2)      作用同减号
    set1.difference_update(set2)找到差集并赋值给set1，直接改变set1中的值
   set1 ^ set2              # 对称差集，返回两个集合中的不同元素
    (set1|set2)-(set1&set2)     作用相当于对称差集
   set1 & set2              # 交集，返回set1和set2中相同的元素
    set1.intersection(set2)    作用同&号
   set1 | set2              # 并集
    set1.union(set2)           作用同|号

【类型转换】
   set(list1)            # 将list1转换为set，并去除其中的重复元素
【增】
   .add()                # 增加单个元素(无序)。
    .add(tuple1)           # 如果添加的为元组，则将tuple1整体视为一个元素加入
   .update()             # 增加多个元素
    .add(tuple1)           # 如果添加的为元组，则将tuple1拆分为单个元素后依次无序加入
【删】
   .remove(element1)     # 删除指定元素，若指定元素不存在，则报错
    .discard(element1)     # 类似remove，删除指定元素，若指定元素不存在不会报错
   .pop()                # 随机删除元素，但在元素中通常会去删除第一个元素
   .clear()              # 清空集合

【set类型转换】
 list、tuple可以转换为set

"""
set1 = {1, 2, 3}
set2 = {2, 1, 3}
print(set1 == set2)
# 集合属于不可变数据类型
print(id(set1))
set1.add(4)
print(id(set1))
# 集合遍历1
for i in set2:
    print(i)
# 集合遍历2，实际上枚举类型就是遍历时把集合{2, 1, 3}转换为[(0,1),(0,2),(0,3)]的格式，见列表
for idx, val in enumerate(set2):
    print(idx, val)


