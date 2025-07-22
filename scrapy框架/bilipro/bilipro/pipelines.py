# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BiliproPipeline:
    f = None # 全局变量
    # 该函数仅会在process_item函数调用前被调用一次
    def open_spider(self,item):
        self.f = open('bili.txt','w',encoding='utf8')
        print('文件已创建!')
    # 该函数仅会在process_item函数调用完全结束后被调用一次
    def close_spider(self,item):
        self.f.close()
        print('文件已关闭!')
    # 该函数用于接收爬虫文件给其提交过来的item对象
    # 参数item即表示接收到的item对象
    # 该函数的调用次数取决于爬虫文件向其提交item对象的个数
    def process_item(self, item, spider):
        title = item['title']
        author = item['author']
        self.f.write(author+':'+title+'\n')
        print(title,'文件已写入!')
        return item
