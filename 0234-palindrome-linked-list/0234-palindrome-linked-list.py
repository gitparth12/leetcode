# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        return self.recursion(head)
        
    def make_list(self, head: Optional[ListNode]) -> bool:
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
    

    def recursion(self, head: Optional[ListNode]) -> bool:
        self.curr = head
        return self.solve(head)

    def solve(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        ans = self.solve(head.next) and head.val == self.curr.val
        self.curr = self.curr.next
        return ans
