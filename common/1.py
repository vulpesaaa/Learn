#!/usr/bin/env python
# encoding: utf-8
from jira import JIRA
import time

jac = JIRA('http://xxx.xxx.xx.xxx:8080', basic_auth=('xxx', 'xxxyyy'))
issue_list1 = []
for i in range(1000, 2000):
    issue_list1.append({
        'project': {'key': 'TE'},
        'summary': "[%s]summary bulk added by api" % i,
        'description': '0',
        'issuetype': {'id': 10007}
    })


def func_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("call %s, time: %f" % (func.__name__, end - start))
        return result

    return wrapper


@func_time
def create_issues(issue_list2):
    # 批量创建
    issues = jac.create_issues(field_list=issue_list1)
    print(len(issue_list2))


@func_time
def search_one_issue():
    # 搜索指定的一个issue
    jra = jac.project('TE')
    a = jac.search_issues('project=TE and key = TE-400')


@func_time
def search_issues():
    # 批量搜索
    issues = jac.search_issues('project=TE', maxResults=600)
    print(len(issues))


@func_time
def update_one_issue():
    # 更新指定的一个issue
    myissue = jac.issue('TE-400')
    issueupdate = {
        'summary': 'test1001',
        'description': 'update_for_myisue'
    }
    myissue.update(issueupdate)

    a = myissue.fields()
    if a.summary == issueupdate.get('summary'):
        print("true")
    else:
        raise RunnerError('error')


@func_time
def get_issue():
    # 获取一个issue issueid or issuekey
    myissue = jac.issue('12006')


@func_time
def delete_issues():
    # 批量删除
    issues = jac.search_issues('project = TE AND description ~ "0"')
    for i in issues:
        i.delete()


@func_time
def delete_one_issue():
    # 删除一个指定的issue
    myissue = jac.issue('TE-1')
    myissue.delete()


create_issues(issue_list1)
search_one_issue()
search_issues()
update_one_issue()
get_issue()
delete_issues()
delete_one_issue()
