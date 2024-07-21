""" pymysql连接mysql
 pip install pymysql
【DML之增删改】
 conn = pymysql.connect(host='', port=3306, user='', passwd='', db='', charset='utf8')         # 建立数据库连接，需要指定具体的数据库
 with conn.cursor() as cursor:                                                                 # 和文件os操作一样，使用完coursor后会自动关闭
      result = cursor.execute("sql语句")                                                         # 传入sql语句，并且 result为受到影响的行数。
                                                                                                   和java一样，不用使用字符串拼接的方式，使用占位符的方式来撰写sql，否则有sql注入风险
                                                                                                   鉴于python的占位符语法，可以很方便的实现动态sql！
 conn.commit()                                                                                 # 注意conn默认是开启事务的，必须手动提交才会完成更改
 conn.rollback()                                                                               # 如果异常需要回滚。

【DML之查询】
 查询操作通常不涉及回滚，查询时不需要返回result
 conn = pymysql.connect(host='', port=3306, user='', passwd='', db='', charset='utf8', cursorclass=pymysql.cursors.DictCursor)         # 建立数据库连接，需要指定具体的数据库，指定使用dictCursor，则查询结果为字典形式（默认为元组形式
 cursor.execute("查询语句")
 conn.fetchone()                                # 查询后返回查询的一条记录
 conn.fetchall()                                # 查询后返回查询的所有记录
                                                    注意游标指向查询结果的一行，如果先使用了.fetchone()，然后.fetchall()的结果中不会包含之前的查询信息（相当于的遍历不回头
                                                    如果使用和java面向对象一样的思想，如果有一个 类的属性名 和 查询结果名一致，我们对查询结果(字典)进行拆包，直接赋值给类的对应构造器即可（没有java那么方便
 conn.fetchmany()                               # 查询后返回查询的一些记录

【快速插入】
1. 使用properties文件，从文件中读取的方式快速创建sql连接
2. 将连接信息写入__init__.py文件中，使用包名.变量名的形式调用

"""
import pymysql

with open("properties", 'r') as file:
    config = {line.strip().split("=")[0]: line.strip().split("=")[1] for line in file}
    host = config.get("host")
    port = config.get("port")
    port = int(port)
    user = config.get("username")
    passwd = config.get("password")
    db = config.get("db")


def insertTest():
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
    try:
        with conn.cursor() as cursor:  # 和文件os操作一样，使用完coursor后会自动关闭
            result = cursor.execute('insert into user(name, password,address,phone) values (%s, %s, %s, %s)',
                                    ("zzj", 123, 123, 123))
            if result == 1:
                print("添加成功")
                conn.commit()
    except pymysql.MySQLError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()


def selectTest():
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            cursor.execute('select * from user')
            for row in cursor:
                print(row)
    except pymysql.MySQLError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    selectTest()
