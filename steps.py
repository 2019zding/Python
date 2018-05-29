# You have two stacks which you will use to create a third
# You will compare stack1[x] to stack2[x] and populate the third
# You will compare last1[x] to last2[x] and populate the third
# Stack with which ever iterators word length is even
# If both are even, then you would add just one case of the word
# Yes you can only use while loops
arr1 = ['woof', 'meow', 'bork', 'craww', 'tricky']
arr2 = ['borf', 'meow', 'growlll', 'chirps', 'tricky']
newArr = []

# Big O is n^2, that means nested loop
# outer count
i = 0
# inner count
j = 0

while i < len(arr1):
    # If index value is even and index value is not in my new array
    if len(arr1[i]) % 2 == 0 and arr1[i] not in newArr:
        #add it to new array
        newArr.append(arr1[i])
        print(newArr)
        #counting
# Don't add repeats
    i = i+1
    # inner loop
    while j < len(arr2):
        if len(arr2[j]) % 2 == 0 and arr2[j] not in newArr:
            newArr.append(arr2[j])
        j = j + 1
print(newArr)
