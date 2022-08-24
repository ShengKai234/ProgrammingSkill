from operator import le


class Solution(object):
    def merge(self, intervals):
        stack = []
        n = len(intervals)

        # O(NlogN)
        def mergesort(arr):
            size = len(arr)
            if size > 1:
                mid = size // 2

                L = arr[:mid]
                R = arr[mid:]
                mergesort(L)
                mergesort(R)

                l_index = r_index = k = 0

                while l_index < len(L) and r_index < len(R):
                    if L[l_index][0] < R[r_index][0]:
                        arr[k] = L[l_index]
                        l_index += 1
                    else:
                        arr[k] = R[r_index]
                        r_index += 1
                    k += 1

                while l_index < len(L):
                    arr[k] = L[l_index]
                    l_index += 1
                    k += 1

                while r_index < len(R):
                    arr[k] = R[r_index]
                    r_index += 1
                    k += 1
                
        mergesort(intervals)

        # O(N)
        for i in range(n):
            if len(stack) > 0 and stack[-1][1] >= intervals[i][0]:
                prevstack = stack.pop()
                stack.append([prevstack[0], max(prevstack[1], intervals[i][1])])
            else:
                stack.append(intervals[i])
        # case: [1,4] [3,5] -> [1,5]
        # case: [1,4] [1,5] -> [1,5]
        # case: [1,4] [2,3] -> [1,4]
        # case: [1,4] [1,3] -> [1,4]
        # case: [1,4] [5,9] -> [1,4] [5,9]
        return stack
        
solution = Solution()
assert (solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]])
assert (solution.merge([[1,4],[0,4]]) == [[0,4]])
assert (solution.merge([[1,4],[2,3]]) == [[1,4]])

# T:O(NlogN)
# S:O(logN), worst case O(N)