import wordcloud
import imageio
import jieba
from matplotlib import pyplot as plt
import re

mk=imageio.imread(r'..\素材\中国地图01.jpg')

stopwords = set()
content = [line.strip() for line in open('D:/pythonProject/素材/stopwords.txt','r').readlines()]
stopwords.update(content)

wc=wordcloud.WordCloud(font_path='simhei.ttf',
                background_color="black",
                mask=mk,
                width=1000,
                height=800,
                # font_step=1,
                # min_font_size=6,
                # max_words=200,
                contour_width=1,
                contour_color="black",
                stopwords=stopwords,
                scale=5,
                # color_func=wordcloud.get_single_color_func("red"),
                colormap="Set1")


with open('D:/pythonProject/MyPractice/datajieba.txt',mode="r",encoding='utf8') as f:
    wordtext=f.read()
    newtext = re.sub('[，。、“”‘ ’]', '', wordtext)
    wordlist=jieba.lcut(newtext)
    wordstring=" ".join(wordlist)
    wc.generate(wordstring)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    wc.to_file(r'D:\pythonProject\MyPractice\0000.png')