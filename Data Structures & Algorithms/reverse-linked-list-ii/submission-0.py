# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next==None or left==right:
            return head
        if left!=1:
            curr=head
            i=1
            prev=curr
            while i!=left:
                prev=curr
                curr=curr.next
                i+=1
            x=curr
            p=None
            while left<=right:
                t=curr.next
                curr.next=p
                p=curr
                curr=t
                left+=1
            prev.next=p
            x.next=curr
            return head
        else:
            curr=head
            p=None
            prev=head
            while left<=right:
                t=curr.next
                curr.next=p
                p=curr
                curr=t
                left+=1
            head=p
            if p.next!=None:
                prev.next=curr

            return head