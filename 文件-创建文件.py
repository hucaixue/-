import os
from pathlib import Path

basepath=Path("我的文件/2018/10/10")
basepath.mkdir(parents=True,exist_ok=True)
# if basepath.exists():
#     basepath.mkdir(parents=True)
