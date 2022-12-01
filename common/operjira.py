from jira import JIRA
# -*- coding=utf-8 -*-
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Pie, Tab, Page, Timeline
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts


# 登录jira并返回一个jira的实例
def login_jira(self, server, username, password):
    jira = JIRA(server=server, basic_auth=(username, password))
    return jira


# 根据jql查询jira的信息
def search_issues(self, jira, jql, max_results, fields):
    try:
        issues = jira.search_issues(jql, fields=fields, maxResults=max_results)
        return issues
    except Exception as e:
        print(e)


# 对jira返回对象解析并整理成字典
def analytical(jira_result,custom_field):
    summarys = {}
    components = {}
    custom_fields = {}
    reason_bugs = {}
    for x in jira_result:
        a = str(x.fields.summary)  # 概要
        if not x.fields.components:
            b = 'None'
        else:
            b = str(x.fields.components[0])  # 模块 返回的是一个jira的components对象  需要转成str
        # 参数待改
        c = str(x.fields.custom_field)  # 归因分析
        d = str(x.key)  # jira号
        e = str(x.fields.labels[0])
        summarys.setdefault(d, a)  # {jira号:概要}
        components.setdefault(b, 0)  # {模块：出现次数}
        if b in components.keys():
            components[b] = components[b] + 1
        custom_fields.setdefault(c, 0)  # {归因分析：出现次数}
        if c in custom_fields.keys():
            custom_fields[c] = custom_fields[c] + 1
        reason_bugs.setdefault((d + a), c)  # {jira号 jira概要：jira归因分析}
        labels = e

        # 注： labels
    return (summarys, components, custom_fields, reason_bugs, labels)


def make(jira_finail_result):
    timeline_bar = Timeline().add_schema(is_auto_play=True, pos_top='7.5%', height='2%')
    timeline_pie = Timeline().add_schema(is_auto_play=True, pos_top='7.5%', height='2%')

    line_name = []
    line_data = []
    for jira_result in jira_finail_result:
        summarys = jira_result[0]
        components = jira_result[1]
        custom_fields = jira_result[2]
        reason_bugs = jira_result[3]
        labels = jira_result[4]
        x = Faker.choose()

        bar = (
            Bar()
                .add_xaxis(list(components.keys()))
                .add_yaxis("", list(components.values()))
                # .reversal_axis() #横向展示
                .set_global_opts(title_opts=opts.TitleOpts("{}".format(labels)),
                                 xaxis_opts=opts.AxisOpts(name_rotate=30, axislabel_opts={"rotate": 30})))
        timeline_bar.add(bar, '')
        # 柱状图

        pie = (
            Pie()
                .add("2", [list(z) for z in zip(list(custom_fields.keys()), list(custom_fields.values()))],
                     radius=["40%", "70%"],
                     label_opts=opts.LabelOpts(
                         position="outside",
                         formatter="{b}:{c}\n{per|{d}%}",
                         background_color="#eee",
                         border_color="#aaa",
                         border_width=1,
                         border_radius=2,
                         rich={
                             "a": {"color": "#989", "lineHeight": '44%', "align": "center"},
                             "abg": {
                                 "backgroundColor": "#e3e3e3",
                                 "width": "30%",
                                 "align": "right",
                                 "height": 21,
                                 "borderRadius": [0, 0, 0, 0],
                             },
                             "hr": {
                                 "borderColor": "#aaa",
                                 "width": "71%",
                                 "borderWidth": 12,
                                 "height": 12,
                             },
                             "b": {"fontSize": 15, "lineHeight": 10},
                             "per": {
                                 "color": "#eee",
                                 "backgroundColor": "#324456",
                                 "padding": [0.5, 0.5],
                                 "borderRadius": 1,
                             },
                         },
                     ),
                     )
                # .set_global_opts(title_opts=opts.TitleOpts(title="标题")) #小标题
                .set_global_opts(legend_opts=opts.LegendOpts(pos_left='83%'),
                                 title_opts=opts.TitleOpts(title="{}".format(labels)),
                                 tooltip_opts=opts.TooltipOpts(is_show=False, ))
        )
        timeline_pie.add(pie, "")
        # 饼图

        line_name.append(labels)
        line_data.append(len(summarys))

        analysetable = (
            Table()
                .add(["事件", '详情'],
                     [
                         ['需求情况', '填写实际的迭代的需求情况'],
                         ['bug情况', '填写实际的迭代的bug情况'],
                         ['总结', '对本次发布进行总结']
                     ]
                     )
                .set_global_opts(title_opts=ComponentTitleOpts(title="迭代总结"))
        )
        # 表格

        bug_list = []
        for one in reason_bugs:
            bug_list.append([reason_bugs[one], one])
        bugtable = (
            Table()
                # .add(["bug原因", 'jira号 概要'], [[1, 'sha'], [1, 2]])   # demo样例
                .add(["bug原因", 'jira号 概要'], bug_list)
                .set_global_opts(title_opts=ComponentTitleOpts(title="Bug归因列表"))
        )
    # bug列表清单

    line = (
        Line()
            .add_xaxis(line_name, )
            .add_yaxis("迭代测试bug数", line_data, is_smooth=True)
            .set_series_opts(textstyle_opts=opts.TextStyleOpts(font_size=50))
            .set_global_opts(title_opts=opts.TitleOpts(title="迭代测试bug数"),
                             xaxis_opts=opts.AxisOpts(name_gap=500, name_rotate=30, axislabel_opts={"rotate": 30},
                                                      )
                             )
    )
    # 折线图
    report_name = '测试报告'

    tab = (
        Tab()
            .add(analysetable, '迭代总结')
            .add(timeline_bar, '迭代bug功能模块统计')
            .add(timeline_pie, '迭代bug归因分析')
            .add(line, '迭代测试bug数')
            .add(bugtable, 'bug列表')
    )
    # 标签页
    tab.render('''../reports/''' + str(report_name) + ".html")
# 以标签页为格式生成图表