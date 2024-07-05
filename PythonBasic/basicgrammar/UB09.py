"""list、tuple、set共性
 作为存储多个数据的数据类型，list、tuple、set有一些共性。
  而dict的数据类型稍有不同，许多操作是仅针对其key值

 str1 in list1/tuple1/set1          # 判断str1是否为容器中的元素
 max(list1/tuple1/set1)             # 找出容器中的最大值
  sum(list1/tuple1/set1)             # 对容器中的元素进行求和
  len(list1/tuple1/set1)             # 求容器中元素的长度
 enumerate(list1/tuple1/set1)      # 转换为[(idx1,val1),(idx2,val2)...]的形式
 容器拆/装包
1、可以使用与容器中元素个数一致的变量个数，来对容器进行装包
   如 a,b,c = (1,2,3)
2、*变量名，表示可变参数，装包时使用列表对参数进行接收
   如 a,*b,c = (1,2,2,3)。接收后b=[2,2]
3、*容器表示对容器进行拆包
   如*{1,2,3}，表示对集合进行拆包了。拆包结果为1 2 3

"""

# 元组拆包
a, *b, c = (2, 5, 8, 9, 7)
print(a, b, c)
print(b)
print(*b)
print(*[5, 8, 9])

