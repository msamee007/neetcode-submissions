# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        p=None
        curr=head
        try:
            while curr.next is not None:
                n=curr.next
                curr.next=p
                p=curr
                curr=n
        except: 
            return head
        head=curr
        curr.next=p
        return head
