class Student:
    name=""
    age=""
    def setValue(self, name,age):
        self.name =name
        self.age =age
    def display(self):
        print(f"Name={st1.name} , Age={st1.age}") 


st1 = Student()
# st1.name ="Shakil"   #  we use  that when  constractor or set value we don't use
# st1.age =22
st1.setValue("name","32")
st1.display()   


# constractur


class Car:

    def __init__(self, brand, colour): # constractor use to set value
        self.brand =brand
        self.colour= colour

    def display(self):
        print(f"Brand Name ={self.brand} \n Colour ={self.colour}")


car1 = Car("BMW","Red")

car1.display()



# inheritance
# parent class, superclass, base class
# child class , subclass,derived class
class Phone:
    def call(self):
        print("You can call")

    def message(self):
        print("You can messages")    
  
class Samsung(Phone):
    def take_Photo(self):
        print("You can take photo")
    

P=Samsung()
P.call()
P.message()
P.take_Photo()