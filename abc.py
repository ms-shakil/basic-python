import requests
import sys

arguments= sys.argv[1]
file_name =sys.argv[2]
r = requests.get(arguments)

with open(file_name,"wb") as f:
    f.write(r.content)