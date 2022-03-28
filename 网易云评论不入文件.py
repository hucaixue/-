from Cryptodome.Cipher import AES
from base64 import b64encode
import requests
import json
import time

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "hvoLCayV6TJ6tjRk"

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

def get_encSecKey():
    return "b264e3b860b271c7e371383393aef531a67189daf3ecf3d0cd0082185f87908151858011cda30041030cf6f39cfee7f439591306fd12aaf1dee92707319259ace2a634249c8c15c41eea20c586d2971857f10151755889a68084e353bd56775a443041a018c52c375f32423901d07176073fe431022c7b37761f3d8413902a20"

def get_params(data):
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second

def to_16(data):
    pad = 16-len(data)%16
    data +=chr(pad) * pad
    return data

def enc_params(data,key): #加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC) #创建加密器
    bs = aes.encrypt(data.encode('utf-8')) #加密
    return str(b64encode(bs),"utf-8") #转化成字符串

if __name__ == '__main__':
    page = int(input('请输入需要爬取的页数：'))
    print('开始爬虫！！！')
    for j in range(1,page+1):
        page_num = str(j*20)
        data = {
            "csrf_token": "56d425a5c2377915165060f10782c21b",
            "cursor": "-1",
            "offset": "0",
            "orderType": "1",
            "pageNo": "1",
            "pageSize": page_num,
            "rid": "R_SO_4_1899989255",
            "threadId": "R_SO_4_1899989255"
        }

        response = requests.post(url,data={"params":get_params(json.dumps(data)),"encSecKey":get_encSecKey()},headers=headers)
        result = json.loads(response.content.decode('utf-8'))

        #hotComments
        for hot in range(len(result['data']['hotComments'])):
            print('hotComments' + ' ')
            print('昵称：' + result['data']['hotComments'][hot]['user']['nickname'] + '\n')
            print('评论：' + result['data']['hotComments'][hot]['content'] + '\n')

            if result['data']['hotComments'][hot]['user']['vipRights'] == None:
                print('vip:yes' + '\n')
            else:
                print('vip:no' + '\n')
            print('点赞数' + str(result['data']['hotComments'][hot]['likedCount']) + '\n')
            print('-------------------------------------' + '\n')

        #comments
        # for r in range(20):
        #     print('comments')
        #     print('昵称：'+result['data']['comments'][r]['user']['nickname']+'\n')
        #     print('评论：'+result['data']['comments'][r]['content']+'\n')
        #
        #     if result['data']['comments'][r]['user']['vipRights'] == None:
        #         print('vip:yes'+'\n')
        #     else:
        #         print('vip:no'+'\n')
        #     print('点赞数'+str(result['data']['comments'][r]['likedCount'])+'\n')
        #     print('-------------------------------------'+'\n')
    print('爬取完毕！！！')