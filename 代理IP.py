from fake_useragent import UserAgent
import requests

url="https://www.youtube.com/"
headers = {"User-Agent": UserAgent().chrome}
proxies = {
  "http": "http://127.0.0.1:3532",
  "https": "http://127.0.0.1:3532"
}
res=requests.get(url,headers=headers,proxies=proxies)
print(res)
