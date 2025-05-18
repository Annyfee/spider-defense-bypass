
# 目标爬取对应网站五页的标题，老师与对应学校

import requests

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'referer': 'https://www.icve.com.cn/portal_new/course/course.html'
}

# 多页数据爬取(假设爬取五页)
k = 1
for n in range(1,6):
    url = f'https://www.icve.com.cn/portal/course/getNewCourseInfo?page={n}'
    print(f'正在爬取第{n}页')
    response = requests.post(url, headers=header)
    data = response.json()
    # 单页数据爬取
    for i in data['list']:
        title = i['Title']
        Teacher = i['TeacherDisplayname']
        UnitName = i['UnitName']
        print(k, title, Teacher, UnitName)
        k += 1
