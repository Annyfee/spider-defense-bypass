import scrapy
from bilipro.items import BiliproItem


class BiliSpider(scrapy.Spider):
    name = "bili"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://search.bilibili.com/all?keyword=%E7%BC%96%E7%A8%8B"]

    # # 测试代码
    # def parse(self, response):
    #     li_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[3]/div')
    #     for li in li_list:
    #         titles = li.xpath('//h3[@class="bili-video-card__info--tit"]/@title').extract()
    #         authors = li.xpath('//span[@class="bili-video-card__info--author"]/text()').extract()
    #         for title,author in zip(titles,authors):
    #             print(title,author)

    # # 基于终端指令实现数据持久化存储 -- 仅可将parse方法的返回值存储到指定后缀的文本文件中 -- scrapy crawl bili -o (文件路径/保存文件名).csv(后缀)
    # def parse(self, response):
    #     li_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[3]/div')
    #     all_data = []
    #     for li in li_list:
    #         titles = li.xpath('//h3[@class="bili-video-card__info--tit"]/@title').extract()
    #         authors = li.xpath('//span[@class="bili-video-card__info--author"]/text()').extract()
    #         for title,author in zip(titles,authors):
    #             dic = {
    #                 'title':title,
    #                 'author':author
    #             }
    #             all_data.append(dic)
    #     print(all_data)
    #     # 爬取到数据被作为parse方法的返回值
    #     return all_data

    # 基于管道实现的持久化存储 -- 常用
    def parse(self, response):
        li_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[3]/div')
        for li in li_list:
            titles = li.xpath('//h3[@class="bili-video-card__info--tit"]/@title').extract()
            authors = li.xpath('//span[@class="bili-video-card__info--author"]/text()').extract()
            for title, author in zip(titles, authors):
                # 创建items类型对象/容器
                item = BiliproItem()
                # 解析到数据存储至item对象
                item['title'] = title
                item['author'] = author
                yield item # 提交给管道