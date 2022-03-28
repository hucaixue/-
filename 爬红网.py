import csv
import json
import requests
from fake_useragent import UserAgent
from lxml import html
import time
import csv

i=1
count = 1
f=open("红网.csv",mode="w")
csvwriter=csv.writer(f)

for i in range(10):
    i+=1
    first_url="https://rapi.rednet.cn/front/msg/index"
    headers={"User-Agent":UserAgent().chrome}
    keydata={
        "area_id": "",
        "cate_child_id": "",
        "cate_id": [],
        "city_id": "430100",
        "currentPage": i,
        "end_time": "",
        "is_reply": "3",
        "is_video": "",
        "page": i,
        "pageSize": 20,
        "page_num": 20,
        "search": "",
        "start_time": "",
        "type_id": "",
        "Referer":"https://people.rednet.cn"
    }

    res1=requests.post(first_url,headers=headers,data=keydata,)
    data_lst=res1.json()["data"]["rows"]

    for data_dic in data_lst:
        count+=1
        id=data_dic["id"]
        content=data_dic["title"]
        sec_url=first_url.rsplit("/",1)[0]+"/detail?id="+f"{id}"
        res2=requests.get(sec_url,headers=headers)
        content_dic=res2.json()["data"]
        # lastcontent=content_dic["content"].replace("<div>\n<p>","").replace("</p>\n</div>","").replace("<p>","")
        lastcontent = content_dic["content"].replace("<div>","").replace("</div>", "").replace("</p>", "").replace("<p>", "")
        # lastcontent =lastcontent.replace("</div>", "")
        # lastcontent = lastcontent.replace("</p>", "")
        # lastcontent = lastcontent.replace("<p>", "")
        title=content_dic["title"]
        print(f"第{count-1}长沙人民的呼声")
        print("标题是：",title)
        print("内容是：",lastcontent)
        # s1=f"第{count-1}长沙人民的呼声"
        # s2="标题是："+title
        # s3="内容是："+lastcontent
        # csvwriter.writerow([s1])
        # csvwriter.writerow([s2,s3])

    time.sleep(3)

f.close()
