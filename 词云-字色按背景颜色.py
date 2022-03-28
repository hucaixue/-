import wordcloud
from wordcloud import ImageColorGenerator
import jieba
from PIL import Image
import re
from matplotlib import pyplot as plt

mk=plt.imread(r'D:\pythonProject\素材\111.jpg')

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
                stopwords={","},
                scale=5,
                # color_func=wordcloud.get_single_color_func("red"),
                colormap="Dark2")

with open('D:/pythonProject/MyPractice/datajieba.txt',mode="r",encoding='utf8') as f:
    wordtext=f.read()
    newtext = re.sub('[，。、“”‘ ’]', '', wordtext)
    wordlist=jieba.lcut(newtext)
    wordstring=" ".join(wordlist)
    wc.generate(wordstring)

    img_colors = ImageColorGenerator(mk)  # 改变字体颜色
    wc.recolor(color_func=img_colors)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    wc.to_file(r'D:\pythonProject\MyPractice\0000.png')