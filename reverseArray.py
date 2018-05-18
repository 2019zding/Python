def reverseArray(self):
    n = len(self.items)
    for x in range(n):
        for y in range(0,n-x-1):
#reverse the inequality sign
            if self.items[y] < self.items[y+1]:
                #swap numbers
                self.items[y], self.items[y+1] = self.items[y+1], self.items[y]
    print(self.items)
