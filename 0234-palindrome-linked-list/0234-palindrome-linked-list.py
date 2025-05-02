# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # can't think of O(n) time and O(1) space
        # O(n) time and O(1) space attempt

        # translate to array
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        # two pointer approach
        if len(arr) % 2 == 0:
            return arr[:len(arr)//2] == list(reversed(arr[len(arr)//2:]))
        return arr[:len(arr)//2] == list(reversed(arr[len(arr)//2+1:]))
        