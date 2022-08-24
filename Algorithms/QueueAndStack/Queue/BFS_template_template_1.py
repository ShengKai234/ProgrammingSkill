class Solution:
    def BFS(self, graph, node):
        # step 1 build graph if graph not given

        # step 2 set queue
        queue = [] # store all nodes which are waiting to be processed
        step = 0 # member of steps needed from root to current node
        
        # initialize
        queue.append(node)

        # step 3 BFS
        while queue:
            # iterate the nodes which are already in the queue
            size = len(queue)
            for i in range(size):
                m = queue.pop(0)
                print(m, end = ' ')
                for neighbour in graph[m]:
                    queue.append(neighbour)
            step += 1
        print('step: ' + str(step))

        return -1 # there is no path from root to target


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
solution = Solution()
solution.BFS(graph, '5')