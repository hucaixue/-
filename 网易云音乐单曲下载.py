import requests

download_url = 'https://music.163.com/song/media/outer/url?id={}'

headers = {
    'Referer': 'https://music.163.com/search/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

url = input('请输入音乐链接：')
music_id = url.split('=')[1]

response = requests.get(download_url.format(music_id), headers=headers)

with open('1.mp3', 'wb') as file:
    file.write(response.content)
    print('<下载成功>')
