import os.path
import time
from itertools import zip_longest

from lxml import etree
import requests
from DataRecorder import Recorder
from concurrent.futures import ThreadPoolExecutor # 多线程


# 初始化excel文件
def get_excel():
    filename = 'top250电影_多线程.xlsx'
    if os.path.exists(filename):
        os.remove(filename)
        print('\n旧文件已清除\n')
    recorder = Recorder(filename)
    recorder.show_msg = False
    return recorder

def get_msg(page_index):
    session = requests.session()
    # 初始化爬取数据
    url = f'https://movie.douban.com/top250?start={page_index*25}&filter='
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
    data = []
    for title,score,comment in zip_longest(titles,scores,comments,fillvalue='无'):
        # print(f'{total_index}.电影名:{title},评分:{score},短评:{comment}')
        data.append({
            '电影名':title,
            '评分':score,
            '短评':comment
        })
    return data


if __name__ == '__main__':
    start_time = time.time()
    recorder = get_excel()

    # 创建一个 最多同时运行 5 个线程 的线程池 executor用于并发执行任务。 with ... as ...：用上下文管理器，自动管理线程池的创建和销毁
    with ThreadPoolExecutor(max_workers=5) as executor:
        # executor.map(func, iterable) 会为 iterable 中的每个值并发执行一次 func
        results = list(executor.map(get_msg,range(10))) # 嵌套列表

    # 统一处理所有数据并录入
    total_index = 1
    for movies in results:
        for movie in movies:
            movie['序号'] = total_index
            print(f"{total_index}. 电影名:{movie['电影名']}, 评分:{movie['评分']}, 短评:{movie['短评']}")
            recorder.add_data(movie)
            recorder.record()
            total_index+=1
    end_time = time.time()
    use_time = end_time - start_time
    print(f'\n共用时:{use_time:.2f}秒!')

# 共用时:5.79秒!

