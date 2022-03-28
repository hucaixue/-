import json
import re
import requests
from fake_useragent import UserAgent

mainurl = "https://www.91kanju2.com/vod-play/61525-1-2.html"
headers = {"User-Agent": UserAgent().chrome}
res1= requests.get(mainurl, headers=headers)
obj1=re.compile(r"url: '(?P<url>.*?)',",re.S)
obj2=re.compile(r"<title>(?P<filmtitle>.*?)</title>",re.S)
src_url=obj1.search(res1.text).group("url")
filmname=obj2.search(res1.text).group("filmtitle")
m3u8_data=requests.get(src_url,headers=headers).text
video_urls=re.sub(r"#E.*","",m3u8_data).split()
for video_url in video_urls:
    res2=requests.get(video_url,headers=headers)
    with open("video/"+f"{filmname}.mp4",mode="ab") as f:
        f.write(res2.content)
        f.close()

print("完成下载!")
