import json
JSONE_FILE ="./data_hand.json"

data_file ={
    "name":"student data",
    "total":0,
    "district":[],
    "student":[]
}

with open(JSONE_FILE,"r") as fd:
    data = json.load(fd)

def data_find(list,id):
    found = False
    for dat in list:
        if dat["id"] == id:
            found = True
            break
    return found
print("There are {} students in this file".format(data_file["total"]))
count = int(input("How many student data do you want insert:"))

j = 0
while j < count:

    print("Enter data of stuendent#{}".format(j+1))

    students ={
        "id":input("ID:"),
        "name":input("Name:"),
        "age":int(input("Age:")),
        "district":input("District:")
    }
    if data_find(data_file["student"],students["id"]):
        print("This id already exist:")
    else:
        data_file["student"].append(students)
        j+=1    
data_file["total"] = len(data_file["student"])

data_dic ={}
data_list =[]

for students in data_file["student"]:
    data_f =students["district"]

    if data_f in data_dic:
        data_dic[data_f]+=1
    else:
        data_dic[data_f]=1    

for nam, cont in data_dic.items():
    data_list.append({
        "name":nam,
        "conunt_data":cont
    })

data_file["district"]=data_list


with open(JSONE_FILE,"w") as fd:
    json.dump(data_file,fd)       