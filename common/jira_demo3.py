# @Author : lmz
# @File : jira_demo3.py
# @Project: Demo1
# @CreateTime : 2022/4/6 17:19:32
# 认证失败例子验证，server的参数值为公司的jira服务器IP:端口号，直接粘贴url地址会带多余的资源导致认证失败
# 留个疑问：直接复制url为啥会失败
from jira import JIRA
# fail
jac = JIRA(server='http://10.25.10.110:8092/issues/?filter=-4',basic_auth=("lumengzhen", "wt123456"))
print(jac.projects())
# pass
jac = JIRA(server='http://10.25.10.110:8092', basic_auth=("lumengzhen", "wt123456"))
print(jac.projects())
