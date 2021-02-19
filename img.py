import requests
import os
import webbrowser as wb
img_url ="https://goo.gl/JxKtPw"
r = requests.get(img_url)
with open("pybook1.png","wb")as f:
    f.write(r.content)

p = os.path.realpath("pybook.png")   
print(p)
wb.open("file://"+p)