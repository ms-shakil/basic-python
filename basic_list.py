arr =["main","fahad","sajjad","asif","payer"]
# print main arr
print(arr)
# print arr singal element with index number
print(arr[0])
# print element by negetive  index number
print(arr[-1])
# get array lenth
print(len(arr))
# using loop on arry
for i in range(len(arr)):
    print(arr[i])
for i in arr:
    print(i)    
##################################################

lst =["main","fahad","sajjad","asif","payer"]
my_arr = [4,6,3,6,7,5,35]
# find element position
print(lst.index("payer"))
# add new element on array
lst.append("shakil")
print(lst)
# remove element
lst.remove("payer")
print(lst)
# sort arr
lst.sort()
my_arr.sort(reverse = True)
print(lst)
print(my_arr)
###########################################
my_lst =["main","fahad","sajjad","asif","payer","Main","Payer","Fahad"]
# sort lower to upder case
my_lst.sort(key=str.lower)
print(my_lst)
# arr revERSE
my_lst.reverse()
print(my_lst)

#########################################
# arry slice
my_ar =[3,4,6,7,4,6,7,4]
print(my_ar[3:6])
print(my_ar[:4])
print(my_ar[5:])
####################################
#Sequence Data Types
Name ="Mainuddin"
print(Name[0])
print("k" in Name)
print("d" in Name)
print("M" not in Name)
for i in Name:
    print("***"+i+"***")

eng ="payer is not engineer"
print(eng[0:5]+" is the"+eng[12:21])
###############################################

# tuple
my_tup =("shakil","mainudin","fahad")
print(my_tup)
for i in my_tup:
    print(i)
# tuple tw list
print(list(my_tup))    

# referencese
num = 10
snum = num
num = 20
print(snum)
print(num)

# id function
print(id("shakil"))
###################################
 # 2D array
my_2D =[[3,4,5],[366,645,64,],["shakil","main"]]
print(my_2D[0])
print(my_2D[1][0])
####################
# loop
lst = list(range(1,40,2))
print(lst)

# list element define with variable
lst=["shakil","main","fahad"]
a,b,c = lst
print(a)
print(b)
print(c)

# element insert on list
lst=["shakil","main","fahad"]
lst.insert(2,"payer")
print(lst)
 
clst=["shakil","main","fahad"]
arr = clst
arr[0] = "payer"
print(clst) #The clst variable refers to the same list.
print(arr)

### aray copy
import copy
name =["shakil","mainuddin","payer","fahad"]
eng = copy.copy(name) # eng is a different list with different identity.
eng[2]="sajjad"
print(name)
print(eng)