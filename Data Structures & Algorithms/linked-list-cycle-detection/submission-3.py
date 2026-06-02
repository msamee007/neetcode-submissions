# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head==None:
            return False
        curr=head
        l=[]
        while curr.next is not None:
            if curr.next in l:
                return True
            l.append(curr)
            curr=curr.next
        return False