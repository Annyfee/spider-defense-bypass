## tips
1. First仅用于熟悉使用命令，可以不看
2. bilipro则是对B站某个关键字搜索所返回的视频标题与作者并保存到csv中
3. biliDB同2，但它保存在数据库(mysql/redis)中
4. imgpro是爬取360搜索的图片页，保存图片
5. deeppro是爬取问政平台，涵盖到二次请求的深度爬取


## 操作流程
1. 安装环境：pip install scrapy
2. 创建一个项目：scrapy startproject xx -- xx即你的scrapy的项目命名
3. 创建爬虫文件： cd project_name(你刚刚创建的爬虫项目) 再scrapy genspider (爬虫文件名称) (起始url) 创建完成后就会在爬虫文件夹下生成一个爬虫文件
4. 先在你的爬虫文件里将allowed_domains注释掉(它是只允许域名内访问，没啥用)，再在设置里：
   1. 把ROBOTSTXT_OBEY改为False
   2. 写入LOG_LEVEL = 'ERROR' 只打印报错的日志信息 -- 这样就不会输出一大坨日志信息眼花缭乱
   3. USER_AGENT处去掉注释并写入正确UA(浏览器上的UA直接copy过来就行)
5. 写完你的所有爬虫逻辑后，运行:scrapy crawl (爬虫文件名称)

## 注意事项(bilirpo/biliDB)
1. scrapy不用写etree这些，它已经帮你封装好了，直接写xpath就行
2. 爬虫文件的def parse(self, response)，其中response就是响应对象，直接用它就行
3. scrapy中用xpath进行数据提取，获取到的是一个Selector对象，想要的文本数据是会被存储到该对象的内部
4. .extract()可以直接将Selector对象中的data属性的值取出来，而.extract_first()只能获取返回的第一个。所以当xpath返回一个时用.extract_first()，返回多个则用.extract()
5. 持久化存储有两种方式: 
   1. 基于终端指令(简单/局限):仅可将parse方法的返回值存储到指定后缀的文本文件中、运行指令：scrapy crawl bili(爬虫文件名) -o biliData(文件路径/保存文件名).csv(后缀)
   2. 基于管道形式(复杂/灵活--常用/能更好的利用scrapy的异步性能):
      1. 在爬虫文件中进行数据解析
      2. 将解析到的数据存储到一个items类型的对象中--先在items.py创建对应对象，再在爬虫文件里引入并创建对应容器，再将其存储
      3. 将item对象提交给管道(pipelines)
      4. 在管道中写process_item的函数，实现对item对象的接收，并对其进行指定形式的持久化存储
      5. 在settings文件中将管道ITEM_PIPELINES注释解开，开启管道
      6. 运行指令scrapy crawl bili(爬虫文件名)
6. 一个管道负责将数据存储到一个具体的载体/平台中，如想存储到另一个或多个平台，需创建多个管道。创建的新管道需要配置到settings的管道列表ITEM_PIPELINES中
7. 管道后的数字表示优先级。数字越小表明该管道的运行优先级越高。
8. yield是将数据提交给管道，当有多个管道时，会传递给优先级高的，则优先级高的就得再将该数据传递给其他管道(通过return)


## 注意事项(imgpro)
1. imgpro适用希望存储图片的框架
2. settings.py中可以写IMAGES_STORE作为爬取文件夹的存储路径
3. 爬取图片中的pipelines写的三个函数是固定写法，不能更改
4. 

## 注意事项(imgpro)