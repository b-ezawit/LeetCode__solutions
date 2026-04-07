# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        
        while head:
            head_next = head.next
            head.next = dummy
            dummy = head
            head = head_next
            
        head = dummy
        return head