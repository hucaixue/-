# import fileinput
# for file in fileinput.input('文稿.txt',encoding="utf-8"):
#     print(fileinput.filename(),'|','Line Number:',fileinput.lineno(),'|: ',file)

# import fileinput
# for line in fileinput.input(files='1.txt',backup='.bak',inplace=1):
#     print(line.rstrip().replace('010','111'))

import fileinput
import glob

for line in fileinput.input(glob.glob("test*.txt"),inplace=False):
    if fileinput.isfirstline():
        print("_"*20,"reading%s..."%fileinput.filename(),"_"*20)
    print(str(fileinput.lineno()) + ': ' + line.upper())

