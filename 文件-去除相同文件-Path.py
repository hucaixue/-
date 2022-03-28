from pathlib import Path
import operator
from filecmp import cmp

src_folder=Path("../MyPractice")
dest_folder=Path("../MyPractice_重复")
if not dest_folder.exists():
    dest_folder.mkdir(parents=True)

file_list=[]
result=list(src_folder.rglob("*"))

for i in result:
    if i.is_file():
        file_list.append(i)

for m in file_list:
    for n in file_list:
        if m!=n and m.exists() and n.exists():
            if cmp(m,n):
                n.replace(dest_folder/n.name)

print("整理完成！")