import json
import re
import requests
from fake_useragent import UserAgent
from tqdm import tqdm

n=1
mainurl = "https://www.acfun.cn/v/ac34024039"
headers = {"User-Agent": UserAgent().chrome}
res1= requests.get(mainurl, headers=headers)
obj=re.compile(r"window.pageInfo = window.videoInfo = (?P<url>.*?);",re.S)
src_url=obj.search(res1.text).group("url")
json_data=json.loads(src_url)
title=json_data["title"]
videoinfo=json_data["currentVideoInfo"]["ksPlayJson"]
video_json=json.loads(videoinfo)
videourl=video_json["adaptationSet"][0]["representation"][0]["backupUrl"][0]
m3u8_data=requests.get(videourl,headers=headers).content

with open("下载密码.m3u8",mode="wb") as f:
    f.write(m3u8_data)
    f=open("下载密码.m3u8",mode="r",encoding="utf-8")
    for line in tqdm(f):
        if line.startswith("#"):
            continue
        print(f"开始下载第{n}段")
        ts_url="https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/"+line
        res2=requests.get(ts_url,headers=headers)
        with open("video/小视频.mp4",mode="ab") as f:
            f.write(res2.content)
        n+=1
print("完成下载!")
