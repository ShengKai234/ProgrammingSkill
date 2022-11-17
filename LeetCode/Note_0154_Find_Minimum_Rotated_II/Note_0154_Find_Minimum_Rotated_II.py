class Solution(object):
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[r] == nums[mid]:
                # [1,2,3,3,3]
                # in this situation, we need carefully reduce the upper bound, so we minus 1 of r
                r -= 1
            elif nums[r] > nums[mid]:
                # we don't minus 1, the nums[mid] could be ans when the nums is non-decreasing.
                # -> [5,0,1,2,3,4]
                # we need keep the right anser
                r = mid
            else:
                # if nums[r] < nums[mid], it mean rotation in the right of mid -> [3,4,0,1]
                l = mid + 1
        return nums[r]
   

if __name__ == '__main__':
    print("template")
    solution = Solution()

# T:O(n)
# S:O(n)