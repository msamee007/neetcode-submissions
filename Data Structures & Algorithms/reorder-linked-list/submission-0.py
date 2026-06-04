# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:      # CHANGED
            return

        curr = head
        i = 0
        while curr is not None:
            i += 1
            curr = curr.next

        curr = head
        j = 1

        while j < (i + 1) // 2:           # CHANGED
            curr = curr.next
            j += 1

        l = curr.next                     # CHANGED
        curr.next = None                  # CHANGED

        prev = None
        while l is not None:
            temp = l.next
            l.next = prev
            prev = l
            l = temp

        l1 = head
        l2 = prev

        while l1 is not None and l2 is not None:   # CHANGED
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2

        return