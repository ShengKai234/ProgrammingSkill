import sys


class MinHeap:
    def __init__(self, heapSize):
        # Create a complete binary tree using an array
        # Then use the binary tree to construct a Heap
        self.heapSize = heapSize

        # the number of size is needed when instantiating an array
        # heapSize records the size of the array
        self.minheap = [0] * (heapSize + 1)
        
        # realSize records the number of element in the Heap
        self.realSize = 0

    def add(self, element):
        self.realSize += 1
        
        # If the number of elements in the Heap exceeds the preset heapZize
        # print "Added too many elements" and return
        if self.realSize > self.heapSize:
            print("Add too many elements")
            self.realSize -= 1
            return
        
        # Add the element into the array
        self.minheap[self.realSize] = element

        # index of the newly added element
        index = self.realSize

        # Parent node of the newly added element
        # Note if we use an array to represent the complete binaty tree
        # and store the root node at index 1
        # index of the parent node of any node is [index of the node / 2]
        # index of the left child node is [index of the node * 2]
        # index of the right child node is [index of the node * 2 + 1]
        parent = index // 2

        while (self.minheap[index] < self.minheap[parent] and index > 1):
            self.minheap[index], self.minheap[parent] = self.minheap[parent], self.minheap[index]
            index = parent
            parent = index // 2



    def peek(self):
        return self.minheap[1]

    def pop(self):
        # If the number of elements in the current Heap is 0,
        # print "Don't have any elements" and return  a default value
        if self.realSize < 1:
            print("Don't have any element!")
            return sys.maxsize
        else:
            # when there are still elements in the Heap
            # self.realsize >= 1
            removeElement = self.minheap[1]

            # put the last element in the Heap to the top of Heap
            self.minheap[1] = self.minheap[self.realSize]
            self.realSize -= 1
            index = 1

            # when the deleted element is not a leaf node
            # leaf > self.realSzie // 2
            while (index <= self.realSize // 2):
                # the left child of the deleted element
                left = index * 2

                # the right child of the deleted element
                right = (index * 2) + 1
                
                # If the 
                if self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]:
                    if self.minheap[left] < self.minheap[right]:
                        self.minheap[index], self.minheap[left] = self.minheap[left], self.minheap[index]
                        index = left
                    else:
                        self.minheap[index], self.minheap[right] = self.minheap[right], self.minheap[index]
                        index = right
                else:
                    # index is minmum
                    break
            
            return removeElement

    def size(self):
        return self.realSize
    
    def __str__(self):
        return str(self.minheap[1:self.realSize + 1])

if __name__ == "__main__":
    # Test case
    minHeap = MinHeap(5)
    minHeap.add(3)
    minHeap.add(1)
    minHeap.add(2)

    # [1, 3, 2]
    print(minHeap)

    # 1
    print(minHeap.peek())

    # 1
    print(minHeap.pop())

    # 2
    print(minHeap.pop())

    # 3
    print(minHeap.pop())

    minHeap.add(4)
    minHeap.add(5)

    # [4,5]
    print(minHeap)