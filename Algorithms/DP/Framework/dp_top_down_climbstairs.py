class Solution:
    def framework_top_down_climbstairs(self, n: int) -> int:
        """A function that returns the answer to the problem for a given state."""
        # Base cases: when i is less than 3 there are i ways to reach the ith stair.
        def dp_top_down(i):
            if i <= 2:
                return i;
            if i not in memo:
                memo[i] = dp_top_down(i - 1) + dp_top_down(i - 2)
            return memo[i]

        memo = {}
        return dp_top_down(n)

solution = Solution()
print(solution.framework_top_down_climbstairs(10))