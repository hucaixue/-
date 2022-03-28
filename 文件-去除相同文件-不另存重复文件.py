from pathlib import Path
import operator
from filecmp import cmp
from tqdm import tqdm

src_folder=Path("../MyPractice")

file_list=[]
result=list(src_folder.rglob("*"))

for i in result:
    if i.is_file():
        file_list.append(i)

for m in file_list:
    for n in file_list:
        if m!=n and m.exists() and n.exists():
            if cmp(m,n):
                n.unlink()

print("整理完成！")