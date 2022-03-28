import requests
from bs4 import BeautifulSoup
import pandas as pd
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from collections import Counter

url= 'https://comment.bilibili.com/271973360.xml'

request = requests.get(url)
request.encoding='utf8'

soup = BeautifulSoup(request.text, 'lxml')
results = soup.find_all('d')
comments = [comment.text for comment in results]
comments = [x.upper() for x in comments]
comments_clean  = "".join([comment.replace(' ','') for comment in comments])
# print(comments_clean)
content = jieba.lcut(comments_clean)
# print(content)

with open("D:/pythonProject/素材/stopwords.txt", "r", encoding="utf-8") as fp:
    stopwords = set([s.rstrip() for s in fp.readlines()])  # 数组转集合

"""去除停用词"""
text = []
for word in content:
    if word not in stopwords:
        text.append(word)

frequency = dict(Counter(text))  # 去掉停用词后的词频统计

mask_image = plt.imread("..\素材\中国地图01.jpg")

wc = WordCloud(font_path='C:/Windows/Fonts/simsun.ttc',  # 字体
               background_color="black",  # 背景色
               mask=mask_image,  # 遮罩
               # prefer_horizontal=0.6,  # 水平文字比例
               width=800,  # 宽度
               height=1000,  # 高度
               colormap="Set1"
               )

# wc.fit_words(frequency)
wc.generate_from_frequencies(frequency)

plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file("output.png")
