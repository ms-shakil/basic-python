import json

JESON_FILE =  "./studnt_data_copy.json"

dic_student={
  "Name":"Student data",
  "Total":0,
  "District":[],
  "Students":[]

}

with open(JESON_FILE,"r") as data_file:
  data=json.load(data_file)
  
  try:
    dic_student["Name"] = data["Name"]
    dic_student["Total"] = data["Total"]
    dic_student["District"] = data["District"]
    dic_student["Students"] = data["Students"]

  except Exception:
    print("Data no found") 

print("There are{} student in the file".format(dic_student["Total"]))  


count = int(input("Enter number of students:"))

def find_information(list,id):
  found = False
  for data in list:
    if data["id"] == id:
       found = True
       break
  return found

i=0
while i < count:
  print("Enter data of student#{}".format(i+1))    
  student={
    "id":input("ID:"),
    "name":input("Name:"),
    "age":input("Age:"),
    "district":input("District:")
  }
  if find_information(dic_student["Students"],student["id"]) == True:
    print("This studnet is already exists")
  else:
    dic_student["Students"].append([student])  
    i+=1

dic_student["Total"] = len(dic_student["Students"])    

dic_data={}
dic_list=[]

for student in dic_student["Students"]:
  dist= student["district"]
  for dist in dic_data:
    dic_data[dist]+=1
  else:
    dic_data[dist]=1

for name,count in dic_data.items():
  dic_list.append(
    {
      "name":name,
      "count":count
    }
  )      

dic_student["District"]=dic_list

with open(JESON_FILE,"w") as data_file:
  json.dump(dic_student,data_file)

      

 
