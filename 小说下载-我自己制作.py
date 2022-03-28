# import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from tqdm import tqdm

url = "https://www.biqupai.com/77_77362/"
headers = {"User-Agent": UserAgent().chrome}
data={"Referer": "https://www.biqupai.com/"}
res1= requests.get(url,headers=headers,data=data)
res1.encoding="utf-8"
page1 = BeautifulSoup(res1.text, 'html.parser')
chapters = page1.find('div', id='list')
chapters = chapters.find_all('a')
for chapter in tqdm(chapters):
    chapter_name = chapter.text
    href=chapter.get("href")
    securl=url.split("com")[0]+"com"+href

    res2=requests.get(securl,headers=headers)
    res2.encoding = "utf-8"
    page2 = BeautifulSoup(res2.text, 'html.parser')
    texts = page2.find('div', id='content')
    content=texts.text.strip().split("\xa0" * 4)
    with open("大明妖孽.txt",mode="a",encoding="utf-8") as f:
        f.write(chapter_name)
        f.write('\n')
        f.write('\n'.join(content))
        f.write('\n')
    print("完成下载!")
