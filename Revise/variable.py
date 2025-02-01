
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

number= 10
str ="Md Sahabuddin Shakil"

name1,name2,name3= "shakil","main","Sr"
x=y=z ="None"
fruits =["apple","banana","mango"]
a,b,c = fruits

str(3) # out put wll be "3"
int(3) # output will be 3
float(3) # output will be  3.0



print(y)
print(type(str))
print(a)

# Global variable

xyz ="Global_variable"

def MyFun():
    xyz = "local variable"

    print(xyz + "this data from local variable.")

print("This Data form Global varable")

