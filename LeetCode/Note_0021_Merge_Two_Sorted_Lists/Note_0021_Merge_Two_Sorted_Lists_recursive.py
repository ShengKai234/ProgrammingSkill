# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def rec(l1, l2):
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            if l1.val <= l2.val:
                l1.next = rec(l1.next, l2)
                return l1
            else:
                l2.next = rec(l1, l2.next)
                return l2


        return rec(list1, list2)

list1 = ListNode(1, ListNode(2, ListNode(3, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))

solution = Solution()
res = solution.mergeTwoLists(list1, list2)
while res:
    print(res.val)
    res = res.next

# T:O(N + M)
# S:O(N + M)