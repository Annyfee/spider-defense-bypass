# 爬取该页面中的《越女剑》，在获取对应章节的标题同时，对标题的链接进行二次访问，再获取每个章节的具体内容，并最终输出保存在文件夹里。

import os
import random
import re
import time

import requests
from lxml import etree

url = 'https://yuenvjian.5000yan.com/'
headers = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
'referer':'https://5000yan.com/'
}
session = requests.session()

if not os.path.exists('越女剑'):
    os.mkdir('越女剑')
response = session.get(url,headers=headers)
response.encoding = 'utf8'
tree = etree.HTML(response.text)
a_list = tree.xpath('/html/body/div[2]/div[1]/div[1]/div[3]/ul/li/a')
for a in a_list:
    if a == a_list[0]:
        continue
    title = a.xpath('./text()')[0]
    href = a.xpath('./@href')[0]
    response_detail = session.get(url=href,headers=headers)
    response_detail.encoding = 'utf8'
    tree = etree.HTML(response_detail.text)
    contents = tree.xpath('/html/body/div[2]/div[1]/div[1]/div[3]/div[4]/p/text()')
    content = ''.join(contents)
    content = re.sub(r'\s+','',content)
    with open(f'./越女剑/{title}.txt','w',encoding='utf8') as f:
        f.write(content)
    print(f'{title}爬取成功!')
print(f'全部爬取完成!共计爬取{len(a_list)-1}条数据!')


