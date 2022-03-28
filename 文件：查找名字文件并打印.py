from pathlib import Path

while True:
    folder=input("搜索文件的路径：")
    folder=Path(folder.strip())
    if folder.exists() and folder.is_dir():
        break
    else:
        print("输入路径不存在，请重新输入！")

search=input("输入文件或文件夹的名字：")
result=list(folder.rglob(f"*{search}*"))
print(result)

if not result:
    print(f"在当前的{folder}下未找到{search}相关的文件夹")
else:
    result_folder=[]
    result_file=[]
    for i in result:
        if i.is_dir():
            result_folder.append(i)
    for i in result:
        if i.is_file():
            result_file.append(i)
    if result_folder:
        print(f"查找到包含关键字{search}的文件夹有：")
        for i in result_folder:
            print(i)
    if result_file:
        print(f"查找到包含关键字{search}的文件有：")
        for i in result_file:
            print(i)