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
data ="Hi my name is payer ahamed . i am  software and civil engineer. i will got 3 married insaallah"
dic={}

for ch in data:
    dic.setdefault(ch,0)
    dic[ch] = dic[ch]+ 1
print(dic)
print(format(dic))