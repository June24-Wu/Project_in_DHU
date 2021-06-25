import scrapy
import time
import json
import os


class MySpider(scrapy.Spider):
    name = "spider"

    def __init__(self):

        self.file = open('demo1_quotes.json', 'w');

        # 设置待爬取网站列表
        self.urls = []
        for i in range(1, 3):
            self.urls.append('http://quotes.toscrape.com/page/' + str(i))

        #       初始化效果 效果等同
        #         self.urls = [
        #             'http://quotes.toscrape.com/page/1/',
        #             'http://quotes.toscrape.com/page/2/',
        #         ]

        print(self.urls)

    def start_requests(self):
        # self.init_urls()
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

            # parse方法会在每个request收到response之后调用

    def parse(self, response):
        #         parse(self, response) 中的response是HtmlResponse 类型的,可以用css选择器或者xpath选择器

        # 提取名言列表
        quotes = response.css("div.quote");  # css选择器
        #         quotes = response.xpath("//div[@class='quote']");  #引号要注意

        for quote in quotes:
            # 提取每条名言中的作者名
            author = quote.css("small.author::text").extract_first();
            # 提取名言的文字内容
            text = quote.css(".text::text").extract_first();
            # 提取名言标签
            tags = quote.css(".tags .tag::text").extract();

            # 构建字典对象
            item = {"author": author, "text": text, "tags": tags};
            # 将字典转换成json字符串
            line = json.dumps(dict(item))
            # 将每个条目写入文件
            self.file.write(line + "\n")
        # 及时将内容写入文件，否则可能会出现少许延迟
        self.file.flush()
        os.fsync(self.file)
        # 输出当前解析完成的网页网址，可以当做爬取进度来看待,与程序逻辑无关
        print("over: " + response.url)

#执行爬虫任务
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.start() # 这句代码就是开始了整个爬虫过程 ，会输出一大堆信息，可以无视

#读取数据
import json
file = open('demo1_quotes.json','r',encoding='UTF-8')
# lines=json.load(file_object)
# lines
# 由于文件中有多行，直接读取会出现错误，因此一行一行读取
data = []
for line in file.readlines():
    dic = json.loads(line)
    data.append(dic)
print('json文件中有%d行数据'%len(data))
print(data)