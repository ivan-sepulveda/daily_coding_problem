class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        # Add an item to the stack
        self.stack.append(x)

    def pop(self):
        # Remove and return the top element
        self.stack.pop()

    def peek(self):
        return self.stack[-1]