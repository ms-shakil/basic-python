
data = open("data.txt","a")

data.write("hello")
data.close()

data = open("data.txt","r")
print(data.read())