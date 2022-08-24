class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minRecord = []
        self.min = 2 ** 31 - 1

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val < self.min:
            self.min = val
        self.minRecord.append(self.min)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minRecord.pop()
        if len(self.minRecord) != 0:
            self.min = self.minRecord[-1]
        else:
            self.min = 2 ** 31 - 1

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