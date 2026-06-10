# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while curr.next:
            temp=curr.next
            g=gcd(curr.val,temp.val)
            n=ListNode(g)
            curr.next=n
            n.next=temp
            curr=temp
        return head