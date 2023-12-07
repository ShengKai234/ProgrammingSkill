from collections import *
from typing import List;

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        inDegree = [0] * numCourses
        for curr, pre in prerequisites:
            adj[pre].append(curr)q
            inDegree[curr] += 1
        
        queue = deque([])
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            for next in adj[c]:
                inDegree[next] -= 1
                if inDegree[next] == 0:
                    queue.append(next)
        
        for i in range(len(inDegree)):
            if inDegree[i] != 0:
                return []
        return res

solution = Solution()
print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))