import os
import shutil
import zipfile
import datetime

path = input("请输入一个地址：")
os.chdir(path)
newlist = []
for dirpath, dirname, files in os.walk("./"):
    for file in os.scandir(dirpath):
        if not file.is_dir():
            file_datetime = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            datetime_delta = datetime.datetime.now() - file_datetime
            if datetime_delta.days >= 2 and file.name.endswith(".txt"):
                newname = f"{file_datetime.strftime('%Y-%m-%d')}-{file.name}"
                os.rename(dirpath + "/" + file.name, newname)
                newlist.append(newname)

if not os.path.exists("长期未使用"):
    os.mkdir("长期未使用")
for f in newlist:
    shutil.move(f, "长期未使用/")

os.chdir("长期未使用/")
ziplist = os.listdir("./")
zipfilename = f"{datetime.datetime.now().strftime('%Y-%m-%d')}_长期未使用.zip"
with zipfile.ZipFile(zipfilename, "w") as zip:
    for file2 in ziplist:
        zip.write(file2)