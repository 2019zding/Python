# Binary binarySearch
# Takes in an array, and a number to look for
def binarySearch(arr, n, lowerHalf=0, upperHalf=None):
    # find middle of array
    mid = arr[len(arr)//2]

    if n == arr[mid]:
        return mid
    elif  n < arr[mid]:
        upperHalf = mid - 1
        return upperHalf
    elif n > arr[mid]:
        lowerHalf = mid + 1
        return lowerHalf
    else:
        print('Error')

    # debug make sure it is the middle of an array

    # TO DO:
    # First, what if the search number isn't in the array?
    # Second, what if the number is found?
    # Third, conditional for the lower and upper half based on our find input


arr = [1,2,3,4,5]
binarySearch(arr, 5)
