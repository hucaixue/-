import wordcloud
import jieba
import imageio
from matplotlib import pyplot as plt

image = imageio.imread(r'..\素材\中国地图01.jpg')

data = (file := open("D:/pythonProject/MyPractice/datajieba.txt", 'r', encoding="utf8")).read()
file.close()

# 将停用词添加到冻结集合
stopwords = frozenset(((file := open("D:/pythonProject/MyPractice/stopwords.txt", 'r', encoding="utf8")).read()).split())
file.close()


# 根据字体属性更改颜色
def color_func(word, /, font_size, position, random_state, **kwargs):
    # 字体位置 y
    if position[0] < 500:
        r = random_state.randint(0, 40)  # 相当于random.randint(0,40)
    else:
        r = random_state.randint(100, 150)

    # 字体位置 x
    if position[1] < 500:
        g = random_state.randint(0, 40)
    else:
        g = random_state.randint(100, 150)

    # 字体大小
    if font_size < 50:
        b = random_state.randint(0, 40)
    else:
        b = random_state.randint(100, 150)

    # 返回一个rgb颜色元组
    return (r, g, b)


wc = wordcloud.WordCloud(font_path="simhei.ttf",  # 字体路径
                         min_font_size=6, max_font_size=100,  # 字号
                         mask=image,  # 词云形状
                         color_func=color_func,  # 这里要将刚才写的函数传入
                         font_step=4,  # 字号步长
                         max_words=500,  # 最大词数
                         background_color="black")  # 背景色

filterfunc = lambda x: x not in stopwords and len(x) > 1
# 将停用词以及长度为1的字去除
words = filter(filterfunc, jieba.lcut(data, HMM=True))

# 生成词云
wc.generate(' '.join(words))

plt.imshow(wc)
plt.axis("off")
plt.show()
# 生成图片
wc.to_file("pywordcloud.png")