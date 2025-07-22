import scrapy
from biliDB.items import BilidbItem

class BiliSpider(scrapy.Spider):
    name = "bili"
    # allowed_domains = ["www.xxxx.com"]
    start_urls = ["https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B"]

    def parse(self, response):
        li_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[3]/div')
        for li in li_list:
            titles = li.xpath('//h3[@class="bili-video-card__info--tit"]/@title').extract()
            authors = li.xpath('//span[@class="bili-video-card__info--author"]/text()').extract()
            for title, author in zip(titles, authors):
                # 创建items类型对象/容器
                item = BilidbItem()
                # 解析到数据存储至item对象
                item['title'] = title
                item['author'] = author
                yield item # 提交给管道
