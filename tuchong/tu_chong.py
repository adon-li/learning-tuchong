#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Liyd
# @Time : 2020/9/11 19:27
# @Email   : muziyadong@gmail.com
# @Software: PyCharm

import datetime
import hashlib
import os
import random
from tuchong.pym import create,pinying,select,insert
import time
import urllib.parse
from urllib.parse import urlencode
from urllib import request,error
import urllib
import re
import json
import socket
from prettytable import PrettyTable
# 定义图虫类
class TuChongPhoto:
    # 编辑主题表格，选择下载图片的主题
    def SearchTheme(self):
        list = []
        title = ["风光","人像","城市","旅行","纪实","街拍","人文",
                 "美女","建筑","静物","夜景","自然","少女","儿童",
                 "秋天","光影","花卉","私房","色彩","抓拍","黑白",
                 "小清新","情绪","日系","后期","写真","微距","创意",
                 "情感","复古","叶子","云","节日","胶片","猫",
                 "纪实","文化","广角","富士","时尚","宾得","艺术",
                 "北京","上海","广州","深圳","南京","成都","武汉",
                 "厦门","杭州","重庆","西藏","西安","四川","大连",
                 "新疆","长沙","苏州","日本","中国","浙江","川西",
                 "香港","云南","情侣","纽约","巴黎","伦敦","北海道"]
        # 将选项表格化
        file_names = ('代号I  ','主题I  ','代号II ','主题II ','代号III','主题III',
                      '代号IV ','主题IV ','代号V  ','主题V  ')
        table = PrettyTable(field_names=file_names)
        for i in range(len(title)):
            list.append('%d'%i)
            list.append(title[i])
        table_rows = [list[j:j+10] for j in range(0,len(list),10) ]
        for table_row in table_rows:
            table.add_row(table_row)
        table.align['代号I'] = 'c'
        print(table)
        theme_int = int(input('请输入代号:'))
        self.name = title[theme_int]
    # 定义选择主题函数
    def ChoiceTheme(self):
        # theme_int = int(input('请输入代号:'))
        self.theme_code = urllib.parse.quote(self.name)
        # 创建数据库数据表
        self.world = pinying(self.name)
        create(self.world)
        return self.theme_code
    # md5加密
    def md5(self, url):
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()
    # 获取第一层图片URL链接
    def GetUrl(self):
        self.url_lists = []
        for i in range(1,6):
            data = {'page':i,
                    'count':20,
                    'order':'weekly',
                    'before_timestamp':''}
            parse = urlencode(data)
            # 拼接URL
            self.url = 'https://tuchong.com/rest/tags/{}/posts?{}'.format(self.theme_code,parse)
            # 将URL链接md5加密
            md5_url = self.md5(self.url)
            # print(md5_url)
            result = select(self.world, md5_url)
            if len(result) != 0:
                continue
            else:
                insert(self.world, md5_url, self.url, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                # print(self.url)
                self.url_lists.append(self.url)
        # print(self.url_lists)
        return (self.url_lists)



    def RequestHeaders(self):
        self.user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) ''AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/84.0.4147.135 Safari/537.36',
                       'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
                       'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
                       'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
                       'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
                       'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
                       'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
                       'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
                       'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
                       'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
                       'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
                       'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
                       'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)']
        # print(self.header)
    def GetUrlResponse(self):
        self.images_urls = []

        for self.url_list in self.url_lists:
            try:
                self.header = {'User-Agent': random.choice(self.user_agents)}
                response = request.Request(self.url_list, headers=self.header)
                self.html1 = request.urlopen(response,timeout=5)
                self.source_code = self.html1.read().decode('utf8')
                json_data = json.loads(self.source_code)['postList']
                for datas in json_data:
                    img_url = dict(datas)['url']
                    self.images_urls.append(img_url)
                return self.images_urls
            except socket.timeout as e:
                self.html1.close()
            except error.HTTPError as e:
                continue

    def ReJpgUrl(self,source_code):
        self.jpg_urls = []
        res = re.compile('class="multi-photo-image" src="(.*?)" alt="">',re.S)
        jpg_url = res.findall(source_code)
        self.jpg_urls.append(jpg_url)
        # return self.jpg_urls
        # print(self.jpg_urls)


    def GetImagesHtml(self):
        self.photos = []
        for self.images_url in self.images_urls:
            # print(self.images_url)
            try:
                self.header = {'User-Agent': random.choice(self.user_agents)}
                # print(self.header)
                # time.sleep(random.randint(0,3))
                response = request.Request(self.images_url, headers=self.header)
                self.html2 = request.urlopen(response,timeout=5)
                source_code = self.html2.read().decode('utf8')
                # print(source_code)
                self.ReJpgUrl(source_code)
                # print(self.jpg_urls)
                self.photos.append(self.jpg_urls)
            except socket.timeout as e:
                self.html2.close()
            except error.HTTPError as e:
                continue

    def write(self):
        lists = []
        # print(self.photos)
        for i in self.photos:
            for j in i:
                for m in j:
                    lists.append(m)
        # print(len(lists))
        path = 'G:/头条百家/各类图片/{}'.format(self.name)
        if os.path.exists(path) == False:
            os.makedirs(path)
        num = 29
        for n in lists:
            urllib.request.urlretrieve(n,path + '/' + self.name + str(num) + '.jpg')
            num += 1
            print("下载完成！已下载{}张图片".format(str(num)))
if __name__ == '__main__':
    TuChongPhoto = TuChongPhoto()
    TuChongPhoto.SearchTheme()
    TuChongPhoto.ChoiceTheme()
    TuChongPhoto.GetUrl()
    TuChongPhoto.RequestHeaders()
    TuChongPhoto.GetUrlResponse()
    TuChongPhoto.GetImagesHtml()
    TuChongPhoto.write()









































