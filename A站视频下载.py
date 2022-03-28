import json
import re
import requests
from fake_useragent import UserAgent

mainurl = "https://www.acfun.cn/v/ac33978961"
headers = {"User-Agent": UserAgent().chrome}
res1= requests.get(mainurl, headers=headers)
obj=re.compile(r"window.pageInfo = window.videoInfo = (?P<url>.*?);",re.S)
src_url=obj.search(res1.text).group("url")
json_data=json.loads(src_url)
title=json_data["title"]
videoinfo=json_data["currentVideoInfo"]["ksPlayJson"]
video_json=json.loads(videoinfo)
videourl=video_json["adaptationSet"][0]["representation"][0]["backupUrl"][0]

m3u8_data=requests.get(videourl,headers=headers).text
m3u8_data=re.sub("#E.*","",m3u8_data).split()
for index in m3u8_data:
    ts_url="https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/"+index
    res2=requests.get(ts_url,headers=headers)
    with open("video/"+f"{title}"+".ts",mode="ab") as f:
        f.write(res2.content)
        f.close()

print("完成下载!")
