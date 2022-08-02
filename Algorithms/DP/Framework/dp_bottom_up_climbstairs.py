class Solution:
    def framework_bottom_up_climbstairs(self, n: int) -> int:
        if n == 1:
            return 1

        # An array that represents the answer to the problem for a givne state
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

solution = Solution()
print(solution.framework_bottom_up_climbstairs(10))