lines=["this is first line.","this is second line.","this is third line."]
with open("file.text","w")as ff:
    for i in lines:
        ff.write(i+"\n")

with open("file.text","r") as fd:
  
    print(fd.read())
