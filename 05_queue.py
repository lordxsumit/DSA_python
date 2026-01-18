""                                             # Simple queue and it's operations

class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return len(self.item)

    def insert(self, value):
        self.item.append(value)

    def delete(self):
        if self.isEmpty() == 0:
            raise Exception("Queue is empty!")
        
        return self.item.pop(0)
    
    def print(self):
        if self.isEmpty() == 0:
            raise Exception("Queue is empty!")
        
        for x in self.item:
            print(x, end=" ")

    

que = Queue()

que.insert(10)
que.insert(20)
que.insert(30)

que.print()
print("\n")

result = que.delete()
print(f"The element popped out is {result}")

que.print()

"""


"""                                            # Double-Ended queue and it's operations
""