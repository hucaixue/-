#导入库
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
#网易云官网 搜索薛之谦跳转网页后  检查  network  doc 找到该网页的
#Request URL: https://music.163.com/artist?id=5781

#1、确定url地址(薛之谦的歌单）
url = 'https://music.163.com/discover/toplist?id=3778678'
#网易云音乐的外链地址
base_url = 'https://link.hhtjim.com/163/'
#2、请求

headers= {
        "User-Agent": UserAgent().chrome
}
result = requests.get(url, headers=headers).text
#3、删选数据 拿到列表中的歌曲id  为一个字典 里面有每首个的id
dom =etree.HTML(result)
# 通过审查元素发现每首歌在<a href="/song?id=417859631"> 中通过xpath分析得获取所有歌曲id的xpath语句为'//a[contains(@href,"/song?")]/@href'
ids = dom.xpath('//ul[@class="f-hide"]//li/a/@href')
#将数据切片只需要id数值
#正则表达式
for i in range(len(ids)):
    ids[i] = re.sub('\D', '', ids[i])
#print(ids)


for i in range(len(ids)):
    #每一首歌的地址
    M_url = f'https://music.163.com/song?id={ids[i]}'
    response = requests.get(M_url, headers=headers)
    html = etree.HTML(response.text)
    music_info = html.xpath('//title/text()')
    #print(music_info)   #['我好像在哪见过你（电影《精灵王座》主题曲） - 薛之谦 - 单曲 - 网易云音乐']
    music_name = music_info[0].split('-')[0]
    singer = music_info[0].split('-')[1]
    #print(music_name, singer)  #我好像在哪见过你（电影《精灵王座》主题曲）   薛之谦

    #获取歌源
    music_url = base_url + str(ids[i]) + '.mp3'
    #print(music_url)    #打印出每首歌的外链网址
    music = requests.get(music_url).content

    #4、保存
    with open('./music/'+music_name+'.mp3', 'wb') as file:
        file.write(music)
    print("正在下载第"+str(i+1)+"首:  "+music_name+singer)
