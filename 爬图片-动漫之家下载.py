import os
import requests
import os
import requests
import time

# 进度条模块
def progressbar(url,path):
    if not os.path.exists(path):   # 看是否有该文件夹，没有则创建文件夹
         os.mkdir(path)
    start = time.time() #下载开始时间
    response = requests.get(url, stream=True)
    size = 0    #初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小
    try:
        if response.status_code == 200:   #判断是否响应成功
            print('Start download,[File size]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))   #开始下载，显示下载文件大小
            filepath = path+'\Pikachu.jpg'  #设置图片name，注：必须加上扩展名
            with open(filepath,'wb') as file:   #显示进度条
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    size +=len(data)
                    print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
        end = time.time()   #下载结束时间
        print('Download completed!,times: %.2f秒' % (end - start))  #输出下载用时时间
    except:
        print('Error!')

def main():
    #下载皮卡丘图片
    url = 'https://img.moegirl.org/common/thumb/e/ed/%E7%9A%AE%E5%8D%A1%E4%B8%98%E4%B9%8B%E6%AD%8C.jpg/1200px-%E7%9A%AE%E5%8D%A1%E4%B8%98%E4%B9%8B%E6%AD%8C.jpg'
    path = r'E:\123'  # 设置下载到本地的地址
    progressbar(url,path)

if __name__ == '__main__':
    main()


'''
连载是[0]
不连载是[1]

|img|15046034344049|hidden|67451|var|pages|id|15046034347175|15046034353307|1056|chapter_order|
15046034393941|sum_pages|chapter_name|15046034365671|15046034373961'.split

https://images.dmzj.com/img/chapterpic/485/78994/15046034344049.jpg      1      
https://images.dmzj.com/img/chapterpic/485/78994/15046034347175.jpg      2
https://images.dmzj.com/img/chapterpic/485/78994/15046034353307.jpg      3
https://images.dmzj.com/img/chapterpic/485/78994/15046034365671.jpg      5
https://images.dmzj.com/img/chapterpic/485/78994/15046034373961.jpg      6
https://images.dmzj.com/img/chapterpic/485/78994/15046034393941.jpg      4

'''