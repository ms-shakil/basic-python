
with open("./file1.csv","w") as f:
  data=f.write("Hello Banglasdesh \n")

with open ("./file1.csv","a") as f:
  data=f.write("How are you\nKemon bhode korco\n")

with open ("./file1.csv","r") as f:
  f.read()  
  f.seek(0)
  for line in f:
      print(line)
