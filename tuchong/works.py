#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Liyd
# @Time : 2020/9/15 16:55
# @Email   : muziyadong@gmail.com
# @Software: PyCharm
import datetime

import pandas as pd

excelFile = r'G:\故障工单-20200929.xls'
df = pd.DataFrame(pd.read_excel(excelFile))
column = list(df)
print(column)
print(column[-5])

data1 = df[['工单编号','工单状态','故障来源','故障等级','{}'.format(column[-5])]]
# print(data1)
zong_data2 = data1[(data1['工单状态'] != '已作废' )& (data1['{}'.format(column[-5])] != '是')]
print("新建立故障工单{}张".format(len(zong_data2)))
gaojing_data =  zong_data2[zong_data2["故障来源"] == '告警监控']
print("其中包括告警监控{}张".format(len(gaojing_data)))
xunjian_data = len(zong_data2) - len(gaojing_data)
if xunjian_data  != 0:
    print("其中包括巡检问题{}张".format(xunjian_data))
else:
    print("无巡检问题")
#
excelFile2 = r'G:\投诉工单-20200929.xls'
df2 = pd.read_excel(excelFile2)
data3 = df2[['工单号','是否测试工单','工单状态','工单类型']]
zong_data3 = data3[data3['是否测试工单'] != '是']
print("共新建客户服务工单{}张".format(len(zong_data3)))
fuwu_data = zong_data3[zong_data3['工单类型'] == '服务请求']
print('客户服务请求{}张'.format(len(fuwu_data)))
zixun_data = zong_data3[zong_data3['工单类型'] == '使用咨询']
print('客户咨询请求{}张'.format(len(zixun_data)))
print('客户投诉{}张'.format(len(zong_data3) - len(fuwu_data) - len(zixun_data)))


# excelFile2 = r'G:\移动云工程变更信息登记表.xlsx'
# df3 = pd.read_excel(excelFile2,sheet_name = '2020年9月工程作业')
# data = df3[(df3['计划开始时间']<='2020-09-09 09:00:00') & (df3['计划开始时间']>='2020-09-08 09:00:00')]
# data4 = data[['变更工单号','变更标题','客户业务影响范围','计划开始时间','计划结束时间','作业结果']]
# for i in data4['客户业务影响范围']:
#     # print(len(i))
#     if len(i) > 50:
#         print(i)
# today = datetime.date.today()
# yesterday = datetime.date.today() - datetime.timedelta(days=1)
# print(today.strftime('%Y-%m-%d 09:00:00'))
# print(yesterday.strftime('%Y-%m-%d 09:00:00'))