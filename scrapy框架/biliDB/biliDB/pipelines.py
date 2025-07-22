# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BilidbPipeline:
    f = None  # 全局变量

    # 该函数仅会在process_item函数调用前被调用一次
    def open_spider(self, item):
        self.f = open('bili.txt', 'w', encoding='utf8')
        print('文件已创建!')

    # 该函数仅会在process_item函数调用完全结束后被调用一次
    def close_spider(self, item):
        self.f.close()
        print('文件已关闭!')

    # 该函数用于接收爬虫文件给其提交过来的item对象
    # 参数item即表示接收到的item对象
    # 该函数的调用次数取决于爬虫文件向其提交item对象的个数
    def process_item(self, item, spider):
        title = item['title']
        author = item['author']
        self.f.write(author + ':' + title + '\n')
        print(title, '文件已写入!')
        return item  # 可以将item传递给下一个优先级高的管道


# 将数据存储到mysql数据库
import pymysql  # py链接mysql


class MysqlPipelines:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        db='spider'  # mysql指定的数据仓库
    )
    cursor = conn.cursor()  # 用于执行sql语句的游标对象

    def process_item(self, item, spider):
        title = item['title']
        author = item['author']
        # 将两个字段存储到mysql的库表中
        sql = 'insert into bili values ("%s","%s")' % (title, author)
        self.cursor.execute(sql)  # 使用游标对象执行sql语句
        # 提交事务
        self.conn.commit()
        print('mysql里一条数据插入成功!')
        return item

    def close_spider(self, item):
        self.cursor.close()
        self.conn.close()


# 将数据存储到redis数据库
from redis import Redis

class RedisPipelines:
    # 这里item是字典对象，redis不能接受所以要现将其转为json格式
    conn = Redis(host='127.0.0.1',port=6379)
    def process_item(self, item, spider):
        # 将item字典存于redis中
        item_json = json.dumps(dict(item),ensure_ascii=False)
        # print(item_json)
        self.conn.lpush('bili',item_json)# 新建列表名称与要存储的数据
        print('redis里一条数据插入成功!')
        return item

    # data = conn.lrange('bili', 0, -1)
    # for item in data:
    #     print('测试redis返回获取数据:',json.loads(item))
    #     break

