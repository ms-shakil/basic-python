import random
print("Hello. What,s your name:")
name = input(":")
print("Well "+ name+"I am taking of a number between 1 and 20.")
secretnumber = random.randint(1,20)
for i in range(1,6):
    print("Take guess number:")
    guess = int(input(":"))
    if guess < secretnumber:
        print("your guess is too low")
    elif guess > secretnumber:
        print("Your guess is too High") 
    else:
        break

if guess == secretnumber:
    print("Wow you win")
else:
    print("Wow no you lose.")               