# 1.1--------------------find_all()
# 字符串过滤，会查找与字符串完全匹配的内容
# t_list = bs.find_all('a')


# 1.2---正则表达式 ,搜索符合正则表达式规则的标签，含有‘a’的标签都会被返回 ，匹配的是某一个标签及其所有的内容
# t_list=bs.find_all(re.compile('a'))



# 1.3*了解----根据函数的方法来搜索
# def name_is_exists(tag):
#     return  tag.has_attr('name')
# t_list = bs.find_all(name_is_exists())   # 搜索所有含有name标签的函数


# --------------------------------------------------------------------------------

# 2.kwargs函数
# t_list = bs.find_all(id = 'head')  #find_all 可以给一个参数


# ---------------------------------------------------------------------------------

# 3.text 参数
# t_list = bs.find_all(text = 'hao123')    # 结果  hao123
# 也可以用 text = [ …………]用列表的形式


# ---------------------------------------------------------------------------------

# 4.limit 参数
# t_list = bs.find_all('a',limit = 3 )    # 直接获取前三个



# ---------------------------------------------------------------------------------
# 5.css选择器
# print(bs.select('title'))    # 通过标签来查找
# 返回一个列表
# print(bs.select('.mnav'))    # 用类名（class）来进行查找
# print(bs.select('#u1'))    # 用id来进行查找
# print(bs.select('a[class= "bri"]'))    # 查找a标签中，class = bri的
# print(bs.select('head > title '))    # 查找head里面的title ， 通过子标签来查找


