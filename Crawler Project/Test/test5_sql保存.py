#!/usr/bin/python3
import pymysql
database = '上海市中小学生入学情况'   # 数据库名称
    db = pymysql.connect(host="localhost", user="root", password='Wwj0233tt.', charset='utf8', db= database) # 创建数据库

cursor = db.cursor()    # 创建游标

table = '上海大学'
# 创建数据表
sql = """CREATE TABLE %s ( 序号 varchar(20), 报名号 varchar(20), 姓名 varchar(20) )""" % table
cursor.execute(sql)
insert = """Insert into %s (序号,报名号,姓名) VALUES (18 , 17 , 16 ) % (table)"""
        cursor.execute(insert)
db.close()
print('成功建表')
