import json

import requests
from new_cookie import save_cookies,get_new_cookie



url = 'https://sf.taobao.com/item_list.htm?_input_charset=utf-8&q=&spm=a213w.7398504.search_index_input.1&keywordSource=5'

with open('cookie.json','r',encoding='utf8')as f:
    cookies = json.load(f) # 从文件直读

flag = True
if flag:
    print('遇到反爬...更新cookie...')
    get_new_cookie(url)
    print('新cookie获得成功!')


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://sf.taobao.com/list/0_____%C9%EE%DB%DA.htm?spm=a213w.7398504.pagination.1.36c21615Iqzq5r&auction_source=0&st_param=-1&auction_start_seg=0&auction_start_from=2025-08-07&auction_start_to=2025-09-30&q=%B7%BF%B2%FA&page=2',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 't=7c87d28becbff649135402c8394fe3d4; wk_cookie2=187686c75c60e47705ddf2231ea28abc; wk_unb=UUpgR1v6otGfysRtfw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; _uetvid=1f746fe037c311f08a6cc3c8035c6ce9; aui=2211901778683; thw=cn; cna=I8vhHnFt3EwCAXjry/Q6YMix; tracknick=tb9637658592; sn=; uc3=vt3=F8dD2fnqa9crc23byrI%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&nk2=F5RMHy8mIWUL74ML&id2=UUpgR1v6otGfysRtfw%3D%3D; csg=17a31290; lgc=tb9637658592; cancelledSubSites=empty; dnk=tb9637658592; skt=1fc8546036fcd897; existShop=MTc1Mzc3Nzc3OQ%3D%3D; uc4=nk4=0%40FY4HWrZETjmS5CNmnn3odzjwzx4sMTc%3D&id4=0%40U2gqyOZjcBXJtSK9LYN2Anu2eXYBJcOf; _cc_=W5iHLLyFfA%3D%3D; sgcookie=E100Ivtiu912QpYb8r3H%2BClZvPSXjjzy8MYqidkIR4%2FjKTPjuV%2FW2XlkKIIPg8QXjvKECCHjhUZxRv0fBTK5NHr%2FTx92k9PCyFBLXG5tNrXJRZY%3D; 3PcFlag=1754710767171; xlly_s=1; isg=BAIC-dH93kXTUMxboakkfnOPUwhk0wbtBpyU-kwbdnUgn6IZNGE4_Y_MSZvjz36F; mtop_partitioned_detect=1; _m_h5_tk=06c72fd4e126769ac097835f7c4ca1bd_1754979539453; _m_h5_tk_enc=fc02a0c9d635626a0006afdffd45beb1; _m_h5_tk=332b6afccb6258416a92b3d2ff4ccf63_1754981699539; _m_h5_tk_enc=b04012cfe670ef1583928d5234c9a9f7; x5sec=7b2274223a313735343937313434342c22733b32223a2230306333356564633862363932623835222c22617365727665723b33223a22307c434f583536735147454e53716b6676382f2f2f2f2f774561447a49794d5445354d4445334e7a67324f444d374d6a447a764e32582b2f2f2f2f2f3842227d; tfstk=gBzoF4Al-uo7R38Wq605ViumXMjxP4gILJLKp2HF0xkXykFEp223KJD-YTg8--2bEULKz2rDt5w0KD1Spvk3pWrRMNQTN7gI82XOWNUWXlHzxXuEY67q62crnRVMo7gI8tdv8GQgN8s8ldDETj5m9XLeUJozgIlK3blr8Jkq0fl9U2uULs0qsfTy8Y8ygIlK3vuE8JPViXHqa2uULS5mOj2P4YaUurWhStstlvo0obmoQSj6Je_IadHgaYYe8YcoqhFrne8UokjhLkkPfIHIyYNmZJ_6P4o3Yz34zt7E7lw0-cuGv_izto2Iyr5e4Ar8eqzzjB8Ui4DUIrnMEtDaPSzsumQNsSzbe7a09B7EMRH4Nzuh71gozYumGyBXzvq4YznSRLWndrV4zkjrxn-NAVYIg6U2AHirGjDtRzzHuSYebgCcih5I4jGSBsfDAHirGjDOisxNV0ljNAC..',
}

response = requests.get(
    url,
    cookies=cookies,
    headers=headers,
).text
print(response)