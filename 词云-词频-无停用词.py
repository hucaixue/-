import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import imageio

txt = open("D:/pythonProject/素材/弹幕.txt", encoding="utf-8").read()
mk=imageio.imread("..\素材\中国地图01.jpg")

count = jieba.lcut(txt)

fre_dic ={}
for word in count:
    fre_dic[word] = fre_dic.get(word, 0) + 1
lst=sorted(fre_dic.items(), key=lambda data: data[1],reverse=True)
frequencies={}
for i in lst:
    frequencies[i[0]]=i[1]

stopwords = set()
content = [line.strip() for line in open('D:/pythonProject/素材/stopwords.txt','r',encoding="utf-8").readlines()]
stopwords.update(content)

wc = WordCloud(font_path="C:/Windows/Fonts/simfang.ttf",
        max_words=100,
        width=2000,
        height=1200,
        mask=mk,
        stopwords=stopwords,
        colormap="Set1")

word_cloud = wc.generate_from_frequencies(frequencies)
# 写词云图片
word_cloud.to_file("create_word_cloud_by_words_count.jpg")
# 显示词云文件
plt.imshow(word_cloud)
plt.axis("off")
plt.show()