import os
import time

from DrissionPage import ChromiumPage

from DataRecorder import Recorder



def create_xlsx(keyword):
    filename = f'{keyword.strip()}.xlsx'
    # 如果文件已存在，先删除它
    if os.path.exists(filename):
        os.remove(filename)
        print(f'已清除旧文件: {filename}')
    # 创建新的recorder实例
    recorder = Recorder(filename)
    recorder.set.show_msg(False) # 移除多余打印信息
    return recorder

# 对返回的数据进行处理，用以获得希望返回的字符
def find_want(data, target_key):
    # 处理数据为字典的递归遍历
    if isinstance(data, dict):
        for key, val in data.items():
            if key == target_key:
                return val
            # 递归遍历子元素
            ret = find_want(val, target_key)
            if ret:
                return ret
    elif isinstance(data, list):
        for i in data:
            ret = find_want(i, target_key)
            if ret:
                return ret
    else:
        return None


# dp自动化抓取
def handler(page, keyword):
    recorder = create_xlsx(keyword)
    # 监听数据接口 -- 尽量写在最前面
    page.listen.start('web/v1/feed')  # 形如这种格式的会被抓取
    page.get(f'https://www.xiaohongshu.com/search_result?keyword={keyword}&source=web_profile_page')
    # time.sleep(2)
    page.wait.load_start()
    s = set()
    print(f'\n开始爬取{keyword}项...\n')
    # 爬取二十条数据
    data_count = 0
    max_count = 20
    error_count = 0
    scroll_interval = 5 # 每采集五条滚动一次
    while data_count < max_count:
        try:
            cards = page.eles('xpath://*[@id="global"]/div[2]/div[2]/div/div/div[3]/div[1]/section')
            for card in cards:
                if data_count >= max_count:
                    break
                # 去重
                index = card.attr('data-index')
                if index in s:
                    continue
                s.add(index)

                print(f'正在爬取第{data_count+1}条数据...')

                # 点击卡片并获取数据
                card.ele('xpath:./div/a[2]/img').click(by_js=True)  # 用js点击，如用默认的False，则是模拟点击，可能会被因为图层遮蔽无法点到
                res = page.listen.wait(count=1, timeout=3, fit_count=True)  # 匹配数量/超时等待时间/是否严格匹配
                data = res.response.body
                # 数据提取
                nickname = find_want(data, 'nickname')
                title = find_want(data, 'title')
                desc = find_want(data, 'desc')
                comment_count = find_want(data, 'comment_count')
                liked_count = find_want(data, 'liked_count')
                # 基于recorder将采集数据写入excel
                map_ = {
                    '博主昵称': nickname,
                    '标题': title,
                    '详情': desc,
                    '评论数': comment_count,
                    '点赞数': liked_count,
                }
                recorder.add_data(map_)
                recorder.record()

                # 关闭卡片+等待
                page.ele('xpath:/html/body/div[5]/div[2]/div').click()
                page.wait.load_start()
                # time.sleep(3)
                data_count+=1

                # 每采集一定数量滚动一次
                if data_count % scroll_interval == 0:
                    print('页面正进行滚动以加载更多内容...')
                    page.scroll.down(1000)
                    page.wait.load_start()
                    # break
        except Exception as e:
            print('error:::', e)
            error_count += 1
            if error_count > max_count:
                print(f'错误超过{max_count}次，停止采集!')
                break
            continue
    if data_count >= max_count:
        print(f'已爬取{data_count}条数据，{keyword}项打印完成!')
    else:
        print(f'{keyword}项采集未完成，共采集到{data_count}条数据')

# 主执行
def main():
    with open('关键字.txt', 'r', encoding='utf8') as f:
        keywords = f.readlines()
    # 浏览器驱动对象
    page = ChromiumPage()
    page.get('https://www.xiaohongshu.com/explore')

    # 等待操作(登录)
    input('请扫码登录,登录成功后按回车继续\n如已登录请直接按回车')

    for keyword in keywords:
        handler(page, keyword.strip())


main()
