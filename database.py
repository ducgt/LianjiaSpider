# -*- coding=utf-8 -*-
import MySQLdb
account = input('请输入MySQL用户名\n >')
password = input('请输入MySQL密码\n >')
table = input('请输入数据库名称\n >')
# 连接数据库
db = MySQLdb.connect('localhost',account, str(password), table)
# 获取游标
cursor = db.cursor()
sql = """CREATE TABLE lianjia(
    TITLE VARCHAR(30),
    LOCATION VARCHAR(100),
    ZONE VARCHAR(10),
    METERS VARCHAR(10),
    DIRECTION VARCHAR(10),
    MONEY VARCHAR(10)
)
"""
# 执行sql语句
cursor.execute(sql)
# 关闭数据库
db.close()
