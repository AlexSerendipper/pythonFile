""" 字典{}
 字典类似于java中的Map类型，对应key-value的形式。key值在字典中是唯一的

【常用方法】
   max(tuple1)                         # 找出元组中的最大值
   dict([tuple1,tuple2])               # 强制类型转换，将tuple1作为键，tuple2作为值，转换为字典，，（示例中的列表也可以换成元组）
    dict([(1,2),(3,4),(5,6),(7,8)])     # 当元素成对出现时也能完成转换，格式为{1:2,3:4,5:6,7:8}
   element1 in dict1                   # 判断元素是否在字典的key值中出现

【增/改】
   dict1[key1] = value1              # 如果字典中存在同名键值，则覆盖。否则新增
   dict1.update(dict2)               # 字典合并，同key的覆盖，不同key的新增

【查】
   value1 = dict1[key1]              # 根据对应的key1找到其value1值，找不到则报错
   dict1.get("key1",defaultValue)    # 根据对应的key1找到其value1值，如果找不到（且没有设置默认值）则返回空值
   .fromkeys(list1,defaultValue)     # 强制转换。将列表中的值作为key，转换为字典（value为默认值，不设置默认值则为none）

【删】
   del dict1['key1']                 # 删除指定key1的item，找不到则报错
   .pop('key1',defaultValue)         # 弹出指定key1的item，如果找不到（且没有设置默认值）则返回空值
   .popitem()                        # 随机弹出字典中的item，通常是从末尾开始删除！
   .clear()                          # 清空字典

【遍历】
for key1 in dict1:                    # 默认遍历的是字典的key1。相当于dict1.keys()
for key1,value1 in dict1.items():     # 同时遍历字典的key1和value1。items为列表中包含元组的形式，因此也可以一个个元组的遍历
for value1 in dict1.values():         # 遍历字典的value1值。dict1.values()返回列表格式的值

"""
dict1 = {'zzj': 100, 'lzy': 666}
print(dict1.items())
for value1 in dict1.values():
    print(value1)
