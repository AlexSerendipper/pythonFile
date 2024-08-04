"""         
@Decription:fiddler
@Time : 2024/8/3 14:13
@Author:alexzhong

【fiddler】
 fiddler是常用的一款HTTP代理式抓包工具。
  ✔✔✔ fiddler启动后，会启动一个代理服务器（同时设置自己作为系统代理，即http=127.0.0.1:8888;https=127.0.0.1:8888），监听在8888端口上。
       (可以在系统设置-代理中，看到已经手动代理已经被fiddler自动设置)
  ✔✔✔ HTTP客户端需要设置fiddler作为代理，把HTTP请求消息发送给fiddler，fiddler再转发HTTP消息给服务端。
  ✔✔✔ 服务端返回消息也是先返回给 fiddler，再由fiddler转发给 客户端。
  由于请求响应消息都经过了fiddler，fiddler自然就抓到了 HTTP请求和响应
 fiddler过滤器配置
 Filters - Use Filters - show only the following Hosts，输入127.0.0.1;*.sohu.com，点击change not yet saved保存。。。表示只抓取发送给127.0.0.1以及以sohu.com结尾的http请求的包
   Show only if URL contains,可以输入关键词，只抓取url中包含指定关键词的http请求
 fiddler查看抓取信息
 Inspector - 点击上半区和下半区的raw标签，可以查看整个 HTTP请求和响应的具体内容。


【客户端设置fiddler作为代理】
【浏览器抓包】浏览器作为客户端
chrome浏览器默认会使用系统代理！！由于fiddler启动后会将自己布置为系统代理，因此chrome浏览器发送的http请求都能被抓到
但是浏览器本身F12打开的开发者窗口，就可以很方便的看到HTTP消息，所以不需要fiddler抓包。
【requests抓包】python作为客户端
 proxies = {'http': 'http://127.0.0.1:8888','https': 'http://127.0.0.1:8888'}   # 指定fiddler为代理
 response = requests.get('http://mirrors.sohu.com/', proxies=proxies)           # 发送请求时先发送给fiddler，也即使用fiddler作为客户端代理
 注意，如果抓 https 网站的包，需要在电脑上安装Fiddler证书，tools—option—HTTPS-Actions->Trust Root Certificate
  然后，还需要执行命令 pip install python-certifi-win32 安装一个第三方库 ，这样会让python使用本地系统安装的证书。此时就可以实现抓取https
  或者使用如下方式，让Requests不去验证证书的合法性（不安全）
 response = requests.get('https://www.baidu.com/', proxies=proxies, verify=False)
【手机抓包】手机作为客户端，以苹果手机为例
1、首先确保手机使用的 WIFI和运行fiddler的电脑 必须使用同一个子网，比如使用同一个WIFI信号连接。
2、fiddler设置及安装证书，注意设置完成后一定要重启fiddler
   tools—option—connections-allow remote compute to connect，即设置允许远程机器连接自己(使用自己作为代理，
   tools—option—HTTPS-选中capture https connects以及decrypt https traffic，第一次会弹出证书安装提示，若是没有，点击Actions->Trust Root Certificate
   如果你的APP访问的服务使用的是自签名的非正式证书，需要把下面的“Ignore server certificate errors”勾选上。
   设置后fiddler就可以截获https请求，注意设置后重启fiddler
   Actions->open windows certificate Manager 可以查看一下证书是否已经正确安装
3、由于HTTPS协议的安全性机制要求，通常来说，代理只有拥有服务端证书对应的私钥，才能查看到解密客户端通信的信息，而手机端就需要把Fidder证书安装为受信任的根证书，才能使用它进行代理抓包
   所以在浏览器访问 fiddler所在机器的IP地址:代理端口，会看到fiddler提供的页面，下载安装证书
   安装后general - about -certificate trust setting，信任fiddler证书
   手机wifi处设置手动代理，即可通过fiddler进行抓包




"""
import requests

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}

import requests, json

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

r = requests.post("http://httpbin.org/post", data=json.dumps(payload),proxies=proxies)
# 也也可以将 数据对象直接传递给post方法的 json参数，如下
# r = requests.post("http://httpbin.org/post", json=payload)
