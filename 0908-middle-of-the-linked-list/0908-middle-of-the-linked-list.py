# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        current = head
        while current:
            current = current.next
            size += 1

        mid = size // 2
        # if size % 2 == 0:
        #     mid += 1
        
        current = head
        for i in range(mid):
            current = current.next

        return current