class Queue:
    def __init__(self):
        self.stack = []

    def rpop(self):
        if len(self.stack) == 1:
            self.result = self.stack.pop()
        else:
            item = self.stack.pop()
            self.rpop()
            self.stack.append(item)

    def enquie(self, item):
        if not item:
            # Throw invalid argument
            pass
        self.stack.append(item)
        self.result = None

    def deque(self):
        if not self.stack:
            # Throw invalid operaion exception
            pass
        self.rpop()
        return self.result



q = Queue()
q.enquie(2)
q.enquie(3)
q.enquie(4)
q.enquie(5)
print(q.deque())
print(q.deque())
print(q.deque())
q.enquie(6)
q.enquie(7)
print(q.deque())
