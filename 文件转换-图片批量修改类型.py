from pathlib import Path
from PIL import Image

basepath=Path("D:\pythonProject\MyPractice\img")
destpath=Path("./目标文件")

if not newpath.exists():
    newpath.mkdir()

jpg_list=[]
for file in basepath.rglob("*.jpg"):
    jpg_list.append(file)

for jpgfile in jpg_list:
    desfile=destpath.joinpath(jpgfile.name).with_suffix(".png")
    Image.open(jpgfile).save(desfile)

print("转换完成！")

