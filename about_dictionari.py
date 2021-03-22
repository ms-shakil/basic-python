mydic={"name":"rohid","age":34,"district":"comilla"}
print(mydic)
print(mydic["name"])
print("name" not in mydic)
print(list(mydic.keys()))
print(list(mydic.values()))
print(mydic.keys())
mydic={"name":"rohid","age":34,"district":"comilla"}
## using loop
# find keys 
for i in mydic.keys():
    print(i)
# find values
for v in mydic.values():
    print(v)
# find key and values
for i in mydic.items():
    print(i)

## string cha count 
data ="Hi my name is payer ahamed . i am a software engineer. Oh i also have Civil engineering degrees. i will got 3 married insaallah"
dic={}

for ch in data:
    dic.setdefault(ch,0)
    dic[ch] = dic[ch]+ 1
print(dic)
print(format(dic))
import pprint
def printF(dic):
    print("The computer will go first.")
    print("{} | {} | {}".format(dic["Top-L"],dic["Top-M"],dic["Top-R"]))
    print("________")
    print("{} | {} | {}".format(dic["Mid-L"],dic["Mid-M"],dic["Mid-R"]))
    print("________")
    print("{} | {} | {}".format(dic["Bot-L"],dic["Bot-M"],dic["Bot-R"]))

data={"Top-L":" ","Top-M":" ","Top-R":" ",
    "Mid-L":" ","Mid-M":" ","Mid-R":" ",
    "Bot-L":" ","Bot-M":" ","Bot-R":" "}
data["Top-L"]="O"
data["Top-M"]="O"
data["Top-R"]="X"
data["Mid-L"]="O"
data["Mid-M"]="X"
data["Mid-R"]="O"
data["Bot-R"]="X"
data["Bot-L"]="X"
data ["Bot-M"]="X"
printF(data)