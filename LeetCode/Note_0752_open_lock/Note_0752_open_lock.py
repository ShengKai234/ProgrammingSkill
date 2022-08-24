class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]
        queue = [['0000', 0]]
        seen = ['0000']
        while queue:
            node, depth = queue.pop(0)
            if node == target:
                return depth
            if node in deadends:
                continue
            for n in neighbors(node):
                if n in seen:
                    continue
                queue.append([n, depth + 1])
                seen.append(n)
        return -1


# def neighbour(node):
#     for i in range(4):
#         x = int(node[i])
#         for d in (-1, 1):
#             y = (x + d) % 10
#             # print(x, d, y)
#             print(node[:i], str(y), node[i+1:])
#             # yield node[:i] + str(y) + node[i+1:]

# neighbour('0000')

solution = Solution()
print(solution.openLock(["1131","1303","3113","0132","1301","1303","2200","0232","0020","2223"],"3312"))
