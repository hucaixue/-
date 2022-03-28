import requests
from bs4 import BeautifulSoup
import pandas as pd
import jieba
import wordcloud
from matplotlib import pyplot as plt

url= 'https://comment.bilibili.com/271973360.xml'

request = requests.get(url)
request.encoding='utf8'

soup = BeautifulSoup(request.text, 'lxml')
results = soup.find_all('d')
comments = [comment.text for comment in results]
comments = [x.upper() for x in comments]
comments_clean  = [comment.replace(' ','') for comment in comments]
# print(comments)
set(comments_clean)
useless_words = ['//TEST', '/TESR', '/TEST', '/TEST/', '/TEXT', '/TEXTSUPREME', '/TSET', '/Y', '\\TEST']
comments_clean = [element for element in comments_clean if element not in useless_words]#去掉不想要的字符
cipin = pd.DataFrame({'danmu':comments_clean})

cipin['danmu'].value_counts()
danmustr = ''.join(element for element in comments_clean)
words = list(jieba.cut(danmustr))
fnl_words = [word for word in words if len(word)>1]

mk=plt.imread(("..\素材\中国地图01.jpg"))

wc = wordcloud.WordCloud(width=1000, font_path='simfang.ttf',height=800,mask=mk,colormap="Set1")
wc.generate(' '.join(fnl_words))
plt.imshow(wc)#看图
plt.axis('off')
plt.show()  #显示图片
wc.to_file(r"D:\pythonProject\danmu_pic.png")#保存
print("完成！")
