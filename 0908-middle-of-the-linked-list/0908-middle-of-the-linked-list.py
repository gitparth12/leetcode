# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Two passes through linked list, i don't like
        # size = 0
        # current = head
        # while current:
        #     current = current.next
        #     size += 1

        # mid = size // 2
        
        # current = head
        # for i in range(mid):
        #     current = current.next

        # return current
        
        ## Single pass using slow, fast pointers
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next:
            fast = fast.next
            slow = slow.next
        
        return slow
