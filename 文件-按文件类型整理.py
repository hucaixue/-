import os
import shutil
import glob

src_path="./"
new_path="./分类文件夹"
if not os.path.exists(new_path):
    os.mkdir(new_path)
file_num=0
dir_num=0
for file in glob.glob(f"{src_path}/**/*",recursive=True):
    if os.path.isfile(file):
        filename=os.path.basename(file)
        if "." in filename:
            suffix=filename.split(".")[-1]
        else:
            suffix="others"
        if not os.path.exists(f"{new_path}/{suffix}"):
            os.mkdir(f"{new_path}/{suffix}")
            dir_num+=1
        shutil.copy(file,f"{new_path}/{suffix}")
        file_num+=1

print(f"整理完成！有{file_num}个文件，{dir_num}个文件夹！")




