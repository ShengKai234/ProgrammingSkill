# Code for Min Heap
import heapq

# Creste an array
minHeap = []

# heapify the array into a Min Heap
heapq.heapify(minHeap)

# Add 3, 2, 1 respectively to the Min Heap
heapq.heappush(minHeap, 3 * -1)
heapq.heappush(minHeap, 1 * -1)
heapq.heappush(minHeap, 2 * -1)

# Check all elements in the Min Heap, the result is [1, 3, 2]
print("Max Heap: ", minHeap)

# Get the top element of the Min Heap
peekNum = minHeap[0] * -1

# The result is 1
print("peek number: ", peekNum)

# Delete the top element in the Min Heap
popNum = heapq.heappop(minHeap) * -1

# Check the top element after deleting 1, the result is 2
print("peek number: ", minHeap[0] * -1)

# Check all elements in the Min Heap, the result is [2, 3]
print("minHeap: ", minHeap)

# Check the number of elements in the Min Heap
# Which is also the length of the Min Heap
size = len(minHeap)

# The result is 2
print("minHeap size: ", size)