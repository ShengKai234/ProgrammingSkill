class Solution:
    def longestCycle(self, edges: List[int]) -> int: 

        def rec(head, visitGlobal):
            visit = []
            node = head
            while node != -1:
                if node in visit:
                    if head == node:
                        for i in range(visit):
                            visitGlobal.add(visit[i])
                        return len(visit)
                    else:
                        return rec(node, visitGlobal)
                visit.append(node)
                node = edges[node]
            return -1


        max_level = 0
        visitGlobal = []
        for i in range(len(edges)):
            if edges[i] in visitGlobal:
                continue
            max_level = max(rec(i, visitGlobal), max_level)

        if max_level <= 0:
            return -1
        return max_level