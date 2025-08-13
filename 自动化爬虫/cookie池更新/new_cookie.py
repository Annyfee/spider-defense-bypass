import json
import time

from DrissionPage import ChromiumPage
from DrissionPage._configs.chromium_options import ChromiumOptions


def save_cookies(cookies, file='cookie.json'):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(cookies, f, ensure_ascii=False,indent=2)


# url = 'https://sf.taobao.com/item_list.htm?_input_charset=utf-8&q=&spm=a213w.7398504.search_index_input.1&keywordSource=5'

def get_new_cookie(url):
    page = ChromiumPage()
    page.get(url)

    # 进入页面先保存一次 cookie
    page.wait.load_start()
    cookies = page.cookies()
    new_cookies = {c['name']: c['value'] for c in cookies}
    save_cookies(new_cookies)
    print(f'已保存{len(new_cookies)}条')

def get_more_cookie(url,first_try=True):
    page = ChromiumPage()
    page.get(url)

    # 进入页面先保存一次 cookie
    page.wait.load_start()
    if first_try:
        cookies = page.cookies()
        new_cookies = {c['name']: c['value'] for c in cookies}
        save_cookies(new_cookies)
        return new_cookies
    # ---- 第二次才执行人工滑块 ----
    slider = page.ele('#nc_1__scale_text', timeout=0.1)
    if slider:
        print('正在处理反爬逻辑...')
        # 等页面刷新完成
        page.wait.load_start()
        page.wait.doc_loaded()  # 确保 DOM 加载完成
        time.sleep(0.5)  # 给 Cookie 同步留一点缓冲

    else:
        # 再极速轮询一次（最多再 0.5s）
        for _ in range(2):
            time.sleep(0.05)
            if page.ele('#nc_1__scale_text', timeout=0):
                print('正在处理反爬逻辑...')

                # 等页面刷新完成
                page.wait.load_start()
                page.wait.doc_loaded()  # 确保 DOM 加载完成
                time.sleep(0.5)  # 给 Cookie 同步留一点缓冲
                break
        else:
            print('无滑块，自动继续...')

    # 无论是否人工，都抓最新 cookie
    cookies = page.cookies()
    new_cookies = {c['name']: c['value'] for c in cookies}
    save_cookies(new_cookies)
    return new_cookies
