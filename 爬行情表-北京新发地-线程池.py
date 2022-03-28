import json
import requests
from concurrent.futures import ThreadPoolExecutor

mainurl = "http://www.xinfadi.com.cn/priceDetail.html"
turl = mainurl.replace("priceDetail", "getPriceData")
# "http://www.xinfadi.com.cn/getPriceData.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4929.5 Mobile Safari/537.36"}

def download_one_page(data):
    res = requests.post(turl, headers=headers, data=data)
    dic = res.json()
    lst = dic["list"]
    for dic in lst:
        prodname = dic["prodName"].strip()
        prodnat = dic["prodCat"].strip()
        lowprice = dic["lowPrice"].strip().replace(" ", "")
        highprice = dic["highPrice"].strip().replace(" ", "")
        avgprice = dic["avgPrice"].strip().replace(" ", "")
        place = dic["place"].strip().replace(" ", "")
        unitinfo = dic["unitInfo"].strip()
        time = dic["pubDate"].strip()

        print(time, prodnat, prodname, lowprice, highprice, avgprice, unitinfo, place)


if __name__=="__main__":
    with ThreadPoolExecutor(50) as t:
        for i in range(3,10):
            data={
            "limit": "20",
            "current": f"{i}",
            "pubDateStartTime": "",
            "pubDateEndTime": "",
            "prodPcatid": "",
            "prodCatid": "",
            "prodName": "",
            "Referer": mainurl
        }
            t.submit(download_one_page, data)
        print("全部完成！")