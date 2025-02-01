"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


# Number type
x =2 # int
y = 3.5 # float
z = 3j # complex number

# Casting number
z= int(y)
y =float("4")
# print(z,y)



# String Data type
name ="Shakl"
UNI ="""sdfsdfffffffffffffsdfasdf
asfsdssdffasd shakil ffffff  """

print(name[1])
print(len(name))
# for x in name:
#     print(x + ' ')

if "shakil" in UNI:
    print("YES")

print("main" not in UNI)

uiu = "united international university"

print(uiu[3:10])
print(uiu.upper().split(' '))


# Tuple , allwo dublicate vlaue , but cant change data . thats why its covert in list 

colours =("white","black","yellow")
colour =list(colours)
colour[1] = "Blue"
colours = tuple(colour)
print(colours)


# Set  , Duplicates are not allow

data ={"apple","orange","banana","apple"}
print(data)