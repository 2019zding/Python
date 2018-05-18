# Create a stack object that has the
# push, pop, isEmpty methods
# Add 3 new methods
# List all items
    # Some type of loop
    # For vs. while
# Find an item
    # Loop through stack
    # if/else
# Add a list to stack

class Stack:
    def __init__(self):
        self.items = []

# create a push method
# inherit self, and user gives us data

    def push(self, item):
        self.items.append(item)

# create a pop method
# taking in self, and user says
# becaause stack is LIFO

    def pop(self):
        self.items.pop()

# return a boolean
    def isEmpty(self):
        a = []
        if self.items == a:
            print('True')
            return True
        else:
            print('False')
            return False
    def list_items(self):
        for x in self.item:
            print (x)
    def find_me(self, missing):
        for x in self.items:
            if x == missing:
                print(x)

# selection sort
    def b_sort(self):
        n = len(self.items)
        for x in range(n):
            for y in range(0,n-x-1):

                if self.items[y] > self.items[y+1]:
                    #swap numbers
                    self.items[y], self.items[y+1] = self.items[y+1], self.items[y]
        print(self.items)

# create a new stack
rat_stack = Stack()
snake_stack = Stack()
cat_stack = Stack()
# populate some data
cat_stack.push(7)
cat_stack.push(77)
cat_stack.push(777)
rat_stack.push('Sniffle')
snake_stack.push('Hissssss')
# Test to see if empty
rat_stack.isEmpty()
cat_stack.b_sort()
