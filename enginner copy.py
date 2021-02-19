class Engineer:
  def __init__(self,id,name,age,dist):
    self.id=id
    self.name=name
    self.age=age
    self.dist=dist

  def __repr__(self):
    return "{},{},{},{}".format(self.id, self.name, self.age, self.dist)


# # import csv
# list_of_enginner=[]    
# count=int(input("Enter an number:"))
# for i in range(count):
#   id=input("Enter an id{}:".format(i))
#   name=input("Enter an name{}:".format(i))
#   age=input("Enter an age{}:".format(i))
#   dist=input("Enter an dist{}:".format(i))
#   with open("./enginner-data.csv","a",newline="")as f:
#     # writer= csv.writer(f)
#     # writer.writerow(["id","name","age","dist"])
#     f.write("{},{},{},{}\n".format(id,name,age,dist))
    

#   with open("./enginner-data.csv","r")as f:
#     list_of_enginner.append(Enginners(id,name,age,dist))

# print(list_of_enginner)


list_of_engineers = [
  "ID,Name,Age,District"
]

count = int(input("Enter number of engineers: "))

for i in range(count):
  print("#### {}".format(i+1))
  id = input("Enter an ID: ")
  name = input("Enter a Name: ")
  age = input("Enter an Age: ")
  dist = input("Enter a district: ")
  eng = Engineer(id, name, age, dist)
  list_of_engineers.append(eng)

with open('./list_of_engineers.csv', 'w') as f1:
  for eng in list_of_engineers:
    f1.write("{}\n".format(eng))
print(list_of_engineers)