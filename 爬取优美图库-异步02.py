import aiohttp
import asyncio
import aiofiles
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

#https://www.umeitu.com/bizhitupian/weimeibizhi/

# url = input("请输入您的网址：")
url="https://www.umeitu.com/meinvtupian/xingganmeinv/index_2.htm"
header = {"User-Agent": UserAgent().chrome}
resp = requests.get(url)
resp.encoding = 'utf-8'
urls=[]
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a")
for a in alist:
    href = a.get('href')  # 直接通过get就可以拿到属性的值
    childhref=url.split("om/")[0] +"om"+href
    child_page_resp = requests.get(childhref)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    child_page = BeautifulSoup(child_page_text, "html.parser")
    d = child_page.find("div", class_="ImageBody")
    img = d.find("img")
    src = img.get("src")
    urls.append(src)
print(urls)

async def aioDownload(url,i):
    name = url.rsplit("/", 1)[1]
    print(f"开始下载第{i}张:{name}")
    async with aiohttp.ClientSession() as session:  # 相当于requests
        async with session.get(url) as resp:  # 相当于resp = requests.get()
            # 请求回来了，aiofiles写入文件，
            async with aiofiles.open("优美图库/"+name, mode='wb') as f:  # 创建文件
                await f.write(await resp.content.read())
                print(f"完成第{i}张:{name}")

async def main():
    tasks = []
    i=1
    for url in urls:
        task = asyncio.create_task(aioDownload(url,i))
        tasks.append(task)
        i+=1
    await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()