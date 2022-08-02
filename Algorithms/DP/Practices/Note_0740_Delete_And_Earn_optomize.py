class Solution(object):
    def deleteAndEarn(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = {}
        maxVal = 0
        for num in nums:
            if num not in numMap:
                numMap[num] = num
                if num > maxVal:
                    maxVal = num
            else:
                numMap[num] += num
        
        
        memo = {}
        def dp(i) -> int:
            # Fill number key-value key=i if i not exist in the map
            if i not in numMap:
                    numMap[i] = 0
            if i == 0:
                return numMap[i]
            if i == 1:
                if i - 1 not in numMap:
                    numMap[i - 1] = 0
                return max(numMap[i], numMap[i - 1])
            if i not in memo:
                memo[i] = max(dp(i - 1), dp(i - 2) + numMap[i])
            return memo[i]
        return dp(maxVal)


nums = [2,2,3,3,3,4]
solution = Solution()
assert solution.deleteAndEarn(nums) == 9

nums = [2,2,3,3,3,9]
solution = Solution()
assert solution.deleteAndEarn(nums) == 18

print('pass all test!!')

# Speed up 20%
# T:O(N + k)
# S:O(N + k)
# k is max value in nums