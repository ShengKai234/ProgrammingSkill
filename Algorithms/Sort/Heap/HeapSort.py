from turtle import left
from typing import List;

class HeapSort:
    def heapSort(self, lst: List[int]) -> List[int]:
        def max_heapify(heap_size, index):
            left, right = 2 * index + 1, 2 * index + 2
            large = index
            if left < heap_size and lst[large] < lst[left]:
                large = left
            if right < heap_size and lst[large] < lst[right]:
                large = right
            if large != index:
                lst[index], lst[large] = lst[large], lst[index]
                max_heapify(heap_size, large)

        for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(lst), i)

        for i in range(len(lst) - 1, -1, -1):
            lst[0], lst[i] = lst[i], lst[0]
            max_heapify(i, 0)
        
        print(arr)

    
if __name__ == "__main__":
    print("HeapSort...")
    arr = [7,3,2,5,6,10,9,8,1]

    heapSort = HeapSort()
    heapSort.heapSort(arr)