class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i in range(n):
            while stack and temperatures[i] > stack[-1][1]:
                prev = stack.pop()
                index = prev[0]
                result[index] = i - index
            stack.append([i, temperatures[i]])
        
        return result
                
        # i = 0 -> 0,73
            # stack = [[0,73]]
        # i = 1 -> 1,74
            # while pass
            # stack.pop() -> prev = [0, 73]
            # result[0] = 1 - 0
            # stack = [[1,74]]
solution = Solution()
assert solution.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0]
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))


# T:O(n)
# S:O(n) from stack
# Note: answer does not count towards the space complexity because space used for the output format does not count.