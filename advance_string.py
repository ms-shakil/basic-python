name ="Hi's name is payer"
print(name.upper())
print(name.lower())
print("name " in name)
print(name, "\n",name)
print(name.islower())
print(name.isupper()) # isalpha isdecimal,is number, startwith ,endwith  return True and false
# join method
nm =["shakil","mainuddin","payer","sajjad"]
print("-".join(nm)) # join method join list type stirng  and return a stirng
## split
myname ="my name is payer. i am software engineer."
print(myname.split())

## rjust method
print("hello".rjust(20,"*"))

## leftjust
print("payer".ljust(30,"_"))

## strip 
print("      xxx     ".strip()) # strip method remove whoile space

## replace mathodes
eng = "i am a software engineer"
print(eng.replace("software","civil"))

## string format
print("i my name is {2}. I am a {1} enginner. i also have {0} engineering degrees".format("civil","software","payer"))