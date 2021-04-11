# print matrix element
arr = [[3, 4, 5, 6], [4, 5, 6, 7, 8]]
for i in arr:
    for j in i:
        print(j)

# cros add
arry = [[3, 4, 5, 6], [4, 5, 6, 7], [3, 4, 5, 6], [4, 5, 6, 7]]
count = 0
for i in range(0, len(arry)):
    count += arry[i][i]
print(count)
