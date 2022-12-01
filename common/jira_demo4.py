# @Author : lmz
# @File : jira_demo4.py
# @Project: Demo1
# @CreateTime : 2022/4/6 17:19:32
#
#
import json

import numpy as np
from jira import JIRA
import pandas as pd

jac = JIRA(server='http://10.25.10.110:8092', basic_auth=("lumengzhen", "wt123456"))
# jac = JIRA('https://jira.atlassian.com')
# print(jac.projects())
bug_jql = 'project = "AUDIT" AND status = 打开'

# json_result=True返回JSON即字典类型，否则返回的是ResultList格式的列表
temp_json = jac.search_issues(bug_jql, json_result=True)
temp_List = jac.search_issues(bug_jql)
# total 和实际遍历的总数值不一致
print(temp_List.total)
c = 0
for te in temp_List:
    c = c + 1
print(c)

f = open('text.text', 'w')

sum_bug = 0
temp = jac.search_issues(bug_jql)
# with open("format_json.json", 'w') as write_f:
#     json.dump(temp_json, f, indent=4, ensure_ascii=False)

# 返回的字典中的所有键值
temp_json.keys()
temp_json['expand']
# 返回关键字issues的列表
issues_list = temp_json['issues']
# fields中的所有键的列表
issues_list[0]['fields'].keys()


# temp_json.expand
# # keys的类型是dict_keys，dict_keys是？？？
# keys = temp_json.keys()


def dumpjson_dict(dict_json):  # 传递过来的应是字典类型
    keys = dict_json.keys()  # 获取字典的所有键
    df1 = pd.DataFrame(keys)  # 当前层的键作为列名
    list2 = [j[i] for j in df1[col_name]]  # 存储对应上述key的value至列表推导式
    for key in keys:
        key_type = type(dict_json[key])
        key_unit = dict_json[key]
        # print(key_type)
        if key_type is str:
            print(1)
        elif key_type is int:
            print(2)
        elif key_type is list:
            print(3)
            dumpjson_list(key_unit)
        elif key_type is dict:
            print(4)
            dumpjson_dict(key_unit)


def dumpjson_list(list_json):
    print(len(list_json))  # 键值的类型是列表，输出当前列表中元素的数量
    for each in list_json:  # 对列表元素进行遍历
        each_type = type(each)
        print(each_type)
        if each_type is str:
            print(5)
        elif each_type is int:
            print(6)
        elif each_type is list:
            print(7)

            dumpjson_list(each)
        elif each_type is dict:
            print(8)
            dumpjson_dict(each)


dumpjson_dict(temp_json)

# 打开一个csv文件
demo1 = open('demo1.csv', 'w')
# 解析json格式的字典数据并写入到demo1.csv中
json.dump(temp_json, demo1)
