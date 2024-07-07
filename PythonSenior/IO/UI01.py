""" 文件操作
【IO操作】
 stream1 = open(file, mode='r', buffering=None, encoding='utf-8')         # file可以使用相对/绝对路径。返回IO流,默认mode为'rt'即读取文本文件
                                                                             默认使用utf-8方式解码文件
                                                                             mode还有'rb'，以二进制方式进行读取，详见源码处
                                                                             'a'，写操作时采样追加形式
 stream1.read()                         # 读取流中的文件，注意为一次性操作，无法二次读取流中的数据
  stream1.readline()                     # 读取一行内容，并加\n，第二次使用为读取第二行
  stream1.readlines()                    # 读取所有行，并保存到列表中
  stream1.write()                        # 写操作'w'，写入文件不存在则会自动创建。第一次写默认会覆盖源文件内容
                                           追加操作'a'，追加操作会往源文件后追加内容
                                           对同一个流进行多次写操作，不会覆盖上次写的内容，但无换行效果
  stream1.writelines(iterable)           # 可以一次性从可迭代体中写入多行
 stream1.name                          # 当前流的文件的完整路径
 stream1.close()                       # 关闭流

【文件复制】
 with open(file1,'rb') as stream1:               # 使用with+open格式，可以自动释放资源
      r = stream1.read()

      with open(file2,'wb') as stream2
         stream2.write(r)

【OS模块】
 path1 = os.path.dirname(__file__)                # 获取当前文件所在目录(绝对路径
  path1 = os.path.getcwd(__file__)                 # 获取当前文件所在目录(绝对路径，与上相同
 path2 = os.path.join(path1,文件名 )                       # 按照 path1/文件名 的方式拼接路径(可拼接多个，从而获得当前路径下文件的完整路径
  os.path.abspath(__file__)                        # 获取当前文件的绝对路径
  os.path.split(path1)                             # 根据输入的地址获取文件名(实际上就是截取了最后一个\后的字符串)
  os.path.splitext(path2)                          # 根据输入的地址获取文件的拓展名(.py等
  os.path.getsize(path2)                          # 根据输入的地址获取文件的大小，单位字节
  os.path.exists(path3)                            # 判断指定路径下是否存在文件/文件夹
 os.listdir(path1)                               # 输入文件目录，返回当前目录下的所有文件和文件夹的名称，并保存到列表中
 os.mkdir(path3)                                 # 在path3路径下创建一个文件夹
  os.rmdir(path3)                                  # 删除指定路径下的文件夹，只能删除空文件夹
  os.remove(path3)                                 # 删除指定路径下的文件(此处输入的是文件名
  os.chdir(path3)                                  # 切换到指定路径，切换后使用getcwd打印可看出。多用于与相对路径连用，
 isabs()                                         # 判断是否为绝对路径
   isfile()                                       # 判断是否为文件
   isdir()                                        # 判断是否为目录
"""
import os

# 读操作
stream = open(r'D:\桌面存放\1\hh.txt', encoding='utf-8')
result = stream.read()
print(result)

# 写操作
stream1 = open(r'D:\桌面存放\1\hh.txt', 'a', encoding='utf-8')
str = '\n敏敏臭宝\n'
stream1.write(str)
stream1.write('嘿嘿')

# os之删除目录操作（删除指定目录下的目录，其中包含文件
path = r'D:\桌面存放\2'
filelist = os.listdir(path)
print(filelist)
for file in filelist:
    path1 = os.path.join(path,file)
    os.remove(path1)
else:
    os.rmdir(path)

print("ok")