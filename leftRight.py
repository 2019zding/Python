def balance(left, right):
    leftWeight = 0
    rightWeight = 0
    # Check weight of each argument
    for x in left:
        if x == '!':
            leftWeight = leftWeight + 2
        else:
            leftWeight = leftWeight + 3

    for y in right:
        if y == '!':
            rightWeight = rightWeight + 2
        else:
            rightWeight = rightWeight + 3

    if (leftWeight > rightWeight):
        print('Left')
        return 'Left'
    elif (rightWeight > leftWeight):
        print('Right')
        return 'Right'
    else:
        print('Balance')
        return 'Balance'
