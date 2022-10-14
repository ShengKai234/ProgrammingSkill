import sys

class MaxHeap:

    def __init__(self, size):
        
        self.heapSize = size + 1
        self.realSize = 0
        self.maxheap = [0] * self.heapSize

    def add(self, value):
        self.realSize += 1
        
        if self.realSize > self.heapSize:
            print("element is full!")
            self.realSize -= 1
            return

        self.maxheap[self.realSize] = value

        index = self.realSize
        parent = self.realSize // 2

        while parent > 0 and self.maxheap[index] > self.maxheap[parent]:
            self.maxheap[index], self.maxheap[parent] = self.maxheap[parent], self.maxheap[index]
            index = parent
            parent = index // 2

    def peek(self) -> int:
        return self.maxheap[1]

    def pop(self) -> int:

        if self.realSize < 1:
            print("Don't have any element!")
            return -sys.maxsize
        else:
            pop_value = self.maxheap[1]
            self.maxheap[1] = self.maxheap[self.realSize]
            self.realSize -= 1

            index = 1
            while index <= self.realSize // 2:
                left_child = index * 2
                right_child = index * 2 + 1

                if self.maxheap[left_child] > self.maxheap[index] or self.maxheap[right_child] > self.maxheap[index]:
                    if self.maxheap[left_child] > self.maxheap[right_child]:
                        self.maxheap[left_child], self.maxheap[index] = self.maxheap[index], self.maxheap[left_child]
                        index = left_child
                    else:
                        self.maxheap[right_child], self.maxheap[index] = self.maxheap[index], self.maxheap[right_child]
                        index = right_child
                else:
                    break

                # if self.maxheap[left_child] > self.maxheap[index]:
                #     self.maxheap[left_child], self.maxheap[index] = self.maxheap[index], self.maxheap[left_child]
                #     index = left_child
                #     continue
                # elif self.maxheap[right_child] > self.maxheap[index]:
                #     self.maxheap[right_child], self.maxheap[index] = self.maxheap[index], self.maxheap[right_child]
                #     index = right_child
                #     continue
                # else:
                #     break
        
            return pop_value

    def size(self) -> int:
        return self.realSize

    def __str__(self) -> str:
        return str(self.maxheap[1 : self.realSize + 1])

if __name__ == "__main__":
    print("MaxHeap...")

    maxHeap = MaxHeap(5)

    maxHeap.add(1)
    maxHeap.add(2)
    maxHeap.add(3)
    # [3,1,2]
    print(maxHeap)
    # 3
    print(maxHeap.peek())
    # 3
    print(maxHeap.pop())
    # 2
    print(maxHeap.pop())
    # 1
    print(maxHeap.pop())
    maxHeap.add(4)
    maxHeap.add(5)
    # [5,4]
    print(maxHeap)