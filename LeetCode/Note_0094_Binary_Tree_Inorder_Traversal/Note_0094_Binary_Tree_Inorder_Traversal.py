from typing import List
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def recursive(node):
            if node is None:
                return

            recursive(node.left)
            output.append(node.val)
            recursive(node.right)
            
        recursive(root)
        return output
   

if __name__ == '__main__':
    print("kai:Note_0094_Binary_Tree_Inorder_Traversal")
    root = TreeNode()
    root.val = 1

    node1 = TreeNode()
    node1.val = 2

    node2 = TreeNode()
    node2.val = 3

    root.right = node1
    node1.left = node2

    solution = Solution()
    print(solution.inorderTraversal(root))
    
# T:O(n)
# S:O(n)