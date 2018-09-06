m = [[1,2,3], [4,5,6]]
m[0][1]
# Lets find the value 5 in this array
# nested loops
# outer loop = rows
# inner loop = columns

find = 5
n = [1,2,3,4,5]

for x in n:
    if find == n:
        print(n)

# rows
for o in range(len(m)):
    # o = the first array [[1,2,3], [4,5,6]]
    # o = [1,2,3]
    for i in range(len[o]):
        # add seq search
        if m[o][i] == find:
            print(m[o][i])
            print('Hurray!')
