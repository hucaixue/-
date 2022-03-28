import os
import shutil
import datetime
import glob

path="D:\pythonProject\AAA实用工具"
if not os.path.exists("最新图片"):
    os.mkdir("最新图片")

for dirpath,dirname,files in os.walk("./"):
    for file in os.scandir(dirpath):
        if file.name.endswith(".jpg"):
            tm=datetime.datetime.fromtimestamp(file.stat().st_mtime)
            newfile=str(tm.year)+"_"+str(tm.month)+"_"+str(tm.day)+"_"+file.name
            os.rename(dirpath+"/"+file.name,newfile)

jpglist=glob.glob("*.jpg")
for name in jpglist:
    shutil.move(name,"最新图片/")