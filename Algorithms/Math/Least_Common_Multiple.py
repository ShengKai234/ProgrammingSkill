class Solution:
    def lcm(self, n1, n2):
        least = 0
        if n1 > n2:
            least = n1
        else:
            least = n2

        while least % n1 != 0 or least % n2 != 0:
            least += 1

        return least

if __name__ == '__main__':
    solition = Solution()
    res = solition.lcm(13, 11)
    print(res)