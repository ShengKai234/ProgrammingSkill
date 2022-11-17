# Code for Min Heap
import heapq

# Creste an array
minHeap = []

# heapify the array into a Min Heap
heapq.heapify(minHeap)

# Add 3, 2, 1 respectively to the Min Heap
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)

# Check all elements in the Min Heap, the result is [1, 3, 2]
print("Min Heap: ", minHeap)

# Get the top element of the Min Heap
peekNum = minHeap[0]

# The result is 1
print("peek number: ", peekNum)

# Delete the top element in the Min Heap
popNum = heapq.heappop(minHeap)

# Check the top element after deleting 1, the result is 2
print("peek number: ", minHeap[0])

# Check all elements in the Min Heap, the result is [2, 3]
print("minHeap: ", minHeap)

# Check the number of elements in the Min Heap
# Which is also the length of the Min Heap
size = len(minHeap)

# The result is 2
print("minHeap size: ", size)


test = [[0,0],[0,1],[1,1],[1,0]]
heap = []
heapq.heappush(heap, test[3])
print(heap)
heapq.heappush(heap, test[2])
print(heap)
heapq.heappush(heap, test[1])
print(heap)
heapq.heappush(heap, test[0])
print(heap)