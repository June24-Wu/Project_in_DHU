# coding=utf-8
# 得到指定一个URL网页内容
import urllib.request
import urllib.error

def askURL(url):
    head = {  # 模拟浏览器头部信息，豆瓣服务器发送消息
        # 服务代理，告诉豆瓣服务器，我们是什么类型的机器，本质是我们可以接受什么文件内容
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    data = bytes(urllib.parse.urlencode({'name': 'eric'}), encoding='utf-8')
    request = urllib.request.Request(url, headers=head, data=data, method="POST")  # 发送请求
    try:
        response = urllib.request.urlopen(request)    # 取得响应
        html = response.read().decode('utf-8')   # 获取网页内容
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html




askURL("https://www.douban.com")
# try:
#     res = urllib.request.urlopen(request)
#     html = res.read().decode("utf-8")
#     print(html)
