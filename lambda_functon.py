# normal function
def fun(a, b):
    print(a*a + 2*a*b + b*b)


fun(5, 5)

# lambda function .......lambda function work for singal line code.........it does't have name

result = (lambda a, b: a*a + 2*a*b + b*b)(5, 5)
print(result)
