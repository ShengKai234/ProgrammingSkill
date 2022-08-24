class Solution(object):
    
    def __init__(self):
        self.count = 0

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        
        length = len(nums)
        
        self.dfs(nums, length, target, 0, 0)
        
        return self.count
    
    def dfs(self, nums, length, target, currSum, currLength):
        if currLength == length:
            if currSum == target:
                self.count += 1
            return

        self.dfs(nums, length, target, currSum + nums[currLength], currLength + 1)
        self.dfs(nums, length, target, currSum - nums[currLength], currLength + 1)

solution = Solution()
print(solution.findTargetSumWays([8,48,11,47,26,12,16,39,38,50,21,12,34,1,28,1,3,9,17,50], 3))

# T:O(t * n) The memo array of size O(t \cdot n)O(t⋅n) has been filled just once. Here, tt refers to the sum of the numsnums array and nn refers to the length of the numsnums array.
# S:O(t * n) The depth of recursion tree can go up to nn. The memo array contains t \cdot nt⋅n elements.
