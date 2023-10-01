import sys

class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        INF = sys.maxsize
        previous = [INF] * n
        current = [INF] * n
        previous[src] = 0
        for i in range(k + 1):
            current[src] = 0
            for flight in flights:
                preNode, currNode, cost = flight
                if previous[preNode] < INF:
                    current[currNode] = min(current[currNode], previous[preNode] + cost)
            previous = current.copy()
        
        return -1 if current[dst] == INF else current[dst]

    

solution = Solution()
# n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
print(solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
