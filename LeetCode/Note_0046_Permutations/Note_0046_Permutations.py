from typing import List

class Solution(object):

    def __init__(self):
        print('Start permute')

    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        permutationsList = []
        
        '''
        This function recursive every level for swap
        size: nums length
        base_swap_index: base change fix with less index
        nums: array
        return None
        '''
        def backtrack(base_swap_index, nums):
            # in all index are used up
            # base_swap_index is the last one element, no one can swap
            if (base_swap_index == size):
                permutationsList.append(nums[:])
                return

            # loop every index where is less or equal then base_swap_index base on base_swap_index
            for i in range(base_swap_index, size):
                # swap i and base_swap_index
                nums[i], nums[base_swap_index] = nums[base_swap_index], nums[i]
                backtrack(base_swap_index + 1, nums)
                nums[i], nums[base_swap_index] = nums[base_swap_index], nums[i]



        backtrack(0, nums)
        print(permutationsList)
   

if __name__ == '__main__':
    solution = Solution()
    solution.permute([1,2,3])

# T:O(n)
# S:O(n)