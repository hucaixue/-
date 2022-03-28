from wordcloud import WordCloud
import jieba
from collections import Counter
from imageio import imread
import matplotlib.pyplot as plt

"""读取停用词"""
with open("D:/pythonProject/素材/stopwords.txt", "r", encoding="utf-8") as fp:
    stopwords = set([s.rstrip() for s in fp.readlines()])  # 数组转集合

"""获取文本内容"""
with open("D:/pythonProject/MyPractice/datajieba.txt", "r", encoding="utf-8") as fp:
    content = fp.read()

"""中文分词"""
content = jieba.lcut(content)

"""去除停用词"""
text = []
for word in content:
    if word not in stopwords:
        text.append(word)

frequency = dict(Counter(text))  # 去掉停用词后的词频统计

mask_image = imread("..\素材\中国地图01.jpg")

wc = WordCloud(font_path='C:/Windows/Fonts/simhei.ttf',  # 字体
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