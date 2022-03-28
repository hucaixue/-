import os
from tempfile import TemporaryDirectory,TemporaryFile

# with TemporaryFile("w+t") as f:
#     f.write("我是tem文件")
#     f.seek(0)
#     data=f.read()
#     print(data)
#

with TemporaryDirectory() as temdir:
    print("created:",temdir)
    tmp=temdir
    print(os.path.exists(temdir))

print(tmp)
print(os.path.exists(tmp))
