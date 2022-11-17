from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        
        def rec(start, end):
            if start > end:
                return [None]

            all_trees = []

            # pick i, find left and right tree
            for i in range(start, end + 1):
                # left trees
                left_trees = rec(start, i - 1)

                # right 
                right_trees = rec(i + 1, end)

                for left_node in left_trees:
                    for right_node in right_trees:
                        current_node = TreeNode(i, left_node, right_node)
                        all_trees.append(current_node)
            return all_trees

        return rec(1, n)
    
    def print_node(self, node):
        if node == None:
            print(None)
            return
        print(node.val)
        self.print_node(node.left)
        self.print_node(node.right)

if __name__ == '__main__':
    print("template")
    solution = Solution()
    res = solution.generateTrees(3)
    for node in res:
        print("------------")
        solution.print_node(node)
            


# T:O(n)
# S:O(n)