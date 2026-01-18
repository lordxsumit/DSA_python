class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    def push(self, value):
        self.s.append(value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty!")
        
        return self.s[-1]   # Here, I am using '-1' instead of '0' for the top because I have used the append function to add value in the push method instead of insert function. (if insert function was used, then here i would have written '0' for the top of the stack)
        
    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty cannot pop anything from the stack!")
        
        return self.s.pop()
        
    def printStack(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty!")
        
        for x in self.s:
            print(x, end=' ')
        
        print("\n")

stk = stack()
stk.push(10)
stk.push(20)
stk.push(30)

stk.printStack()

# result = stk.pop()
# print(f"The element popped from stack is {result}")

# stk.printStack()

print(f"The top of the stack contains {stk.peek()}")