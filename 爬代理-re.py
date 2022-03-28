import re
import requests
from fake_useragent import UserAgent

url="https://www.kuaidaili.com/free/"
headers={"User-Agent":UserAgent().chrome}
page=requests.get(url,headers=headers).text
object=re.compile(r"<td data-title='IP'>(?P<IPadr>.*?)</td>.*?'PORT'>(?P<PORTadr>.*?)</td>"
                  r".*?'类型'>(?P<type>.*?)</td>.*?'位置'>(?P<place>.*?)</td>.*?'响应速度'>(?P<speed>.*?)"
                  r"</td>.*?'最后验证时间'>(?P<time>.*?)</td>",re.S)
result=object.finditer(page)
for it in result:
    print(it.group("IPadr"))
    print(it.group("PORT"))
    # dic = it.groupdict()
    # print(dic)
