""" 接口测试
@Decription:
@Time : 2024/8/3 13:00
@Author:alexzhong
【接口测试概述】
 依据接口规范，写出测试用例，
  使用软件工具，直接通过消息接口 对 被测系统 进行消息收发
  验证被测系统行为是否正确
 目前的软件系统之间的消息接口大部分是基于 HTTP 协议收发的。
  HTTP协议的特点是，客户端发出一个HTTP请求给 服务端，服务端就返回一个HTTP响应。好像程序的API调用。
  所以 接口测试 通常又被称之为 API接口测试 或者 WEBAPI接口测试
 通常并不是所有的接口都需要测试，内部接口，即内部子系统之间的接口，主要由开发人员自己进行测试
  而外部接口，即与另外的系统进行交互的接口(常由其他公司、部门开发)，测试工程师一定要进行测试
 获取接口文档，评审文档 —— 根据接口文档，写出测试用例 —— 使用软件工具进行验证

【request】
 接口测试需要工具和被测系统之间进行消息（通常是HTTP消息）的收发。基于HTTP的接口测试工具，常见的有Postman、Jmeter等
  都是用来构建HTTP请求消息，并且解析收到的HTTP响应消息，用户来判断是否符合预期
  (获取网页、图片、css 这些静态资源，服务端无需特别的数据处理便可以直接读取，并返回给客户端，这些通常不称为API接口消息
  我们所说的API接口请求消息，通常指服务端需要进行处理，比如：对请求的权限检查、从数据库中读出数据、进行信息过滤等，最后在HTTP响应中返回给客户端的消息)
  当然，我们完全可以使用Python的requests库，自己写代码发送接收HTTP请求
 pip install requests
 response1 = requests.get(url)        # 使用get方法(还有post、put..)发起http请求，返回一个Requests库里面定义的一个Response类的实例对象。 这个对象代表着响应消息。
 urlpara = {'wd':'iphone&ipad','rsv_spt':'1'}                 # 发送url请求参数，字典传参，如果参数值中有一些特殊符号，还是建议用这种方式
  requests.get('https://www.baidu.com/',params=urlpara)         # 实际上如果参数短的话是可以直接用，url+问号+参数1&参数2（urlencoded格式），直接写在url地址中，就不需要使用字典传递
 requests.get('https://www.baidu.com/',headers=heapara)       # 发送请求头，同理，我们可以使用字典的方式向请求头headers中的传参

【reponse】
 response1 = requests.get(url)
 response1.text                       # 得到响应体的字符串形式。requests会根据响应头(如 Content-Type的编码格式)对响应体进行解码，但是有时候，服务端并不一定会在消息头中指定编码格式
                                         这时可以在调用response1.text之前指定编码格式。即response.encoding='utf8'
 response1.content                    # 得到响应体的原始字节串，如有必要可以直接对获取的字节串对象进行解码response.content.decode('utf8')
 dict1 = response1.json()             # 响应消息体格式，通常以json字符串居多。为了方便处理响应消息中json格式的数据，我们通常需要将json格式字符串转化为python对象。。这实际上相当于 json.loads(response.content.decode('utf8'))
 response1.status_code                # 得到返回的状态码
 headers = response1.headers          # 响应头headers对象是一个继承自字典的子类对象

【构建消息体】Web API接口中，请求体采用什么格式，是由开发人员设计的决定的，主要是这3种： urlencoded ，json ， XML。
-----------------xml格式
payload = '''
<?xml version="1.0" encoding="UTF-8"?>
<WorkReport>
    <Overall>良好</Overall>
    <Progress>30%</Progress>
    <Problems>暂无</Problems>
</WorkReport>
'''
# Requests默认会使用 latin-1 编码格式为字节串放到http消息体中，然后发送出去。而例子中里面包含中文，不能用缺省 latin-1编码，所以我们将字符串对象用utf8编码为字节串对象传入给data参数
# 这是一个通用方法，下方的格式也能使用.encode的方式进行编码
r = requests.post("http://httpbin.org/post", proxies=proxies, data=payload.encode('utf8'))

-----------------urlencoded格式，见上方传递url请求参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
# 抓包可以看见，在使用urlencoded格式构建消息体后，会自动在请求头中指定明了请求体格式Content-Type: application/x-www-form-urlencoded

-----------------json格式
payload = {
    "Overall": "良好",
    "Progress": "30%",
    "Problems": [
        {
            "No": 1,
            "desc": "问题1...."
        },
        {
            "No": 2,
            "desc": "问题2...."
        }
    ]
}
# 注意要dump成一个json格式字符串进行传参
r = requests.post("http://httpbin.org/post", data=json.dumps(payload), proxies=proxies)
# 也可以将 数据对象直接传递给post方法的 json参数，如下
# r = requests.post("http://httpbin.org/post", json=payload, proxies=proxies)


"""
import requests
response = requests.get("http://mirrors.sohu.com/")
print(response.text)
