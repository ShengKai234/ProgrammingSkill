import json
import unittest

class Solution(object):
    def __init__(self):
        print('Start Find Pivot Index')

    def pivotIndex(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # timeout
        # size = len(nums)
        # for i in range(0, size):
        #     leftSum, rightSum = 0, 0
        #     left, right = 0, size - 1
        #     while left < i:
        #         leftSum += nums[left]
        #         left += 1
        #     while right > i:
        #         rightSum += nums[right]
        #         right -= 1
        #     if leftSum == rightSum:
        #         return i
        # return -1

        size = len(nums)
        sumList = [0] * size
        sumNums = 0
        for i in range(size):
            sumNums += nums[i]
            sumList[i] = sumNums
        
        # 極端值錯誤 povit = 0 or povit = size
        # for i in range(0, size - 1):
        #     if sumList[i - 1] == sumList[-1] - sumList[i]:
        #         return i
        # if sumList[-1] - sumList[0] == 0:
        #     return 0
        # if sumList[size - 2] == 0:
        #     return size - 1

        left, right = 0, sumNums
        for i in range(size):
            right = sumList[-1] - sumList[i]
            if left == right:
                return i
            left = sumList[i]
        return -1

class CalculatorTest(unittest.TestCase):
    def test(self, testcase, expect):
        self.assertEqual(testcase, expect)

if __name__ == '__main__':

    calculatorTest = CalculatorTest()

    solution = Solution()
    
    nums = [1,7,3,6,5,6]
    calculatorTest.test(solution.pivotIndex(nums), 3)
    # assert solution.pivotIndex(nums) == 3

    nums = [2,1,-1]
    calculatorTest.test(solution.pivotIndex(nums), 0)
    # assert solution.pivotIndex(nums) == 0

    nums = [-1,-1,0,1,1,0]
    calculatorTest.test(solution.pivotIndex(nums), 5)
    # assert solution.pivotIndex(nums) == 5

    nums = [-1,-1,-1,1,1,1]
    calculatorTest.test(solution.pivotIndex(nums), -1)
    # assert solution.pivotIndex(nums) == -1

    f = open("testcase.txt")
    oneLine = f.readline()
    nums = json.loads(oneLine)
    calculatorTest.test(solution.pivotIndex(nums), 8650)
    # assert solution.pivotIndex(nums) == 8650
    print('pass all test!!')
    
    # O(N)