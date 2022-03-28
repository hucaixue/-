import os
import zipfile

dirlist=os.listdir()
# with zipfile.ZipFile("myzipfile.zip",mode="w") as zip:
#     for file in dirlist:
#         if file.endswith(".py"):
#             zip.write(file)
# with zipfile.ZipFile("myzipfile.zip",mode="r") as zip:
#     print(zip.namelist())
# with zipfile.ZipFile("myzipfile.zip","r") as zip:
#     zip.extract("动态加盐.py","./")

with zipfile.ZipFile("myzipfile.zip","r") as zip:
    zip.extractall("02")