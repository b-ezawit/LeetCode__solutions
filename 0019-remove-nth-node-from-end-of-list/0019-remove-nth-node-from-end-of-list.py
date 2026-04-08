# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size +=  1
        
        curr = head
        diff = size - n
        for _ in range(diff-1):
            if curr:
                curr = curr.next
        if diff == 0:
            head = head.next
        else:
            if curr.next:
                curr.next = curr.next.next
        return head
        