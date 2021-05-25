from bs4 import BeautifulSoup # 网页解析，获取数据
import re # 正则表达式，进行文字匹配
import urllib.request, urllib.error # 制定URL,获取网页数据
import xlwt # 进行excel操作

head = {  # 模拟浏览器头部信息，豆瓣服务器发送消息
    # 服务代理，告诉豆瓣服务器，我们是什么类型的机器，本质是我们可以接受什么文件内容
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Accept': 'text / html, application / xhtml + xml, application / xml;0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN, zh;q = 0.9',
    'Cookie': 'dqduid=rB8CbV9lQt8ahRfiBY0eAg==; __51cke__=; sajssdk_2015_cross_new_user=1; Hm_lvt_ac3d87d81953324fa2119a12756e54bc=1600471840,1600471845,1600471858,1600472315; __tins__17453986=%7B%22sid%22%3A%201600474056412%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201600475856412%7D; __51laig__=21; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22174a38d3b737fb-06655543b48de-f313f6d-2073600-174a38d3b74320%22%2C%22%24device_id%22%3A%22174a38d3b737fb-06655543b48de-f313f6d-2073600-174a38d3b74320%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; Hm_lpvt_ac3d87d81953324fa2119a12756e54bc=1600474057',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document' ,
    'Sec-Fetch-Mode': 'navigate' ,
    'Sec-Fetch-Site': 'same-origin',
    'Host': 'm.dongqiudi.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Sec-Fetch-User': '?1'

}
data = bytes(urllib.parse.urlencode({'name': 'eric'}), encoding='utf-8')
url = input('请输入要检查的网址')
request = urllib.request.Request(url, headers=head, data=data, method="POST")  # 发送请求
try:
    response = urllib.request.urlopen(request)  # 取得响应
    html = response.read().decode('utf-8')  # 获取网页内容
except urllib.error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
print(html)
print('爬取成功')