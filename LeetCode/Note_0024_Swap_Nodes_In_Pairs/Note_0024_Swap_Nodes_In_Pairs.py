from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        f_node = head
        s_node = head.next

        f_node.next = self.swapPairs(s_node.next)
        s_node.next = f_node

        return s_node

    def printNode(self, head):
        if head == None:
            return

        print(head.val)
        self.printNode(head.next)

solution = Solution()


node4 = ListNode(4, None)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(node1)
solution.printNode(node1)


print("reverse...")
res = solution.swapPairs(node1)
solution.printNode(res)
# T:O(n)
# S:O(n)