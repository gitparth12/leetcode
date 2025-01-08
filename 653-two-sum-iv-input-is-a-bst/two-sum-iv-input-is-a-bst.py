# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ## store required values by getting k - num for each num in bst
        nums = []
        hashset = set()
        self.inorderHelper(root, nums)
        for num in nums:
            if k-num in hashset:
                return True
            hashset.add(num)
        return False

        
    def inorderHelper(self, root: TreeNode, nums: list):
        if root.left:
            self.inorderHelper(root.left, nums)
        nums.append(root.val)
        if root.right:
            self.inorderHelper(root.right, nums)