import pyinputplus as pyip
this is simple input validation
while True:
     print("Enter your age:")
      age = input()
       try:
            age = int(age)
        except:
            print("please use numeric digits.")
            continue
        if age < 1:
            print("please entera positive number.")
            continue
        print("your age is", age)
        break
print("enter the Email")
value = pyip.inputEmail()
print(value)
print("Eneter the Datetime")
value = pyip.inputDate()
print(value)
print("Eneter the password")
value = pyip.inputPassword()
print(value)

min max greater than and less than  keyword arguments
value = pyip.inputNum("Enter the number", min=4, max=19)
print(value)
value = pyip.inputNum("Enter the number:", min=5, lessThan=7)
print(value)
# we can aslo use blank ,limit timeout ,default, regexes and blockregexes keyword arguments
