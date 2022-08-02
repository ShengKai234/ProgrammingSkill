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
        head = ListNode(-1)
        pre = head
        while list1 and list2:
            if list1.val <= list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next
            
        if list1 is None:
            pre.next = list2
        else:
            pre.next = list1
        return head.next

list1 = ListNode(1, ListNode(2, ListNode(3, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, None)))

solution = Solution()
res = solution.mergeTwoLists(list1, list2)
while res:
    print(res.val)
    res = res.next

# T:O(N + M)
# S:O(1)