import math
# from math import inf

class Solution(object):
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        right_sum = sum(nums)
        mini = math.inf
        mini_index = 0
        left_sum = 0
        tmp = 0
        for i in range(n):
            left_sum += nums[i]
            right_sum -= nums[i]
            
            if i < n - 1:
                tmp = abs(left_sum // (i + 1) - right_sum // (n - i - 1))
            else:
                tmp = abs(left_sum // (i + 1))
            # print(left_sum, i + 1, right_sum, n - i - 1 , '-', tmp)
            if tmp < mini:
                mini = tmp
                mini_index = i
        return mini_index
   

if __name__ == '__main__':
    print("template")
    _list = [100000,100000,100000,100000,100000,100000,0,0,0,0,0,0]
    solution = Solution()
    res = solution.minimumAverageDifference(_list)
    print(res)

# T:O(n)
# S:O(n)