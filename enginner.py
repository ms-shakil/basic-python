class Enginners:

  def __init__(self,id,name,age,dist):
    self.id=id
    self.name=name
    self.age=age
    self.dist=dist
  def __repr__(self):
    return """
    id:{0}
    name:{1}
    age:{2}
    dist:{3}
    """.format(self.id,self.name,self.age,self.dist)


# import csv
list_of_enginner=[]    
count=int(input("Enter an number:"))
for i in range(count):
  id=input("Enter an id{}:".format(i))
  name=input("Enter an name{}:".format(i))
  age=input("Enter an age{}:".format(i))
  dist=input("Enter an dist{}:".format(i))
  with open("./enginner-data.csv","a",newline="")as f:
    # writer= csv.writer(f)
    # writer.writerow(["id","name","age","dist"])
    f.write("{},{},{},{}\n".format(id,name,age,dist))
    

  with open("./enginner-data.csv","r")as f:
    list_of_enginner.append(Enginners(id,name,age,dist))

print(list_of_enginner)


