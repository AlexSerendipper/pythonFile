"""         
@Decription:session的使用，基础知识详见javaweb-session
@Time : 2024/8/4 13:52
@Author:alexzhong

【session对象】
session1 = requests.Session()        # 获取session对象
session1.proxies.update("")          # session对象使用代理
response1 = session1.post()          # 用session对象发送请求，此时session1对象中的数据实际上就是在会话层面上共享
                                       可以在response1中看见Set-Cookie字段，表示通知客户端以cookie的形式存储sessionId。与javaweb-session基础知识相符

"""
import requests

# 打印HTTP响应消息的函数
def printResponse(response):
    print('\n\n-------- HTTP response * begin -------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print('')

    print(response.content.decode('utf8'))
    print('-------- HTTP response * end -------\n\n')


# 创建 Session 对象
s = requests.Session()
# 通过 Session 对象 发送登录请求，此时session1对象中的数据实际上就是在会话层面上共享
response = s.post("http://127.0.0.1/api/mgr/signin",
                  data={
                      'username': 'byhy',
                      'password': '88888888'
                  })

printResponse(response)

# 通过 Session 对象 发送添加客户请求，实际上在百叶黑羽后台校验了session1中的登录数据，如果正确才能添加客户成功！
response = s.get("http://127.0.0.1/api/mgr/customers",
                 params={
                     'action'    :  'list_customer',
                     'pagesize'  :  10,
                     'pagenum'   :  1,
                     'keywords'  :  '',
                 })

printResponse(response)