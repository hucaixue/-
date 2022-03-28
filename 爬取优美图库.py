import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'  # 处理乱码

# print(resp.text)
# 把源代码交给bs
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a")

for a in alist:
    href = a.get('href')  # 直接通过get就可以拿到属性的值
    childhref=url.split("/bi")[0] +href
    child_page_resp = requests.get(childhref)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    child_page = BeautifulSoup(child_page_text, "html.parser")
    p = child_page.find("p", align="center")
    img = p.find("img")
    src = img.get("src")
    # 下载图片
    img_resp = requests.get(src)
    # img_resp.content  # 这里拿到的是字节
    img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    with open("优美图库/"+img_name, mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件
    print("over!!!", img_name)
    time.sleep(1)

print("all over!!!")