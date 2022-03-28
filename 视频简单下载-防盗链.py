import requests
import re
from fake_useragent import UserAgent

# n=1
headers={"User-Agent":UserAgent().chrome}
# url="https://www.91kanju2.com/vod-play/31151-1-1.html"
# res=requests.get(url,headers=headers)
# obj=re.compile(r"url: '(?P<url>.*?)',",re.S)
# m3u8_url=obj.search(res.text).group("url")
# res.close()
# print(m3u8_url)

n=1
m3u8_url="https://v4.cdtlas.com/20220317/JkFC2EXO/1100kb/hls/index.m3u8"

res2=requests.get(m3u8_url,headers=headers)
with open("video.m3u8",mode="wb") as f:
    f.write(res2.content)
res2.close()
print("m3u8文件下载完毕!")


with open("video.m3u8", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # 先去掉空格, 空白, 换行符
        if line.startswith("#"):  # 如果以#开头. 我不要
            continue
        # 下载视频片段
        resp3 = requests.get(line)
        f = open(f"video/{n}.ts", mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n += 1
        print(f"完成第{n-1}个")