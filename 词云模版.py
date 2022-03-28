import wordcloud
import imageio
import jieba
from matplotlib import pyplot as plt
import re

mk=imageio.imread(r'..\素材\中国地图01.jpg')
wc=wordcloud.WordCloud(width=1000,
                    height=800,
                    background_color='black',
                    font_path='simhei.ttf',
                    font_step=1,
                    min_font_size=6,
                    max_words=200,
                    stopwords={","},
                    scale=5,
                    mask=mk)

with open('文稿.txt',mode="r",encoding='utf8') as f:
    wordtext=f.read()
    newtext = re.sub('[，。、“”‘ ’]', '', wordtext)
    wordlist=jieba.lcut(newtext)
    wordstring=" ".join(wordlist)
    wc.generate(wordstring)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    wc.to_file(r'D:\pythonProject\MyPractice\1122.png')
