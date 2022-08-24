from os import curdir
import queue


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fast
        visited = {'0'}
        queue = []
        queue.append([n, 0])
        while queue:
            curr, depth = queue.pop(0)
            for i in range(1, curr):
                val = i * i
                if val > curr:
                    break
                if curr == val:
                    return depth + 1
                nextN = curr - val
                if nextN in visited:
                    continue
                queue.append([nextN, depth + 1])
                visited.add(nextN)
        return n

        # slow
        # visited = {n}
        # queue = []
        # queue.append([n, 0])
        # while queue:
        #     curr, depth = queue.pop(0)
        #     if curr == 0:
        #         return depth
        #     for i in range(1, curr):
        #         val = i * i
        #         if val > curr:
        #             break
        #         nextN = curr - val
        #         nextDepth = depth + 1
        #         if nextN in visited:
        #             continue
        #         queue.append([nextN, nextDepth])
        #         visited.add(nextN)

solution = Solution()
print(solution.numSquares(7927))
