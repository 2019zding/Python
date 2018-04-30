class Queue():
    # init
    def __init__(self):
        self.items = []


    # enqueue
    def enqueue(self, items):
        return self.items.insert(0, items)

    # dequeue
    def dequeue(self):
        return self.items.pop()
    # show all
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
