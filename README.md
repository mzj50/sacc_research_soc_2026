# 暑假大作战题目要求
---

## 必做任务
- 抓取学校[创新创业教育学院官网](https://cxcy.njupt.edu.cn/ "就是这个") 的“通知公告”版块，提取出前五条通知的标题、发布日期、详情页完整URL
  - 使用`requests + BeautifulSoup`, 或使用`Scrapy`
  - 添加`headers`和延时
  - 提取的详情页链接拼接为绝对路径，可使用`urljoin`
- 数据格式化输出为本地文件(如 CSV、JSON 等)

## 可选任务
- 向你的个人邮箱推送通知汇总
  - 邮件正文包含标题、发布日期、链接
  - 使用`smtplib`和`email`库，支持`SMTP_SSL`加密连接
  - 不要把发件人邮箱、授权码、收件人邮箱提交上来，记得使用`.env`文件并`.gitignore`掉它们

---
## 简单例子
### requests + BeautifulSoup
1. 安装依赖 如果不用lxml,也可以使用Python内置的`html.parser`
```bash
pip install beautifulsoup4 requests lxml
```

2. 创建 `main.py` 爬取网站以 Bing 为例
```python
from bs4 import BeautifulSoup
import requests

url = 'https://cn.bing.com/'

response = requests.get(url)
response.encoding = 'utf-8' 

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    title_tag = soup.find('title')
    if title_tag:
        print(title_tag.get_text())
    else:
        print("未找到<title>标签")
else:
    print("请求失败，状态码：", response.status_code)
```

3. 运行，输出为`搜索 - Microsoft 必应` 
