"""list、tuple、set、dict等容器共性
【共同函数】针对list、tuple、set
 str1 in list1/tuple1/set1          # 判断str1是否为容器中的元素
 max(list1/tuple1/set1)             # 找出容器中的最大值
  sum(list1/tuple1/set1)             # 对容器中的元素进行求和
  len(list1/tuple1/set1)             # 求容器中元素的长度
 enumerate(list1/tuple1/set1)      # 转换为[(idx1,val1),(idx2,val2)...]的形式

【容器拆/装包】
1、可以使用与容器中元素个数一致的变量个数，来对容器进行装包
   如 a,b,c = (1,2,3)
2、*变量名，表示可变参数，装包时使用列表对参数进行接收
   如 a,*b,c = (1,2,2,3)。接收后b=[2,2]
3、*容器表示对容器进行拆包
   如*{1,2,3}，表示对集合进行拆包了。拆包结果为1 2 3
4、**{}表示对字典进行拆包，但这种拆包方式仅用于对**kwargs赋值
5. 函数入参中
*args，表示可填入任意参数，填入参数用元组接收
**kwargs，表示要求填入关键字参数，填入参数用字典接收
   函数体中
*args，表示拆包的数据，即拆包后再赋值
**kwargs，表示拆包的数据

【推导式】针对列表list、set、dict。通过简单处理将 旧的容器 ==> 新的容器。主要用于简化操作
 [表达式 for 变量 in list if 条件]                  # 列表推导式
 (表达式 for 变量 in dict1 if 条件)                 # 元组推导式
 {表达式 for 变量 in dict1 if 条件}                 # 集合/字典推导式

--------------------
# 1)取出列表中长度大于3的名字，将其首字母大写后赋值给新列表
names = ['zzj','alex']
result = [name.capitalize() for name in names if len(name)>3]
--------------------
# 2)取出0~5内的偶数，分别与0~5内的奇数组成元组，并存储于列表中
# 从本例中可以看出， for..if..for..if 是层层递进的关系！!!
result2 = [(i,j) for i in range(5) if i % 2 == 0 for j in range(6) if j % 2 != 0]
--------------------
# 3)薪资大于5000则加200,薪资小于5000则加500。。。由于涉及到if..else的同级操作，所以利用三元表达式置于表达式处操作
dict1 = {'name': 'tom1', 'salary': 5000}
dict2 = {'name': 'tom2', 'salary': 8000}
dict3 = {'name': 'tom3', 'salary': 4500}
dict4 = {'name': 'tom4', 'salary': 3000}
list2 = [dict1, dict2, dict3, dict4]

result = [(dic['salary']+200 if dic['salary']>5000 else dic['salary']+500) for dic in list2]  # 如此操作会将薪资取出后作为新列表返回
result = [{'name':dic['name'], 'salary':(dic['salary']+200 if dic['salary']>5000 else dic['salary']+500)} for dic in list2]  # 以原始列表相同格式返回
--------------------
# 4) 把list1的元素取出来加2放到set中，即完成去重
list1 = [1,1,2,3,4,5]
{x+2 for x in list1 if x>=1}
--------------------
# 5) 字典推导式，将字典的key和value颠倒
result = {value:key for key,value in dict1.item}
"""

# 元组拆包
a, *b, c = (2, 5, 8, 9, 7)
print(a, b, c)
print(*b)
print(*[5, 8, 9])

# 元组拆包2
def bb(a, b, *c, **d):
    print(a, b, c, d)

bb(1, 2)
bb(1, 2, 3, 4)
bb(1, 2, x=100, y=200)
# bb(1, 2, a=100, y=200)  # 注意，由于变量a已经使用，无法重复赋值。所以报错

# 推导式示例1
names = ['zzj', 'alex']
result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 推导式示例2
# 薪资大于5000则加200,薪资小于5000则加500
dict1 = {'name': 'tom1', 'salary': 5000}
dict2 = {'name': 'tom2', 'salary': 8000}
dict3 = {'name': 'tom3', 'salary': 4500}
dict4 = {'name': 'tom4', 'salary': 3000}
list2 = [dict1, dict2, dict3, dict4]

result = [(dic['salary']+200 if dic['salary']>5000 else dic['salary']+500) for dic in list2]  # 如此操作会将薪资取出后作为新列表返回
print(result)
result = [{'name':dic['name'], 'salary':(dic['salary']+200 if dic['salary']>5000 else dic['salary']+500)} for dic in list2]  # 以原始列表相同格式返回
print(result)