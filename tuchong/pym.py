#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Liyd
# @Time : 2020/10/11 19:56
# @Email   : muziyadong@gmail.com
# @Software: PyCharm
import datetime

import pymysql
from pypinyin import lazy_pinyin,  Style
conn = pymysql.connect('localhost',user='root',passwd='root')
cursor = conn.cursor()
def close():
    cursor.close()
def create(tableName):
    cursor.execute('use tuchong;')
    cursor.execute('create table if not exists %s (id int not null auto_increment primary key,'
                   'md5 varchar(200) not null,'
                   'url varchar(500) not null,'
                   'updatetime datetime not null);'% tableName)
def insert(table,md5,url,time):
    cursor.execute('use tuchong;')
    cursor.execute('insert into %s(md5,url,updatetime) values("%s","%s","%s");'% (table,md5,url,time))
    cursor.connection.commit()
def select(table,md5):
    cursor.execute('use tuchong;')
    cursor.execute('select 1 from %s where md5 = "%s" limit 1;'% (table,md5))
    data = cursor.fetchall()
    return data
def pinying(world):
    s = str(world).replace(" ", "")
    style = Style.NORMAL
    w = lazy_pinyin(s, style=style)
    t = ''.join(w)
    return t

# if __name__ == '__main__':
#     dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     # print(dt)
#     url = "https://tuchong.com/rest/tags/%E9%9D%92%E5%B2%9B/posts?page=1&count=20&order=weekly&before_times"
#     # insert('qingdao','631a8b4e2fd84765f883791d46a9110',url,dt)
#     a = select('qingdao','631a8b4e2fd84765f883791d46a9110')
#     print(len(a))