from re import M
from traceback import print_tb


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        res = 0
        employee = dict()
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            employee.setdefault(manager[i], [])
            employee[manager[i]].append(i)
        queue = []
        # visited = []

        queue.append([headID, informTime[headID]])
        # visited.append(headID)
        while queue:
            m_id, time = queue.pop(0)
            if employee.get(m_id) is None:
                continue
            res = max(res, time)
            for e in employee[m_id]:
                # if e not in visited:
                queue.append([e, time + informTime[e]])
                    # visited.append(e)
                
        return res

solution = Solution()

print(solution.numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))

print(solution.numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]))