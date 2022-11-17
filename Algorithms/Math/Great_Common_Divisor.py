class Solution:

    def gcd(self, n1, n2):
        greatest = 0
        if n1 < n2:
            greatest = n1
        else:
            greatest = n2

        while n1 % greatest != 0 or n2 % greatest != 0:
            greatest -= 1

        return greatest


if __name__ == '__main__':
    solution = Solution()
    res = solution.gcd(11, 5)
    print(res)