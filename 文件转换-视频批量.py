import os
from pathlib import Path

ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"
source_path = Path("D:/pythonProject/AAA实用工具/")
des_path = Path("./目标文件/")

if not des_path.exists():
    des_path.mkdir()

source_list=[]
for file in source_path.rglob("*.mp4"):
    source_list.append(file)

for source_file in source_list:
    print("正在转换:"+source_file.name)
    new_name = source_file.name[:-4]
    os.system(f"{ffmpeg} -i {source_file} {des_path}{new_name}.mp3")

print("转换完毕!")