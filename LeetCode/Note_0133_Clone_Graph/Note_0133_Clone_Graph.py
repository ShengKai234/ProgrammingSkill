
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val, [])
        
        self.visited[node] = clone_node
        
        if node.neighbors:
            for n in node.neighbors:
                clone_node.neighbors.append(self.cloneGraph(n))
            
        return clone_node
        

solution = Solution()

# T:O(n + m),  m: neighbors
# S:O(n)