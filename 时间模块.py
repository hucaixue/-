import os
from pathlib import Path
import glob
import datetime
format="%Y年%m月%d日 %H:%M:%S"
basepath=Path("D:/pythonProject/")
for file in basepath.rglob("*"):
    info=file.stat().st_mtime
    dt=datetime.datetime.fromtimestamp(int(info))
    print(dt.strftime(format))