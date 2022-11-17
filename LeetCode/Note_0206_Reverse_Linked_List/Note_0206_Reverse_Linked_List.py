from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def printNode(self, head):
        if head == None:
            return

        print(head.val)
        self.printNode(head.next)

solution = Solution()

node5 = ListNode(5, None)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
print(node1)
solution.printNode(node1)


print("reverse...")
res = solution.reverseList(node1)
solution.printNode(res)
# T:O(n)
# S:O(n)