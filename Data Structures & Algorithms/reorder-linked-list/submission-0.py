# Definition for singly-linked list.
# class ListNode:
from os import preadv
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        #find mid
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        sec=slow.next
        slow.next=None
        prev,cur=None,sec
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        l1=head
        l2=prev
        while l2 :
            t1=l1.next
            t2=l2.next
            l1.next=l2
            l2.next=t1
            l1=t1
            l2=t2

            
      


        
