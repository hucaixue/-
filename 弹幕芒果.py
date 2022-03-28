import pprint
import requests
from fake_useragent import UserAgent
import time
import pandas as pd

url="https://bullet-ali.hitv.com/bullet/2022/03/20/051754/12281642/0.json"
headers = {"User-Agent": UserAgent().chrome}
res=requests.get(url,headers=headers)

df = pd.DataFrame()
items=res.json()["data"]["items"]

for item in items:
    time=item["time"]
    content=item["content"]
    print(time,content)
    text = pd.DataFrame({'时间': [time], '弹幕': [content]})
    df = pd.concat([df, text])
df.to_csv('悬崖之上.csv', encoding='utf-8', index=False)
    # text = pd.DataFrame({'弹幕': [content]})
    # df = pd.concat([df, text])
# df.to_csv('革命者_弹幕.csv', encoding='utf-8', index=False)
