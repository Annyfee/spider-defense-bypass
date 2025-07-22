# XPath 使用技巧

## ✅ 基本说明

- **XPath** 是一种用于在 **XML/HTML 文档中定位和选择节点**的语言。
- 常用于数据提取、爬虫开发，**返回结果永远是列表**。
- 常见解析工具：`XPath`（最常用） > `BeautifulSoup` > `正则`（效率低，但通用性更强）。

---

## 📌 基本语法

| 表达式 | 说明 |
|--------|------|
| `/` | 选取当前节点的直接子节点 |
| `//` | 选取当前节点下的所有子孙节点（全局搜索） |
| `.` | 当前节点 |
| `..` | 父节点 |

---

## 🧩 节点选取与属性获取

- **选取节点**：`//标签名[@属性名=属性值]`
- **获取属性**：`//标签名/@属性名`
- **获取文本**：`//标签名/text()`
- **获取子节点文本**：`//标签名//text()`（包含子节点的文本）

> ✅ 示例：
```python
link = selector.xpath('//a[@class="sister"]')[0]
href = link.xpath('./@href')[0]     # 获取属性
text = link.xpath('./text()')[0]    # 获取文本
```

---

## 🔍 常用技巧

### 1. 属性筛选
```xpath
//div[@id="main"]               # 选取 id 为 main 的 div
//a[@class="sister"]            # 选取 class 为 sister 的 a 标签
```

### 2. 文本筛选
```xpath
//p[text()="内容"]              # 选取文本为“内容”的 p 标签
//p[contains(text(), "内容")]   # 选取文本包含“内容”的 p 标签
```

### 3. 位置筛选（索引从 1 开始）
```xpath
//li[1]                        # 第一个 li
//li[last()]                   # 最后一个 li
//li[last()-1]                 # 倒数第二个 li
```

### 4. 模糊匹配
```xpath
//div[contains(@id, "he")]     # id 中包含 "he" 的 div
//div[starts-with(@id, "he")]  # id 以 "he" 开头的 div
```

### 5. 多条件查询
```xpath
//div[@id="main" and @class="content"]  # 同时满足两个属性
//div[@id="main" or @id="footer"]       # 满足任意一个属性
```

### 6. 多路径查询
```xpath
//title | //price              # 选取所有 title 和 price 标签
```

> ⚠️ 注意：`|` 两边必须是完整的 XPath 表达式。

---

## 📁 通配符（使用较少）

| 表达式 | 说明 |
|--------|------|
| `*` | 匹配任何元素节点 |
| `@*` | 匹配任何属性节点 |
| `node()` | 匹配任何类型的节点 |

---

## 📋 小贴士

- XPath 返回的是列表，即使只有一个结果，也要用 `[0]` 取值。
- 使用 `./` 表示当前节点继续查找。
- 若不确定结构，可用 `//node()` 查看所有节点。
- 获取节点文本内容推荐：`./text()`
- 获取节点属性推荐：`./@属性名`

---

## 🧪 示例代码片段

```python
from lxml import etree

html = '''你的 HTML 内容'''
selector = etree.HTML(html)

# 提取所有链接
links = selector.xpath('//a/@href')

# 提取特定文本
texts = selector.xpath('//a[@class="sister"]/text()')

# 遍历提取并处理
for link in links:
    print(link)
```

---

## ✅ 总结

本技巧表适用于快速查阅和使用 XPath，适合用于单个爬虫项目的 README，帮助理解数据提取逻辑，无需深入完整 XPath 教程。