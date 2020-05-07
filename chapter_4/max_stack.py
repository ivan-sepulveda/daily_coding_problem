"""
4.1 Implement a max stack
Implement a stack that has the following methods:

push(val): push val onto the stack
pop: pop off and return the topmost element of the stack.
    If there are no elements in the stack, throw an error.
max: return the maximum value in the stack currently.
    If there are no elements in the stack, throw an error.

Each method should run constant in time.
"""


class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val):
        # Add an item to the stack
        self.stack.append(val)
        if self.maxes:
            self.maxes.append(max(val, self.maxes[-1]))
        else:
            self.maxes.append(val)

    def pop(self):
        # Remove and return the top element
        self.stack.pop()
    """
    def max():
        return self.maxes[-1]
    """
