# 实现爬取下厨房网站中任意菜谱搜索结果数据爬取
import requests
from lxml import etree


url = 'https://www.xiachufang.com/search/'
header = {
'referer':'https://www.xiachufang.com/search/?keyword=%E9%B8%A1%E8%9B%8B&cat=1001',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}
key = input('请输入您喜欢的食材')
params={
'keyword':key,
'cat':'1001'
}
response = requests.get(url,headers=header,params=params).text
tree = etree.HTML(response)
title_base = tree.xpath('//ul[@class="list"]')
#
for i in title_base:
    titles = i.xpath('.//p[@class="name"]/a/text()')
    for title in titles:
        print(title.strip())

