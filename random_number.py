import random
def Find_randomNumber(value):
    if value == 1:
        return "its one."
    elif value == 2:
        return "its two."
    elif value == 3:
        return "its three."
    elif value == 4:
        return "its four."
    elif value == 5:
        return "its five."

R = random.randint(1,5)
print(Find_randomNumber(R))