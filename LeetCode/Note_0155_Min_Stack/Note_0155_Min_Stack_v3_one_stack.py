class MinStack(object):

    def __init__(self):
        self.stack = [] # [val, min]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack or val < self.stack[-1][1]:
            self.stack.append([val, val])
        else:
            self.stack.append([val, self.stack[-1][1]])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
   

minStack = MinStack();
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())