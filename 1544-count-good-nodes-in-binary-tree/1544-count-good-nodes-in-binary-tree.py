# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Return number of good nodes in tree
        def dfs(root: TreeNode, largest: int) -> int:
            if not root:
                return 0

            res = 1 if root.val >= largest else 0
            largest = max(largest, root.val)
            return res + dfs(root.left, largest) + dfs(root.right, largest)

        return dfs(root, root.val)


# DFS from the root, keeping track of the maximum encountered on the current path
# Return number of good nodes in subtree
