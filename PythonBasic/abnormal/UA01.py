"""
【异常概述】
 异常：在Java语言中，将程序执行中发生的不正常情况称为“异常” (开发过程中的语法错误和逻辑错误不是异常)

【异常处理】与java的try-catch非常类似
try:
    可能出现异常的代码
except 异常类型1:
    如果有异常执行的代码
except 异常类型2:
    如果有异常执行的代码
except Exception as err:
    print('出错啦！',err)                   # 打印错误信息
[else]:                                     # 可选项
    没有异常才会执行的代码
    所以需要使用else，在try中就不要使用return，否则就到达不了了
[finally]:
    无论是否存在异常都会被执行的代码

【抛出异常】raise
raise 异常类型1("错误提示信息")              # 主动抛出异常

"""


class excep():
    raise Exception("嘿嘿")
