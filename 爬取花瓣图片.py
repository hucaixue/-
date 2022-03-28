import json
import time
import requests
from fake_useragent import UserAgent
from tqdm import tqdm
from PIL import Image
import os

url1="https://api.huaban.com/search?q=%E5%BD%93%E6%8F%92%E7%94%BB%E5%B8%88%E7%A7%80%E8%B5%B7%E6%81%A9%E7%88%B1%E6%9D%A5&sort=all&per_page=20&page=4"
url = "https://huaban.com/search?q=%E5%BD%93%E6%8F%92%E7%94%BB%E5%B8%88%E7%A7%80%E8%B5%B7%E6%81%A9%E7%88%B1%E6%9D%A5&sort=all"
headers = {
    "User-Agent":UserAgent().chrome}
res=requests.get(url1,headers=headers)
dic=res.json()
i=61
pins=dic["pins"]
for pin in tqdm(pins):
    boardid=pin["board_id"]
    key=pin["file"]["key"]
    pic_src="https://hbimg.huabanimg.com/"+key+"_fw658/format/webp"
    print(pic_src)
    picres=requests.get(pic_src,headers=headers)
    with open(f"图片/第{i}张.jpg",mode="wb") as f:
        f.write(picres.content)
        print(f"完成一张{boardid}")
    time.sleep(1)
    i+=1
print("全部完成！")

# source_path = "D:\\pythonProject\\MyPractice\\图片\\"
# des_path = "D:\\pythonProject\\MyPractice\\图片\\"
# source_file = os.listdir(source_path)
# for file_name in source_file:
#     print(f"正在转换{source_path}{file_name}")
#     image = Image.open(f"{source_path}{file_name}")
#     file_name = file_name[:-4]
#     print(f"正在保存{des_path}{file_name}.jpg")
#     image.save(f"{des_path}{file_name}.jpg")
# print("图片转换完毕")