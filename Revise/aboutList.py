my_list=["laptop","keyboard","mouse","table","monitor","desktop"]
list2 =["None","None","None"]
my_list[3]="lol"

my_list.append("Books")
my_list.insert(1,"Mobile") # insert specified index

my_list.extend(list2) # append element from another array

my_list.remove("table")
my_list.pop(3)
my_list.pop() # remove last element

# sort list
my_list.sort()
my_list.sort( reverse=True)

print(len(my_list))

for x in my_list:
    print(x)

for i in range(len(my_list)):
    print(my_list[1])

