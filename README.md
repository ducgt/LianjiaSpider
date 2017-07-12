# 概要 #
此爬虫主要基于Scrapy + MySQL爬取链家网中，北京地区的租房信息。
Python版本为Python3.6

# 使用说明 #
首先运行database.py文件来交互式创建数据表
```
python database.py
```

之后在src文件夹根目录下运行
```
scrapy crawl LianjiaSpider
```
等待爬虫爬取之后，在数据库中查看如图
![](/screenshots/mysql.png)
