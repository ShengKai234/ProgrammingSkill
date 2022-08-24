class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True

s = Solution()
print(s.canAttendMeetings([[0,30],[5,10],[15,20]]))

# T:O(n)
# S:O(n)