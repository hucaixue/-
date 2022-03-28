import requests
from lxml import etree
import re
from fake_useragent import UserAgent

url = 'https://music.163.com/artist?id=7115'
headers = {'user-agent':UserAgent().chrome,'referer':'https://music.163.com/'}
res = requests.get(url,headers=headers)

obj = re.compile(r'/song\?id=(\d+)">(.*?)</a>')
result=obj.findall(res.text)

wl = 'https://link.hhtjim.com/163/{}.mp3'

for id, name in result:
    url = wl.format(id)
    song = requests.get(url,headers=headers).content # 获取音乐的二进制文件
    name = name+".mp3"

    with open(f'./网易云音乐/{name}','wb') as file:
        file.write(song)

    print(f'歌曲：{name.rstrip(".mp3")}','下载完毕!')