# x argument take  multiple arguments
# def function(*data):
#    print(data)


#function(30, 30, 53, "shakil", "habujabi")

# xx argument

# xx arg take key value data


# def fun(**data):
#    print(data)


#fun(id=3435, name="shakil", age=22)

x = 2
y = 2
z = 2
n = 2
res = [[i, j, k]for i in range(x+1)for j in range(y+1)
       for k in range(z+1)if i+j+k != n]
print(res)
