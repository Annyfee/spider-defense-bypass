import time

import requests
from lxml import etree
import os
url = 'https://sc.chinaz.com/tupian/index.html'
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
'referer':'https://sc.chinaz.com/tupian/index_2.html'
}
if not os.path.exists('图片集'):
    os.mkdir('图片集')
session = requests.session()
response = session.get(url,headers=header)
response.encoding = 'utf8'
tree = etree.HTML(response.text)
img_link = tree.xpath('/html/body/div[3]/div[2]/div/img') # 里面没有值，自然用/text()获取到的是空值
n = 1
for img in img_link:
    time.sleep(0.1)
    title = img.xpath('./@alt')[0]
    url_pict = img.xpath('@data-original')[0]
    response_detail = requests.get(url=url_pict,headers=header).content
    with open(f'./图片集/{n}.{title}.png','wb') as f:
        f.write(response_detail)
    print(f'图片{n}.{title}已保存!')
    n+=1
print(f'所有图片都保存完毕!一共{len(img_link)}张图片!')


