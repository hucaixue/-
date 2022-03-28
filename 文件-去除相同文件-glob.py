import os
import glob
import operator

dirpath="../MyPractice/"
file_list=[]
for i in glob.glob(dirpath+"**/*",recursive=True):
    if os.path.isfile(i):
        file_list.append(i)

for m in file_list:
    for n in file_list:
        if m!=n and os.path.exists(m) and os.path.exists(m):
            if operator.is_not(m,n):
                os.remove(n)

print("over!")

