import wordcloud
import imageio
import jieba
from matplotlib import pyplot as plt
import re

mk=imageio.imread(r'D:/pythonProject/素材/12.jpg')

wc=wordcloud.WordCloud(font_path='simhei.ttf',
                background_color="black",
                mask=mk,
                # width=1000,
                # height=800,
                # font_step=1,
                # min_font_size=6,
                # max_words=200,
                # contour_width=1,
                # contour_color="black",
                # stopwords={","},
                scale=5,
                # random_state=48,
                colormap="Set1")


with open('D:/pythonProject/MyPractice/胡林西全班.txt',mode="r",encoding='utf8') as f:
    wordtext=f.read()
    newtext = re.sub('[，。、“”‘ ’]', '', wordtext)
    wordlist=newtext.split(" ")
    wordstring=" ".join(wordlist)
    wc.generate(wordstring)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    wc.to_file(r'D:\pythonProject\MyPractice\1111.jpg')