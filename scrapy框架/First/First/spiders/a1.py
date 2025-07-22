import scrapy


class A1Spider(scrapy.Spider):
    # 爬虫文件唯一标识
    name = "a1"
    # 允许域名才能发请求 -- 没啥用，通常注释掉
    # allowed_domains = ["www.baidu.com"]
    # 起始url列表 -- 列表内部url都会被框架进行异步请求发送
    start_urls = ["https://www.xiachufang.com/category/40073/"]

    # 数据解析 response即响应对象
    def parse(self, response): # parse调用次数取决于start_urls列表元素的个数
        li_list = response.xpath('/html/body/div[3]/div/div/div[1]/div[1]/div/div[2]/div[2]/ul/li')
        for li in li_list:
            # 在 Scrapy 中，当你使用 XPath 或 CSS 选择器提取数据时，通常会得到一个 Selector 或 SelectorList 对象。
            # 而用.get() 方法就可以从 Selector 或 SelectorList 对象中提取第一个匹配的字符串值。
            title = li.xpath('./div/div/p[1]/a/text()').get().strip()
            print(title)
