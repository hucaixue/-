from Cryptodome.Cipher import AES
from base64 import b64encode
import requests
import json
import time

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "0hyFaCNAVzOIdoht"

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

def get_encSecKey():
    return "4022359ea3110bcd034e0160c3b89e5e172fd0110a3cf765d9f366d9fd09840a1f4a4705ac43719fdb8bfeb44d3b92334733061ad10942131184a4dfba0ac9d2cf867b8b6236523c1ca5f44c0d2d82c1c2665a3137a9241c7373539c1aa8e5e9bb9d33dafc764b5d76c2ab34fc94df85e27a934c8a603fa713f2cf38c2b7bbae"

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
    fp = open('./网易云评论.txt', 'w', encoding='utf-8')
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
            fp.write('hotComments' + ' ')
            fp.write('昵称：' + result['data']['hotComments'][hot]['user']['nickname'] + '\n')
            fp.write('评论：' + result['data']['hotComments'][hot]['content'] + '\n')

            if result['data']['hotComments'][hot]['user']['vipRights'] == None:
                fp.write('vip:yes' + '\n')
            else:
                fp.write('vip:no' + '\n')
            fp.write('点赞数' + str(result['data']['hotComments'][hot]['likedCount']) + '\n')
            fp.write('-------------------------------------' + '\n')

        #comments
        for r in range(20):
            fp.write('comments')
            fp.write('昵称：'+result['data']['comments'][r]['user']['nickname']+'\n')
            fp.write('评论：'+result['data']['comments'][r]['content']+'\n')

            if result['data']['comments'][r]['user']['vipRights'] == None:
                fp.write('vip:yes'+'\n')
            else:
                fp.write('vip:no'+'\n')
            fp.write('点赞数'+str(result['data']['comments'][r]['likedCount'])+'\n')
            fp.write('-------------------------------------'+'\n')
    print('爬取完毕！！！')



