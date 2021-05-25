# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def get_html(url):     # 获取网页
    headers = {"User-Agent": UserAgent(verify_ssl=False).random}
    response = requests.get(url, headers=headers)     # 用UserAgent的方法来访问网页


    # ----------------------------------------1、解决中文乱码问题-----------------------------------
    if response.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(response.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = response.apparent_encoding
    else:
        encoding = response.encoding
    response = response.content.decode(encoding, 'ignore').encode('utf-8', 'ignore')
    # -------------------------------------------------------------------------------------------
    return response


def html_parser(response):
    soup = BeautifulSoup(response, 'html.parser')
    print(soup)
    return soup


url = input('请输入要检查的网址')
html_parser(get_html(url))


# ---------------------------------检查字符代码---------------------------------------------
# cop = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9]")   # 解决字符问题，保留英文和中文
# chinese = re.compile(r'[^\u4e00-\u9fa5]') # 仅保留中文字符