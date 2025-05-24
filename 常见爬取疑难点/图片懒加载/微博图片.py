import os.path
import requests
from lxml import etree

url = 'https://blog.sina.com.cn/s/blog_01ebcb8a0102zj25.html'
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
'referer':'https://blog.sina.com.cn/s/articlelist_32230282_1_1.html'
}
session = requests.session()
response = session.get(url,headers=header)
response.encoding = 'utf8'

if not os.path.exists('西安图片集'):
    os.mkdir('西安图片集')

tree = etree.HTML(response.text)
title = tree.xpath('//*[@id="t_01ebcb8a0102zj25"]/text()')[0]

div_total_link = tree.xpath('//*[@id="sina_keyword_ad_area2"]')[0] # element对象必须以非列表形式才能xpath!!!

img_link = div_total_link.xpath('./a/img')
div_link = div_total_link.xpath('./div/a/img')
n = 1
for img in img_link:
    real_src = img.xpath('./@real_src')[0]
    response_detail = session.get(url=real_src,headers=header).content
    with open(f'./西安图片集/{n}.图片.png','wb') as f:
        f.write(response_detail)
    print(f'图片{n}写入完成!')
    n += 1

for div1 in div_link:
    real_src = div1.xpath('./@real_src')[0]
    response_detail = session.get(url=real_src,headers=header).content
    with open(f'./西安图片集/{n}.图片.png','wb') as f:
        f.write(response_detail)
    print(f'图片{n}写入完成!')
    n += 1

print(f'全部爬取完成!总计爬取{len(img_link)+len(div_link)}张图片!')
