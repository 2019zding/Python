# Create a 2D array that contains days and a list of their
# highest, lowest, and mean temp
# Then
# Cycle through this 2D array to
# Find the highest of all temps and return that day

# Data Type: Days => 0-6, Temps => 0-2
# Row = Day
# Col = Temp
# weather = [[64, 75, 81], [72, 76, 80],...]
# highestTemp = 0
# if weather[i][o] > highestTemp
# highestTemp = weather[i][o]

weather = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [90,14,15], [16,17,18], [19,20,21]]
highestTemp = 0
for i in range(len(weather)):
    for j in range(len(weather[i])):
        if weather[i][j] > highestTemp:
            highestTemp = weather[i][j]
print(highestTemp)
