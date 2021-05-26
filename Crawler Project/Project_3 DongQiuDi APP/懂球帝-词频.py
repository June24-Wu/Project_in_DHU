#import nltk
import jieba
import requests
import re
import datetime
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
from fake_useragent import UserAgent  
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from PIL import Image

def all_page(url):
    base_url = url
    urllist = []
    for page in range(3, 7):
        allurl = base_url + str(page)
        urllist.append(allurl)
    return urllist
"""
wwj 看这里！！！UserAgent！！
这个函数需要传个参（url地址）;
主函数main()在最下面
"""
def get_html(url):
	headers = {"User-Agent": UserAgent(verify_ssl = False).random}
	response = requests.get(url, headers = headers).text
	return response

def html_parser(response):
	soup = BeautifulSoup(response, 'html.parser')
	s = soup.find_all('dd')
	return s 

def write_web(content , filename):
	with open(filename , 'a+', encoding='utf-8') as f:
		for c in content:
			c1 = str(c)
			c1 = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\。\@\#\\\&\*\%]", "",c1)
			f.write(c1) 

def jieba_text(filename1, filename2):
	txt = open(filename1,'rb').read()  
	words  = jieba.lcut(txt)  
	counts = {}
	exclueds = {'球队','我们','他们','可是','想要','可是','：','--','！','？'}
	for word in words: 
		counts[word] = counts.get(word, 0) + 1   
		if word in exclueds:
				del(counts[word])

	items_new = []			
	items = list(counts.items())  
	items.sort(key=lambda x:x[1], reverse=True)
	for i in items:
		if not len(i[0]) == 1 :
			items_new.append(i)

	with open(filename2,'a') as f:   
		for i in range(10):  
			word, count = items_new[i]
			f.write("{0:<10}{1:>5}".format(word, count))

	new_list = []
	for i in items_new:
		new_list.append(i[0])
	word_str=' '.join(new_list)

	return word_str,items_new


def create_word_cloud(word_str , news_kind ):
	now = datetime.datetime.now().strftime("%Y-%m-%d %H")
	cloud_mask = np.array(Image.open("C:\\Users\\HP\\Desktop\\大作业懂球帝\\补充材料\\love1.png"))#词云的背景图
	wc = WordCloud(
		background_color = "white",
		mask = cloud_mask,          #背景图cloud_mask
		max_words=125,
		font_path ='C:\\Users\\HP\\Desktop\\大作业懂球帝\\补充材料\\simsun.ttf' ,
		height=4000,
		width=40000,
		max_font_size=1000,
		random_state=100,)
	fbword = wc.generate(word_str)  

	plt.imshow(fbword)
	plt.axis("off")
	#plt.show()
	plt.savefig('C:\\Users\\HP\\Desktop\\大作业懂球帝\\词云图\\%s%s返图.jpg' % (news_kind, now))
	#wc.to_file('%s%s返图.jpg' % (news_kind, now))

def transfer_to_csv(rows, news_kind):
	now = datetime.datetime.now().strftime("%Y-%m-%d %H")
	fields =['词语','频数']
	filename = '%s词频统计%s.csv' % (news_kind, now)
	with open(filename , 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(fields)
		csvwriter.writerows(rows)

"""直方图"""
def draw_bar(rows , news_kind):
	x = []
	y = []
	plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
	#plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
	for row in rows[0:10]:
		x.append(row[0])
		y.append(row[1])
	plt.plot(x, y, color = 'r')
	plt.bar(x,y, alpha = .5, color = 'g')
	plt.xlabel('单词')
	plt.ylabel('出现次数')
	plt.title('单词直方图')
	now = datetime.datetime.now().strftime("%Y-%m-%d %H")
	plt.savefig('C:\\Users\\HP\\Desktop\\大作业懂球帝\\柱状图\\%s柱状图%s.jpg' %(news_kind, now))

def main():
	now = datetime.datetime.now().strftime("%Y-%m-%d %H")
	news_kind = ['英超','意甲' ,'西甲' ,'德甲']
	url = "https://www.dongqiudi.com/newsList/"
	i = 0
	for url in all_page(url):
		html = get_html(url)
		content = html_parser(html)
		write_web(content , '懂球帝新闻页面%s%s.txt' % (news_kind[i],now))
		rows =(jieba_text('懂球帝新闻页面%s%s.txt' % (news_kind[i],now) ,'懂球帝分析结果%s%s.txt' % (news_kind[i],now)))[1]
		draw_bar(rows, news_kind[i])
		a = (jieba_text('懂球帝新闻页面%s%s.txt' % (news_kind[i],now) ,'懂球帝分析结果%s%s.txt' % (news_kind[i],now)))[0]
		create_word_cloud(a, news_kind[i])
		plt.clf()
		transfer_to_csv(rows, news_kind[i])
		i += 1


if __name__ == '__main__':
	flag = 0
	now = datetime.datetime.now()
	sched_timer = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)\
				+ datetime.timedelta(seconds = 5)

	while (True):
		now = datetime.datetime.now()
		if sched_timer < now < sched_timer + datetime.timedelta(seconds = 1):
			time.sleep(1)
			main()
			flag = 1	
		else:
			if flag == 1:
				sched_timer = sched_timer + datetime.timedelta(minutes = 10)
				flag = 0


"""
	url = "https://www.dongqiudi.com/newsList/"
	for url in all_page(url):
		html = get_html(url)
		content = html_parser(html)
		write_web(content , '懂球帝新闻页面.txt')
		print("=======================================================================")
	create_word_cloud(jieba_text('懂球帝新闻页面.txt','懂球帝分析结果.txt'))
	print("结束")



	url = "https://www.dongqiudi.com/newsList/"
	for url in all_page(url):
		html = get_html(url)
		content = html_parser(html)
		write_web(content , '懂球帝新闻页面.txt')
		print("=======================================================================")
	create_word_cloud(jieba_text('懂球帝新闻页面.txt','懂球帝分析结果.txt'))
	print("结束")

	url = 'https://dongqiudi.com/news'              
	#url ='https://www.whoscored.com/Editorial'
	html = get_html(url)
	content = html_parser(html)
	write_web(content , '懂球帝新闻页面.txt')
	jieba_text('懂球帝新闻页面.txt','懂球帝分析结果.txt')
	"""