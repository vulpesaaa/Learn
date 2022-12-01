# @Author : lmz
# @File : jira_demo2.py
# @Project: Demo1
# @CreateTime : 2022/4/6 15:27:36


# -*- coding: utf-8 -*-
import jira
from selenium import webdriver

# import Write_excel
#
# wr = Write_excel.Write_excel('SasaiBugStatistic.xlsx')
# sheetNames = ['PaymentProduct', 'LiveProduct', 'OthersProduct', 'AllProduct', 'PaymentPreProduct', 'LivePreProduct',
#               'OthersPreProduct', 'AllPreProduct']
# driver = webdriver.Chrome()
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import re
from jira import JIRA
from jira.client import JIRA


# 打开页面
# 1. 打开登录页面 http://10.25.10.110:8092/login.jsp
# 2. 查找登录用户名输入框，输入用户名
# 3. 查找登录用户密码输入框，输入用户密码
# 4. 查找提交按钮，输入用户名
# 5. 打开问题页 http://10.25.10.110:8092/issues/?filter=-4
# 6. 退出驱动
def openPage():
    s = Service(r'D:\drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get('http://10.25.10.110:8092/login.jsp')
    sleep(2)
    el = driver.find_element(By.ID, "login-form-username")
    el.send_keys("lumengzhen")
    el = driver.find_element(By.ID, "login-form-password")
    el.send_keys("wt123456")
    el = driver.find_element(By.ID, "login-form-submit")
    el.click()
    sleep(5)
    driver.get('http://10.25.10.110:8092/issues/?filter=-4')
    sleep(2)
    driver.quit()


# openPage()
# 密码我复制了然后就好了？？？？？？为啥之前输入的就不行？？
# 问题出现在server而不是用户密码
jac = JIRA(server='http://10.25.10.110:8092/', basic_auth=("lumengzhen", "wt123456"))
print(jac.projects())


