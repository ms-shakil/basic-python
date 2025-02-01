person ={
    "name":"Shakil",
     "age":32,
     "university":"UIU"
}

person1 =dict(name="main", age =26, university ="Daffodil") 

# access
person["age"]=23
person["district"]="Comilla"
person.pop("university")

print(person.keys())
print(person.values())
print(person["name"])


for x in person:
    print(x)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for x,y in person.items():
    print(x, y)