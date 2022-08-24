class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minRecord = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minRecord or val < self.minRecord[-1]:
            self.minRecord.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minRecord.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minRecord[-1]
        


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