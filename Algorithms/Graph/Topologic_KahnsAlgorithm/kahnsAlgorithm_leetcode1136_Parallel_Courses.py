from collections import *
from typing import List;

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        inDegree = [0] * (n + 1)
        
        for edge in (relations):
            f, t = edge
            adj[f].append(t)
            inDegree[t] += 1
        
        queue = deque([])
        for i in range(1, len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        
        semester = 0
        while queue:
            semester += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                for nxt in adj[curr]:
                    inDegree[nxt] -= 1
                    if inDegree[nxt] == 0:
                        queue.append(nxt)
                        
        for i in range(1, len(inDegree)):
            if inDegree[i] != 0:
                return -1
        return semester

solution = Solution()
print(solution.minimumSemesters(3, [[1,3],[2,3]]))