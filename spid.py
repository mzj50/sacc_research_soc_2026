import requests
import time 
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import random
url = 'https://cxcy.njupt.edu.cn/'
response = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0'},timeout=10)
response.encoding = 'utf-8'
time.sleep(random.uniform(1,3))
date_tags = []
title_tags = []
links = []
sheets = [1,2,3,4,5]
data = []


def run_spider():
    try:
        if response.status_code == 200:
            print('访问成功！')
            soup = BeautifulSoup(response.content,'html.parser')
            txt1 = soup.find_all('span',attrs={'class':"news_title"})
            for span in txt1:                      # 遍历每个 span
                a_tag = span.find('a')             # 在当前 span 内找 a 标签（只取第一个）
                if a_tag:
                    title = a_tag.get_text(strip=True) 
                    title_tags.append(title)  # 获取标题文本
                    href = a_tag.get('href') if a_tag.get('href') else ''
                    if href:
                        link = urljoin (url,href)
                        links.append(link)
                    else:
                        links.append('')
                else:
                    title_tags.append('')
                    links.append('')
            txt2 = soup.find_all('span',attrs={'class':"news_meta"})
            for all_dates in txt2:
                date_tags.append(all_dates.get_text(strip=True))
            while len(date_tags) < len(title_tags):
                date_tags.append('')
            # data_append()
            # 现在将各个数据列表中的结果整合成字典，并存入data列表中
            for idx in range(1,6):
                data.append({'页面':sheets[idx-1],'日期':date_tags[idx-1],'标题':title_tags[idx-1],'详情链接':links[idx-1]})
            # print(data)
            #这里进行去重处理
            seen_titles = set()
            unique_data = []
            #现在对数据进行去重处理，保留第一次出现的标题
            for item in data:
                if item['标题'] not in seen_titles:
                    seen_titles.add(item['标题'])
                    unique_data.append(item)
            print(f'去重前: {len(data)} 条数据')
            print(f'去重后: {len(unique_data)} 条数据')
            print(unique_data)
            return unique_data
        else:
            print ('访问失败，状态码:', response.status_code)
    except Exception as e:
        print(f'爬虫模块运行发生错误{e}')
if __name__ =='__main__':
    run_spider()

