# import requests
# url ="http://dimikcomputing.com"
# res = requests.get(url)
# with open("dimik.html","w")as f:
#     f.write(res.text)

# import os
# import  webbrowser as wb
# with open("dimik.html","w", encoding=res.encoding)as f:
#     f.write(res.text)

# file_path = os.path.realpath("dimik.html")
# print(file_path)    
# wb.open("file://"+file_path)

import requests
import sys

arguments= sys.argv[1]
file_name =sys.argv[2]
r = requests.get(arguments)

with open(file_name,"wb") as f:
    f.write(r.content)