from jira import JIRA
import urllib3
import json
import pandas as pd

urllib3.disable_warnings()

"""
主要实现登录jira、查询jql、获取需要的BUG字段生成dataframe、统计BUG
"""


class jiraOperation:

    def loginJira(self, server, username, password):
        """
        登录jira
        :return: jira
        """

        jira = JIRA(server=server, basic_auth=(username, password))
        return jira

    def searchIssues(self, jira, jql, max_results=1000):
        ''' Search issues
        @param jql: JQL, str
        @param max_results: max results, int, default 100
        @return issues: result, list
        执行jql返回bug list
        '''
        try:
            issues = jira.search_issues(jql, maxResults=max_results)
            return issues
        except Exception as e:
            print(e)

    def getIssuesfield(self, jira):
        """
        获取BUG的所有字段，包括自定义字段
        :return:
        """
        field = jira.fields()
        for item in field:
            print(json.dumps(item, ensure_ascii=False))

    def getDataframe(self, jira_result):
        """
        生成数据明细
        :return:df
        """
        key_list = []
        summary_list = []
        priority_list = []
        severity_list = []
        assignee_list = []
        status_list = []
        components_list = []

        for issue in jira_result:

            key = issue.key  # BUG编号
            summary = issue.fields.summary  # BUG简述
            priority = issue.fields.priority  # 优先级
            ## customfield_10302 待验证，待验证
            customfield_10302 = issue.fields.customfield_10302  # 严重程度
            assignee = issue.fields.assignee  # 经办人
            status = issue.fields.status  # 状态
            if issue.fields.components == []:  # 如果BUG没有绑定模块，默认其他
                components = '其他'
            else:
                components = str(issue.fields.components[0])

            key_list.append(str(key))
            summary_list.append(str(summary))
            priority_list.append(str(priority))
            severity_list.append(str(customfield_10302))
            assignee_list.append(str(assignee))
            status_list.append(str(status))
            components_list.append(str(components))

        ipl_data = dict(key=key_list, summary=summary_list, priority=priority_list, severity=severity_list,
                        assignee=assignee_list, status=status_list,
                        components=components_list)  # 生成统计数据明细
        df = pd.DataFrame(ipl_data)
        return df

    def count_status(self, df):
        """
        BUG完成状态统计
        :param df:
        :return: status_set
        """
        status_set = {}
        status_groupd = df.groupby("status")

        for name, group in status_groupd:
            count = group["status"].count()
            status_set.setdefault(str(name), str(count))
        return status_set

    def count_statusAndassignee2(self, df):
        """
        处理人完成BUG统计
        可以实现根据人员分组并统计出每个人未解决和已解决的BUG数量
        :param df:
        :return: assignee_people_list, todo_list, done_list
        """
        assignee_people_list = []
        todo_list = []
        done_list = []

        for assignee, group in df.groupby('assignee'):
            assignee_people_list.append(assignee)
            status = group["status"]
            status_list = list(status)  # 输出每个人所有状态的数组

            # 统计各个状态在数组中出现的次数
            todo = status_list.count('待办')
            progress = status_list.count('处理中')
            resolved = status_list.count('已解决')
            rejected = status_list.count('Rejected')
            reopen = status_list.count('重新打开')
            close = status_list.count('完成')
            # 统计未解决和已解决的次数
            todo_item = todo + progress + reopen
            done_item = resolved + close + rejected
            # 未解决和已解决输出成数组
            todo_list.append(todo_item)
            done_list.append(done_item)
        return assignee_people_list, todo_list, done_list

    def count_components(self, df):
        """
        各模块BUG统计
        :param df:
        :return: components_set
        """
        components_set = {}
        components_groupd = df.groupby("components")

        for name, group in components_groupd:
            count = group["components"].count()
            components_set.setdefault(str(name), str(count))
        return components_set

    def count_componentsAndseverity2(self, df):
        """
        各模块BUG严重等级统计
        可以实现根据模块统计,输出每个模块BUG严重等级的统计
        :param df:
        :return: components_list, deadly_list, serious_list, medium_list, low_list
        """
        components_list = []
        deadly_list = []
        serious_list = []
        medium_list = []
        low_list = []

        for components, group in df.groupby('components'):
            components_list.append(components)
            severity = group["severity"]
            status_str = list(severity)  # 输出每个模块所有严重等级的数组

            # 统计各个严重等级在数组中出现的次数
            deadly = status_str.count('致命')
            serious = status_str.count('严重')
            medium = status_str.count('中')
            low = status_str.count('低')

            # 每个严重等级输出成数组
            deadly_list.append(deadly)
            serious_list.append(serious)
            medium_list.append(medium)
            low_list.append(low)

        return components_list, deadly_list, serious_list, medium_list, low_list

    def todo_bug(self, df):
        """
        遗留BUG，待办+处理中+重新打开
        :param df:
        :return: todo_bug_list
        """
        # 获得status列中值等于待办、处理中、重新打开的行
        todo_bug = df.query('status=="待办"| status=="处理中"| status=="重新打开"')
        todo_bug_list = (todo_bug.values).tolist()  # 转成列表
        return todo_bug_list
