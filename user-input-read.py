# a=input("Enter on string:")
# b=input("Enter on string:")
# c=input("Enter on string")
# with open("./file1.csv","a") as f:
#   f.writelines('{}\n{}\n{}\n'.format(a,b,c))
# with open("./file1.csv","r") as f:
#   f.read()
#   f.seek(0) 
#   for lines in f:
#     print(lines)

#Multipole string Writing in file....
list_of_data=[]
count=int(input("Enter an number:"))
for i in range(count):
  id=input("Enter id{0}:".format(i))
  name=input("Enter name:")
  age=int(input("Enter an age:"))
  with open("./student-data.csv","w") as f:
    f.writelines(",{},,{},,{}\n".format(id,name,age))

with open("./student-data.csv","r") as f:
  f.read()
  f.seek(0) 
  list_of_data.append(f)


  for lines in f:
    print(lines) 


