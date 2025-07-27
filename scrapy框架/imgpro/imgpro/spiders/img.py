import scrapy
from imgpro.items import ImgproItem

class ImgSpider(scrapy.Spider):
    name = "img"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://image.so.com/zjl?sn=0&ch=wallpaper"]

    def parse(self, response):
        # 获取图片地址并将其封装到item对象，再将该对象提交给pipelines管道
        res = response.json()['list']
        for i,x in enumerate(res,start=1):
            title = x['title']
            img_src = x['qhimg_url']
            item = ImgproItem()
            item['title'] = title
            item['img_src'] = img_src
            yield item
            # 通过图片链接，scrapy再由异步爬取存储二进制图片数据
