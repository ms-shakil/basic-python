arr = [2, 3, 4, 5, 6, 7, 8]
result = [x*x for x in arr]
print(result)

result = [x for x in arr if x % 2 == 0 or x % 3 == 0]
print(result)
