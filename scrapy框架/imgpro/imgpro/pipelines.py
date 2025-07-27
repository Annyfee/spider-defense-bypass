# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


from scrapy.pipelines.images import ImagesPipeline # ImagesPipeline:用于处理图片文件的内置管道

# 重新构建固定三函数(scrapy已封装好)用于图片批量下载与保存
class ImgproPipeline(ImagesPipeline):
    # 负责对图片进行请求发送并获取图片二进制数据
    # 可以通过item参数接收爬虫文件提交过来的item对象
    def get_media_requests(self,item,info):
        title = item['title']
        img_src = item['img_src']

        # 对图片地址进行请求发送(手动发请求)
        # meta参数：实现请求传参，将meta所构建的字典传递给file_path
        yield scrapy.Request(img_src,meta={'title':title})

    # 负责指定保存图片时图片的名字
    def file_path(self, request, response=None, info=None, *, item=None):
        # 获取图片名字 -- 让get_media_requests函数将图片名发到file_path函数
        title = request.meta['title']+'.jpg'
        print(title,'图片保存成功!')
        return title

    # 用来将item对象传递给下一个管道
    def item_completed(self, results, item, info):
        return item