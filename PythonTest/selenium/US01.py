""" Selenium概述
@Decription:
@Time : 2024/7/28 15:37
@Author:alexzhong

【Selenium概述】
Selenium 是一套 Web网站 的程序自动化操作 解决方案。
通过它，我们可以写出自动化程序，像人一样在浏览器里操作web界面。 比如点击界面按钮，在文本框中输入文字 等操作。
而且还能从web界面获取信息,然后用程序进行分析处理。

【Selenium原理】
自动化程序调用Selenium客户端库函数（比如点击按钮元素）
客户端库会发送Selenium命令 给浏览器的驱动程序（针对不同浏览器，需要安装不同浏览器驱动，可以理解为浏览器驱动就是翻译官，把我们的程序翻译给浏览器去执行）
浏览器驱动程序接收到命令后,驱动浏览器去执行命令
浏览器驱动程序获取命令执行的结果，返回给我们自动化程序

【安装】
pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple    # 安装selenium库
https://googlechromelabs.github.io/chrome-for-testing/              # 安装浏览器驱动程序（尽量安装和当前chrome版本接近即可

【】示例如下
 wd = webdriver.Chrome(r'D:\chromeDriver\chromedriver.exe')                       # 创建 WebDriver对象，并指明地址使用chrome浏览器驱动
  wd = webdriver.Chrome(service=Service(r'D:\chromeDriver\chromedriver.exe')       # selenium4.x版本写法。创建 WebDriver 对象，指明使用chrome浏览器驱动
 wd.get('https://www.baidu.com')          # 打开网址
 wd.quit()                                # 关闭浏览器
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 对象，指明使用chrome浏览器驱动，实际上这行代码开启，浏览器就被开启了
wd = webdriver.Chrome(r'D:\chromeDriver\chromedriver.exe')

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

# 程序运行完会自动关闭浏览器，就是很多人说的闪退
# 这里加入等待用户输入，防止闪退
input('等待回车键结束程序')
wd.quit()