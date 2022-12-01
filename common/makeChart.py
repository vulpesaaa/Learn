from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Tab, Page, Timeline, Line
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import datetime

"""
主要实现生成图表，一个图表一个页签
"""


class chart():

    def bugStatus_pie(self, custom_fields):
        """
        饼图-"BUG完成状态统计
        :param custom_fields:
        :return:
        """
        labels = "BUG完成状态统计"
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

        return pie

    def statusAndassignee2_bar(self, statusAndassignee2):
        """
        柱状图-处理人完成BUG统计
        :param statusAndassignee2:
        :return:
        """
        # timeline_bar = Timeline().add_schema(is_auto_play=False, pos_top='7.5%', height='2%')
        labels = "处理人完成BUG统计"
        bar = (
            Bar()
                .add_xaxis(statusAndassignee2[0])
                .add_yaxis("未解决", statusAndassignee2[1])
                .add_yaxis("已解决", statusAndassignee2[2])
                .set_global_opts(title_opts=opts.TitleOpts("{}".format(labels)),
                                 xaxis_opts=opts.AxisOpts(name_rotate=30, axislabel_opts={"rotate": 30})))

        return bar

    def components_bar(self, components):
        """
        柱状图-各模块BUG统计
        :param components:
        :return:
        """
        labels = "各模块BUG统计"
        bar = (
            Bar()
                .add_xaxis(list(components.keys()))
                .add_yaxis("", list(components.values()))
                .set_global_opts(title_opts=opts.TitleOpts("{}".format(labels)),
                                 xaxis_opts=opts.AxisOpts(name_rotate=30, axislabel_opts={"rotate": 30})))
        return bar

    def componentsAndseverity2_bar(self, componentsAndseverity2):
        """
        柱状图-各模块BUG严重等级统计
        :param componentsAndseverity2:
        :return:
        """

        labels = "各模块BUG严重等级统计"
        bar = (
            Bar()
                .add_xaxis(componentsAndseverity2[0])
                .add_yaxis("致命", componentsAndseverity2[1])
                .add_yaxis("严重", componentsAndseverity2[2])
                .add_yaxis("中", componentsAndseverity2[3])
                .add_yaxis("低", componentsAndseverity2[4])
                .set_global_opts(title_opts=opts.TitleOpts("{}".format(labels)),
                                 xaxis_opts=opts.AxisOpts(name_rotate=30, axislabel_opts={"rotate": 30})))
        return bar

    def bug_list(self, todo_bug_list):
        """
        表单-BUG遗留清单
        :param todo_bug_list:
        :return:
        """
        bugtable = (
            Table()

                .add(["jira号", '概要', '优先级', '严重程度', '经办人', '状态', '模块'], todo_bug_list)
                .set_global_opts(title_opts=ComponentTitleOpts(title="Bug遗留清单"))
        )
        return bugtable

    def tab(self, bugStatus_pie, statusAndassignee2_bar, components_bar, componentsAndseverity2_bar, bugtable):
        """
        一个Tab下添加多个图表，并生成html文件
        :param bugStatus_pie:
        :param statusAndassignee2_bar:
        :param components_bar:
        :param componentsAndseverity2_bar:
        :param bugtable:
        :return:
        """
        report_name = '测试报告'
        tab = Tab()
        tab.add(bugStatus_pie, "BUG完成状态统计")
        tab.add(statusAndassignee2_bar, "处理人完成BUG统计")
        tab.add(components_bar, "各模块BUG统计")
        tab.add(componentsAndseverity2_bar, "各模块BUG严重等级统计")
        tab.add(bugtable, "BUG遗留清单")

        time = datetime.datetime.now().strftime('%Y-%m-%d')

        return tab.render('./report/' + str(report_name) + time + ".html")
