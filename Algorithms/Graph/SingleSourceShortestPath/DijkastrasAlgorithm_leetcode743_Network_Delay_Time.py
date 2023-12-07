class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. adjancy
        adj = defaultdict(list)
        for f, to, w in times:
            adj[f].append((to, w))
        
        # shortest time from k
        st = [float('inf')] * (n + 1) # 1-index
        st[0] = 0
        st[k] = 0 # k to k is 0
        
        # visited
        visited = [False] * (n + 1)
        
        heap = [(0, k)] # (time, origin vertex number)
        heapq.heapify(heap)
        while heap:
            travelTime, vertex = heapq.heappop(heap)
            visited[vertex] = True
            
            for to, w in adj[vertex]:
                if not visited[to]:
                    nextTravelTime = travelTime + w
                    st[to] = min(st[to], nextTravelTime)
                    heapq.heappush(heap, (nextTravelTime, to))
        
        ans = max(st)
        if ans == float('inf'):
            return -1
        return ans