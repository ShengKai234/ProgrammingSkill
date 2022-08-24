class Solution:
    #function for dfs 
    def DFSUtil(self, graph, node, visited):
        
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                self.DFSUtil(graph, neighbour, visited)

    def DFS(self, graph, node):
        visited = set() # Set to keep track of visited nodes of graph.
        self.DFSUtil(graph, node, visited)
        


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
solution = Solution()
solution.DFS(graph, '5')