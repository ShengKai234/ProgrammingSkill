class MyQueue(object):

    def __init__(self):
        self.array1 = []
        self.array2 = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.array1:
            self.front = x
        self.array1.append(x)
        return None

    def pop(self) -> int:
        if not self.array2:
            while self.array1:
                self.array2.append(self.array1.pop())
        pop_value = self.array2[-1]
        self.array2.pop()
        return pop_value
        

    def peek(self) -> int:
        if self.array2:
            return self.array2[-1]
        return self.front

    def empty(self) -> bool:
        return not self.array1 and not self.array2
        


    # def __init__(self):
    #     self.array = []

    # def push(self, x: int) -> None:
    #     self.array.append(x)
    #     return None

    # def pop(self) -> int:
    #     if not self.array:
    #         return None
    #     pop_value = self.array[0]
    #     del self.array[0]
    #     return pop_value

    # def peek(self) -> int:
    #     return self.array[0]

    # def empty(self) -> bool:
    #     if not self.array:
    #         return True
    #     else:
    #         return False
        
   

if __name__ == '__main__':
    print("template")
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())


# T:O(n)
# S:O(n)