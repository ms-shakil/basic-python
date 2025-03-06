# lambda function has no name, its singal line code
x= (lambda a,b:a*b)(2,4)

def my_Fun(N):
    return (lambda a:a*a+a)(N)

print(x )
print(my_Fun(20))