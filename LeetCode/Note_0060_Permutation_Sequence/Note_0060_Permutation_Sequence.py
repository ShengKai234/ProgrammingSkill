class Solution(object):
    

    def getPermutation(self, n: int, k: int) -> str:
        
        nums = ['1']
        factorial = [1]

        # generate factorial system base 0!->1, 1!->1, 2!->2, 3!->6 ...., (n-1)!
        for num in range(1, n):
            factorial.append(factorial[num - 1] * num)
            nums.append(str(num + 1))
        
        # fix k in array index, fit k in the interval 0 ~ (n! - 1)
        k -= 1

        res = []
        # group_index is appear times in each element
        # n is remain size in interval
        for i in range(n, 0, -1):
            # n division k! to find group in each group
            group_index = k // factorial[i - 1]
            # rest next stage take k number, 下位（stage）的取值位子
            k = k % factorial[i - 1]
            res.append(nums[group_index])
            # delete nums which is took
            del nums[group_index]

   

if __name__ == '__main__':
    print("test")
    solution = Solution()
    solution.getPermutation(3, 3)

# T:O(n)
# S:O(n)