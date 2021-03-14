x=["shakil","mainuddin","fahad","asif","sajjad"]
for i in x:
    print(i)
    if i=="fahad":
        break
        
i=1
while i <34:
    print(i)
    i+=2

dictonary

dic={"name":"shakil","age":23,"class":13,"district":"comilla"}
print(len(dic))



x=10
y=1
while x > 0:
    star="*"*y
    space=" "*x
    print(space+star)
    x-= 1
    y+=2

x=19
y=1
while x > 0:
    star="*"*x
    space=" "*y
    print(space+star)
    x-= 2
    y+=1


x=10
y=1
while x > 0:
    star="*"*y
    space=" -"*x
    print(space+star)
    x-= 1
    y+=2


year=int(input("Enter an year:"))

if year % 4 == 0 :
    print("its leap yerar")
else:
    print("it's not leap year")    



# function

def fnc(x, li):
    print(type(x))
    print(type(li))
    x=300
    li.append(6)
    return x
a=23
my_li=[3,4,5,6,3]    
print(my_li)
y=fnc(a,my_li)

print(y)
print(a)
print(my_li)



def sl(x ,y):
    x=2
    y=0
    return x ,y

a=45
my=[2,3,4,5,]
y=sl(a,my)
print(y)    


def sm(n1,n2):
    sum=5+n2
    return sum

k=3
v=sm(k,33)
print(v)



# oop


class shakil:
    side=6
    
    def __init__(self,x):
       self.side=x     

    def area(self):
        return self.side * self.side
sq=shakil(4)
print(shakil.side)
print(shakil.area(sq)) 
print(sq.area())           


class rect:
    def __init__(self):
        print("insite of rect")

    def area(self,x,y):
        return x*y    

class square(rect):
    def __init__(self):
        print("insite of square")        
r=rect()
sq=square()
sl=sq.area(5,5)
print(sl)
a = [4,56,6,7,8,3,0,]

print(a.append("shakil"))


#squre root 

var = 100**(1/2)
print(var)
num = 5
for i in range(1,num):
    for j in range(1,i):
        print(j, end ='')

name =""
while name != "your name":
    print("Enter your name:")
    name = input()
print("Thank You")    
while name =="":
    print("yes")
    name ="shakil"
print("NO")    

while True:
    print("Enter your name:")
    name  = input()
    if name =="Shakil":
        break
arr =[6,31415926535897932384626433832795,1,3,10,3,5]
for i in range(len(arr)):
    for j in range(i ,len(arr)):
        if arr[i]> arr[j]:
            T = arr[i]
            arr[i]= arr[j]
            arr[j] = T
print(arr)            
n = int(input())

unsorted = []

for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)
print(unsorted)    

st ="this is a string"
sl =st.split(" ")
print("-".join(sl))
s1="js"
s2 ="pythons"
value = False
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            value = True
if value == True:
    print("YES")
else:
    print("NO")  

Time  =list("12:23:35AM")

TT = Time[-2]
if TT =="P":
    Hu1 =Time[0]
    Hu2 = Time[1]
    Hu = int(Hu1+Hu2)
    if Hu < 12:
        L = str(12 +Hu)
        if len(L)==1:
            Time [0]="0"
            Time[1] =L[0]
        elif len(L) == 2:
            Time[0]=L[0]
            Time[1]=L[1]         
elif TT =="A":
    Hu1 = Time[0]
    Hu2  = Time[1]
    Hu = int(Hu1+Hu2)
    if Hu < 12:
        Hu = str(Hu)
        if len(Hu)==1:
            Time[0]="0"
            Time[1]=Hu[1]
        else:
            Time[0]=Hu[0]    
            Time[0]=Hu[1]       
    elif Hu == 12:
        Time[0] ="0"
        Time[1] ="0"   
res = "".join(Time[0:8])
print(res)
s ="11:23:33:AM"
s =list(s)
obj ={
     "01":"13",
     "02":"14",
     "03":"15",
     "04":"16",
    "05":"17",
    "06":"18",
    "07":"19",
    "08":"20",
    "09":"21",
    "10":"22",
    "11":"23",
    "12":"12"
}

if s[-2]=="P":
    H1=s[0]
    H2 =s[1]
    H =H1+H2
    T =obj[H]
    s[0]=T[0]
    s[1]=T[1]
if s[-2]=="A":
    H1=s[0]
    H2 =s[1]
    H =H1+H2

    if H =="12":
       s[0]="0"
       s[1]="0"    
res ="".join(s[0:8])
print(res)
