from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
import requests
from lxml import etree
from bs4 import BeautifulSoup

def download_pic(url,i):
    name = url.rstrip("/")[1]
    print(f"开始下载第{i}张:{name}")
    res=requests.get(url)  # 相当于requests
    with open("优美图库/"+name, mode='wb') as f:  # 创建文件
        f.write(resp.content)
        print(f"完成第{i}张:{name}")

if"__name__"=="__main__":
    url = "https://www.umeitu.com/meinvtupian/xingganmeinv/index_2.htm"
    header = {"User-Agent": UserAgent().chrome}
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    i=1
    urls = []
    main_page = BeautifulSoup(resp.text, "html.parser")
    alist = main_page.find("div", class_="TypeList").find_all("a")
    for a in alist:
        href = a.get('href')  # 直接通过get就可以拿到属性的值
        childhref = url.split("om/")[0] + "om" + href
        child_page_resp = requests.get(childhref)
        child_page_resp.encoding = 'utf-8'
        child_page_text = child_page_resp.text
        child_page = BeautifulSoup(child_page_text, "html.parser")
        d = child_page.find("div", class_="ImageBody")
        img = d.find("img")
        src = img.get("src")
        urls.append(src)

    with ThreadPoolExecutor(50) as t:
        for url in urls:
            t.submit(download_pic, url,i)
            print(f"{url}提取完毕！")
        print("全部完成！")


