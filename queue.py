class Queue():
    # initialization
    def __init__(self):
        self.items = []


    # enqueue, which means adding an item to a queue
    def enqueue(self, items):
        return self.items.insert(0, items)

    # dequeue, which means removing an item from a queue
    def dequeue(self):
        return self.items.pop()
    # showing all of the items in the list
    def list(self):
        for x in self.items:
            print(x)

# q is an instance of class Queue
# q is a type of Queue
q = Queue()
# adding to the queue
q.enqueue('cat')
q.enqueue('rat')
# debug, see list before dequeue
print("This is popped")
print(q.dequeue())
# debug, see list after dequeue
q.list()
