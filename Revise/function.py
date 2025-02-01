
# def FizzBuzz():
#     num = int(input("Enter a number:"))
#     for i in range(0,num):
#         if i%5==0 and i%3==0 :
#             print("FizzBuzz")
#         elif  i%5==0:
#             print("Fizz")
#         elif i%3==0:
#             print("Buzz")
#         else:
#             print("None")     


# FizzBuzz()


def Recurson(number):
    if number> 0:
      
        number-=1
        print(number)
        Recurson(number) 
        print(number)   

Recurson(10)
