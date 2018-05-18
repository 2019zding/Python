def reverseArray(arr):
    n = len(arr)
    for x in range(n):
        for y in range(0, n-x-1):
            #reverse the inequality sign so that it reverses array
            if arr[y] < arr[y+1] :
                arr[y], arr[y+1] = arr[y+1], arr[y]
    return arr
