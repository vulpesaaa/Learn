from jiraOperation import *
from makeChart import *

server = 'http://10.25.10.110:8092/'
username = 'lumengzhen'  # jira账号密码
password = 'wt123456'

jql_ALL_BUG = """project = TES AND issuetype = Bug """  # sprint的jql，这里放了全部的BUG，可以按照需求调整

"""project = AUDIDA AND issuetype = 故障 ORDER BY created DESC""" # 审计的sprint 的jql ，待验证

"""实例化jiraOperation类"""
report = jiraOperation()
jira = report.loginJira(server=server, username=username, password=password)  # 登录jira

jira_result = report.searchIssues(jira, jql_ALL_BUG)  # 查询jql
jira_result_df = report.getDataframe(jira_result)  # 获取BUG信息，输出成DataFrame

"""执行jira数据的统计"""
count_status = report.count_status(jira_result_df)  # 统计BUG状态

count_statusAndassignee2 = report.count_statusAndassignee2(jira_result_df)  # 统计处理人完成BUG情况

count_components = report.count_components(jira_result_df)  # 统计每个模块的BUG

count_componentsAndseverity2 = report.count_componentsAndseverity2(jira_result_df)  # 统计每个模块不同严重程度的BUG

todo_bug = report.todo_bug(jira_result_df)  # 统计遗留BUG

"""实例化chart类"""
charts = chart()
bugStatus_pie = charts.bugStatus_pie(count_status)  # 生成图表--统计BUG状态
statusAndassignee2_bar = charts.statusAndassignee2_bar(count_statusAndassignee2)  # 生成图表--统计处理人完成BUG情况
components_bar = charts.components_bar(count_components)  # 生成图表--统计每个模块的BUG
componentsAndseverity2_bar = charts.componentsAndseverity2_bar(count_componentsAndseverity2)  # 生成图表--统计每个模块不同严重程度的BUG
bug_list = charts.bug_list(todo_bug)  # 生成图表--统计遗留BUG

"""渲染出html，可在report文件下查看到生成的html文件"""
charts.tab(bugStatus_pie, statusAndassignee2_bar, components_bar, componentsAndseverity2_bar, bug_list)
