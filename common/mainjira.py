from operjira import *

# 这个地方填写自己公司的jira地址和账号密码
jira_login = ['http://10.25.10.110:8092/', 'lumengzhen', 'wt123456']
jql = ["project = AUDIDA AND issuetype = 故障 ORDER BY created DESC"]
fields = ['components,summary,customfield_10903,labels']

if __name__ == '__main__':
    jira_finail_result = []
    # 登录jira
    jira = login_jira(jira_login[0], jira_login[1], jira_login[2])
    # 仅获取问题的某些字段
    jira_result = search_issues(jira, jql, max_results=500, fields=fields[0])
    # 分析字段
    jira_result = list(analytical(jira_result))
    jira_finail_result.append(jira_result)
    # 生成图表
    make(jira_finail_result)
