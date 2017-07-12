# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class LianjiaspiderPipeline(object):
    def open_spider(self, spider):
        self.con = MySQLdb.connect('localhost', 'root', '密码', '数据库名字')
        self.cursor = self.con.cursor()

    def process_item(self, item, spider):
        insert_sql = "INSERT INTO lianjia(TITLE, LOCATION, ZONE, METERS, DIRECTION, MONEY) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(item['title'], item['location'], item['zone'], item['meters'], item['direction'], item['money'])
        self.cursor.execute(insert_sql) # 执行sql语句
        self.con.commit() # 提交到数据库，insert和updata语句必须执行这句
        return item

    def spider_close(self, spider):
        self.con.close()
