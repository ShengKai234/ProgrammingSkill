from typing import List

class Solution(object):
    
    def __init__(self):
        print('Start 3Sum')

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        size = len(nums)
        # f is fix point
        for f in range(size):
            if f == 0 or nums[f] != nums[f-1]:
                p1, p2 = f + 1, size - 1
                target = 0 - nums[f]
                while p1 < p2:
                    other = nums[p1] + nums[p2]
                    if target == other:
                        result.append([nums[f], nums[p1], nums[p2]])
                        while p1 < p2 and nums[p1] == nums[p1+1]:
                            p1 += 1
                        while p1 < p2 and nums[p2] == nums[p2-1]:
                            p2 -= 1
                        p1 += 1
                        p2 -= 1
                    elif target < other:
                        p2 -= 1
                    else:
                        p1 += 1
        return result

if __name__ == '__main__':

    nums = [-1,0,1,2,-1,-4]
    nums = [0,0,0]

    solution = Solution()
    print(solution.threeSum(nums))

    # O(N^2)