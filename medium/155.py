
class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)
    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



#from chatGPT 

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


# Example usage
min_stack = MinStack()
min_stack.push(5)
min_stack.push(3)
min_stack.push(7)
min_stack.push(2)

print("Top:", min_stack.top())        # Output: 2
print("Min:", min_stack.getMin())     # Output: 2

min_stack.pop()
print("Top after pop:", min_stack.top())    # Output: 7
print("Min after pop:", min_stack.getMin()) # Output: 3

min_stack.pop()
min_stack.pop()
print("Top now:", min_stack.top())          # Output: 5
print("Min now:", min_stack.getMin())       # Output: 5



"""