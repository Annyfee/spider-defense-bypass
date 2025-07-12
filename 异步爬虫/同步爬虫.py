import os.path
import time
from itertools import zip_longest

from lxml import etree
import requests
from DataRecorder import Recorder

# 初始化excel文件
def get_excel():
    filename = 'top250电影_同步.xlsx'
    if os.path.exists(filename):
        os.remove(filename)
        print('\n旧文件已清除\n')
    recorder = Recorder(filename)
    recorder.show_msg = False
    return recorder

def get_msg():
    session = requests.session()
    recorder = get_excel()
    total_index = 1
    # 循环爬取250个数据
    for j in range(10):
        # 初始化爬取数据
        url = f'https://movie.douban.com/top250?start={j*25}&filter='
        headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'referer':'https://movie.douban.com/top250?start=225&filter='
        }
        res = session.get(url,headers=headers).text
        tree = etree.HTML(res)
        # 获取其中关键数据
        titles = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
        scores = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
        comments = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')

        for title,score,comment in zip_longest(titles,scores,comments,fillvalue='无'):
            print(f'{total_index}.电影名:{title},评分:{score},短评:{comment}')
            map_={
                '序号':total_index,
                '电影名':title,
                '评分':score,
                '短评':comment
            }
            recorder.add_data(map_)
            recorder.record()
            total_index+=1



if __name__ == '__main__':
    # 计时
    start_time = time.time()
    get_msg()
    end_time = time.time()
    use_time = end_time - start_time
    print(f'共用时:{use_time:.2f}秒!')

# 共用时:7.24秒!