# 问政平台 -- 使用代理并获取当前页的标题与对应代码
import random
import time
import requests
from lxml import etree
import os

url = 'https://wz.sun0769.com/political/index/supervise'
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
'referer':'https://wz.sun0769.com/political/index/politicsNewest?id=1&page=3'
}

# 代理链接
def get_proxy():
    url_proxy = '你的api接口'
    res = requests.get(url_proxy).text
    return res.strip().split('\r\n')


proxy_list = get_proxy()

session = requests.session()


response = session.get(url, headers=header,proxies={'https': random.choice(proxy_list)})
tree = etree.HTML(response.text)
a_link = tree.xpath('/html/body/div[2]/div[3]/ul/li/span[3]/a')
n = 1
for a in a_link:
    href = a.xpath('./@href')[0]
    href = 'https://wz.sun0769.com/'+href
    title = a.xpath('./text()')[0]
    response = session.get(url=href,headers=header,proxies={'https':random.choice(proxy_list)})
    tree = etree.HTML(response.text)
    content = tree.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()')[0]
    with open('询问集.txt','a',encoding='utf8') as f:
        f.write(f'{n}'+title+'\r'+content+'\r\n')
    print(f'第{n}条数据已保存!')
    n+=1
print(f'所有数据已保存!共计保存{a_link}条数据!')


