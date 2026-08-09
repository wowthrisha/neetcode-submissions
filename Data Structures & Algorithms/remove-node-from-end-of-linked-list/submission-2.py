# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1.dummy
        dummy=ListNode()
        dummy.next=head
        #2.gap 
        fast,slow=dummy,dummy
        for _ in range(n):
            fast=fast.next
        if not fast:
            return 
        while fast.next:
            fast=fast.next
            slow=slow.next
        
       
        slow.next=slow.next.next
        return dummy.next

