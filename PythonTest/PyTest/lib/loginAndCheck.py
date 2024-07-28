""" 登录功能自动化
@Decription:
@Time : 2024/7/28 12:01
@Author:alexzhong
"""

from selenium import webdriver
import time

def loginAndCheck(username,password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get('http://127.0.0.1/mgr/sign.html')

    if username is not None:
        driver.find_element_by_id('username').send_keys(username)

    if password is not None:
        driver.find_element_by_id('password').send_keys(password)

    driver.find_element_by_css_selector("button[type='submit']").click()

    time.sleep(2)

    alertText = driver.switch_to.alert.text
    print(alertText)

    driver.quit()  # 关闭弹窗

    return alertText