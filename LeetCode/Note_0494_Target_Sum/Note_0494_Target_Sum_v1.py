import re


class Solution(object):
    
    def __init__(self):
        self.count = 0
        self.memo = {}
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        
        length = len(nums)
        
        self.dfs(nums, length, target, 0, 0)
        
        return self.memo[(0, 0)]
    
    def dfs(self, nums, length, target, currSum, currLength):
        if currLength == length:
            if currSum == target:
                self.memo[(currLength, currSum)] = 1
            else:
                self.memo[(currLength, currSum)] = 0

        if (currLength, currSum) not in self.memo:
            self.memo[(currLength, currSum)] = self.dfs(nums, length, target, currSum + nums[currLength], currLength + 1) + self.dfs(nums, length, target, currSum - nums[currLength], currLength + 1)
        return self.memo[(currLength, currSum)]
        
solution = Solution()
print(solution.findTargetSumWays([8,48,11,47,26,12,16,39,38,50,21,12,34,1,28,1,3,9,17,50], 3))

# T:O(nlogn)
# S:O(n)