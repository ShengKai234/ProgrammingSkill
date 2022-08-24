class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        queue = []
        n = len(rooms)
        m = len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        

        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            room = queue.pop(0)
            for move in moves:
                row = room[0] + move[0]
                col = room[1] + move[1]
                if 0 > row or row >= n or 0 > col or col >= m or rooms[row][col] != 2147483647:
                    continue
                rooms[row][col] = rooms[room[0]][room[1]] + 1
                queue.append([row,col])
        return rooms

        
        # moves = [[0,1],[1,0],[-1,0],[0,-1]]
        # step = 0
        # while queue:
        #     size = len(queue)
        #     for i in range(size):
        #         room = queue.pop(0)
        #         rooms[room[0]][room[1]] = min(step, rooms[room[0]][room[1]])
        #         for move in moves:
        #             row = room[0] + move[0]
        #             col = room[1] + move[1]
        #             if [row, col] in visited:
        #                 continue
        #             if 0 > row or row >= n or 0 > col or col >= m or rooms[row][col] != 2147483647:
        #                 continue
        #             queue.append([row,col])
        #             visited.append([row,col])
        #             # if 0 <= row and row < n and 0 <= col and col < m and rooms[row][col] == 2147483647:
        #             #     queue.append([row,col])
        #             #     visited.append([row,col])
        #     step += 1
        # return rooms

solution = Solution()
assert(solution.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]) == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]])