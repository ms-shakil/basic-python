import json
JSON_FILE ="./lebar.json"

list_of_engineers =[]

with open(JSON_FILE,"r") as fd:
    data_f = json.load(fd)
    list_of_engineers = data_f

def find_data(list,id):
    found = False
    for data in list:
        if data["id"] == id:
            found = True
            break
    return found

count= int(input("How many data do you want insert:"))
i= 0
while i < count:
    engineer={
    "id":input("Enter an id:"),
    "name":input("Enter name:"),
    "age":int(input("Enter age:")),
    "district":input("Enter district:")
    }
    if find_data(list_of_engineers, engineer["id"]):
        print("this data already exist")
    else:
        list_of_engineers.append(engineer)
        i+=1

with open(JSON_FILE,"w") as fd:
    json.dump(list_of_engineers,fd)  


