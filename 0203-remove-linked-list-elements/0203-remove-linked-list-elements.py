# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(val)
        dummy.next = head
        curr = dummy
        while curr.next :
            if curr.next.val == val:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
                del temp
            else:
                curr = curr.next
        return dummy.next
