import scrapy
from deeppro.items import DeepproItem

class DeepSpider(scrapy.Spider):
    name = "deep"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1"]

    page_num = 1
    url_model = f"https://wz.sun0769.com/political/index/politicsNewest?id=1&page="

    def parse(self, response):
        ul = response.xpath('//ul[@class="title-state-ul"]/li')
        for li in ul:
            title = li.xpath('.//a[@class="color-hover"]/text()').extract_first().strip()
            state = li.xpath('.//span[@class="state2"]/text()').extract_first().strip()

            item = DeepproItem()
            item['title'] = title
            item['state'] = state
            href = 'https://wz.sun0769.com/'+li.xpath('.//a[@class="color-hover"]/@href').extract_first()
            yield scrapy.Request(url=href,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 3:
            print(f'正在爬取第{self.page_num}页的数据...')
            new_url = f'{self.url_model}{self.page_num}'
            self.page_num+=1
            yield scrapy.Request(url=new_url,callback=self.parse)

    def parse_detail(self,response):
        content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        meta_ = response.meta
        item = meta_['item']
        item['content'] = content
        yield item


