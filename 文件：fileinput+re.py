import fileinput
import re

pattern='[010|021]-\d{8}'
for line in fileinput.input("1.txt"):
    if re.search(pattern,line):
        print("="*50)
        print("Filename:"+fileinput.filename()+"| Line Number:"+str(fileinput.filelineno())+"|"+line)

