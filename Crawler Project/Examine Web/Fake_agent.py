# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import chardet

def get_html(url):     # 获取网页
    headers = {"User-Agent": UserAgent(verify_ssl=False).random}
    response = requests.get(url, headers=headers)     # 用UserAgent的方法来访问网页


    # 1、解决中文乱码问题
    if response.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(response.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = response.apparent_encoding
    else:
        encoding = response.encoding
    response = response.content.decode(encoding, 'ignore').encode('utf-8', 'ignore')

    # 2、用chardet函数来解决中文乱码问题（不优）
    # response = response.content   # 提取相应文本
    # cod = chardet.detect(response)
    # coding = cod['encoding']
    # response = response.decode(coding,'ignore')     # 用chardet函数来解码decoding

    return response


def html_parser(response):
    soup = BeautifulSoup(response, 'html.parser')
    print(soup)
    return soup


html_parser(get_html(input('请输入网址：')))


# ------------------------------------------------------------------------------------
#   去除字符串中其他符号
# cop = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9]")
# string = cop.sub("", line)
# -------------------------------------------------------------------------------------