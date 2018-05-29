def countDown(n):
    if n < 0:
        return 0
    else:
        print(n)
        n = n-1
        countDown(n)

countDown(7)
