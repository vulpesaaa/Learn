# @Author : lmz
# @File : jira_demo1.py
# @Project: Demo1
# @CreateTime : 2022/4/6 11:03:46
import re
import jira
from jira import JIRA

# 认证模式登录失败，暂时跳过（后续要研究搞出来）
# 17:17 搞出来，server的参数值为公司的jira服务器IP:端口号，上午的直接粘贴url地址认证失败
jira = JIRA('http://10.25.10.110:8092/', basic_auth=("lumengzhen", "wt123456"))
print(jira.projects())
# 在匿名模式下获取能看到的所有项目
# 使用server参数直接链接服务
jac = JIRA('https://jira.atlassian.com')
print(jac.projects())
projects = jac.projects()
print(projects[1])
# 对所有项目进行排序并返回2，3，4项key
keys = sorted(project.key for project in projects)[2:5]
print(keys)

# 获取一个问题
# jira.Issue，一个类
# issue = jira.Issue("JRA-1330")
# JIRA.issue一个方法，在说明文档中实际上用的这个方法，后面需要用到issue中的一个fields字段，Issue是没有的,且
# issue = JIRA.issue("JRA-1330")

issue = jac.issue("JRA-1330")
alt_comments = [
    comment for comment in issue.fields.comment.comments
    if re.search(r"atlassian.com", comment.author.key)
]
print(alt_comments[0].author.key)
print(issue.fields.comment.comments)
# 需要认证后才能添加
# jac.add_comment(issue,"Comments text")

# 分别获取问题中的几个字段，此处是总计、投票字段
summary = issue.fields.summary  # "Provide field-level security permissions"
votes = issue.fields.votes.votes  # "440"
print(summary)
print(votes)
# 仅获取问题的某些字段
issue = jac.issue("JRA-1330", fields='summary,comment')
print(issue)



