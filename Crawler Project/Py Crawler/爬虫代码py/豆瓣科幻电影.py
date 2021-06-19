#coding:utf-8
import requests
import re,json
from  time import sleep
from lxml import etree
import pandas as pd
import numpy as np
from fake_useragent import UserAgent
import csv74
# import redis
from pandas import DataFrame

#定义要爬取的内容，字典格式
def init_movie_list():
    dic_move_list = {
        '电影标识': '', '电影名': '', '链接': '', '类型': '', '国家': '', '上映日期': '', '年':'',
        '月': '', '日': '', '片长': '', '评分': '', '总评分人数': '', '短评数': '', '长评数': '',
#         '电影简介': '',
    }
    return dic_move_list


def get_list(sum):
    #     url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort=time&page_limit=20&page_start={0}'.format(sum,)
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort=time&page_limit=20&page_start=' + 'sum'
    #     headers={'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive', 'Cookie': 'll="108296"; bid=BbME6r_nuro; __yadk_uid=jdHi3QlBPfjdvh5YlbVdCR40Ypf2vvlA; _vwo_uuid_v2=D6726514AB365C52EFCDE704CAC845697|74724018438da00ae712a95e94cb5fc7; __utmc=30149280; __utmc=223695111; __utmz=30149280.1555418104.5.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/connect/qrconnect; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18929; __utma=30149280.1273655765.1554811453.1555519339.1556175978.7; __utmb=30149280.1.10.1556175978; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1556175980%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.385128923.1554811453.1555519339.1556175980.7; __utmb=223695111.0.10.1556175980; __utmz=223695111.1556175980.7.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; dbcl2="189292246:a+SESTm2EuM"; ck=8mfX; _pk_id.100001.4cf6=c11972beecd6d174.1554811458.7.1556177322.1555519340.', 'Host': 'movie.douban.com', 'Referer': 'https://movie.douban.com/explore', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36', 'X-Requested-With': 'XMLHttpRequest'}

    headers = {"User-Agent": UserAgent(verify_ssl=False).random}
    page = requests.get(url, headers=headers).text
    sleep(3)
    # print(url)
    # print(page)
    page = json.loads(page)['subjects']
    # print(page)
    for i in page:
        dic1 = init_movie_list()
        dic1['链接'] = i['url']
        dic1['电影标识'] = i['id']
        dic1['评分'] = i['rate']
        dic1['电影名'] = i['title']
        get_detail(dic1)
        # break


def get_detail(dic1):
    print('抓取电影信息')
    #     headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': 'll="108296"; bid=BbME6r_nuro; __yadk_uid=jdHi3QlBPfjdvh5YlbVdCR40Ypf2vvlA; _vwo_uuid_v2=D6726514AB365C52EFCDE704CAC845697|74724018438da00ae712a95e94cb5fc7; __utmc=30149280; __utmc=223695111; __utmz=30149280.1555418104.5.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/connect/qrconnect; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18929; __utma=30149280.1273655765.1554811453.1555519339.1556175978.7; __utmb=30149280.1.10.1556175978; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1556175980%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.385128923.1554811453.1555519339.1556175980.7; __utmb=223695111.0.10.1556175980; __utmz=223695111.1556175980.7.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; dbcl2="189292246:a+SESTm2EuM"; ck=8mfX; _pk_id.100001.4cf6=c11972beecd6d174.1554811458.7.1556177658.1555519340.', 'Host': 'movie.douban.com', 'Referer': 'https://movie.douban.com/explore', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    headers = {"User-Agent": UserAgent(verify_ssl=False).random}
    page = requests.get(url=dic1['链接'], headers=headers).text
    page2 = page
    # sleep(3)
    html = etree.HTML(page)

    # 片长的提取
    content = html.xpath('//*[@id="info"]/span[@property="v:runtime"]/@content')
    if content:
        dic1['片长'] = content[0]

    # 总评分人数的提取
    content = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')
    if content:
        dic1['总评分人数'] = content[0]

    # 电影类型的提取和转换
    list1 = re.findall('<span class="pl">类型:</span>(.*?)<br/>', page)
    #     print(list1)
    if list1:
        list2 = re.findall('<span property="v:genre">(.*?)</span>', list1[0])
        # print(list2)
        if list2:
            if len(list2) == 1:
                #                 print("其它")
                dic1['类型'] = '其它'
            else:
                for i in range(len(list2)):
                    if list2[i] != '科幻':
                        #                         print(list2[i])
                        dic1['类型'] = list2[i]
                        break

    # 制片国家的提取和转换
    content = re.findall("制片国家/地区:</span> (.*?)<br/>", page)
    if content:
        di_qu = content[0]
        c = di_qu.split('/')
        if c:
            dic1['国家'] = c[0]
    #         print(c[0])

    page = page.replace('\\/', '/')
    page = page.replace('\n', '').replace('\t', '').replace('\r\n', '').replace(' ', '')
    page2 = page2.replace('\n', '').replace('\t', '').replace('\r\n', '')

    # 上映日期及年月日的提取和转换
    cate_list = re.findall('<spanclass="pl">上映日期:</span>(.*?)<br/>', page)
    if cate_list:
        c = re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}', cate_list[0])
        if c:
            dic1['上映日期'] = c[0]

            year = re.findall('[0-9]{4}', c[0])
            if year:
                dic1['年'] = year[0]
            month = re.findall('-([0-9]{2})-', c[0])
            if month:
                dic1['月'] = month[0]
            day = re.findall('-[0-9]{2}-([0-9]{2})', c[0])
            if day:
                dic1['日'] = day[0]

    # 短评数和长评数的提取和转换
    c = re.findall('comments\?status=P">全部([0-9]*?)条</a>', page)
    if c:
        dic1['短评数'] = c[0]
    c = re.findall('<ahref="reviews">全部([0-9]*?)条</a>', page)
    if c:
        dic1['长评数'] = c[0]

    print(dic1)

    # 向csv里存储数据
    writer.writerow([dic1['电影标识'], dic1['电影名'], dic1['链接'], dic1['类型'], dic1['国家'],
                     dic1['上映日期'], dic1['年'], dic1['月'], dic1['日'], dic1['片长'],
                     dic1['评分'], dic1['总评分人数'],
                     dic1['短评数'], dic1['长评数']])

#创建一个包含列名的csv文件，用来存储爬下来的数据
# rd_cli = redis.Redis(db=6,encoding='utf-8')
name = '豆瓣电影.csv'
csvfile = open(name,"w",newline="",encoding="utf-8-sig")
writer = csv.writer(csvfile)
#写入一行标题
writer.writerow(["电影标识" ,"电影名" ,"链接" ,"类型" ,"国家" ,"上映日期" ,"年", "月" ,"日" , "片长" ,"评分" , "总评分人数","短评数", "长评数"])

# 爬虫主程序
# 翻页，每页20个电影
for i in range(10):  # 先爬取10页做演示
    print(i)
    num = i * 20
    print(num)
    get_list(num)

# get_list(60)
print("爬取完毕")

# 关闭文件
csvfile.close()

#读取刚才爬取的数据
data = pd.read_csv('豆瓣电影.csv')
# data = pd.read_excel('豆瓣电影.xls')
print('共爬取数据 %s 行（科幻电影个数）' %len(data))

# 查看每列数据的数据类型
print(data.dtypes)
#print(data)