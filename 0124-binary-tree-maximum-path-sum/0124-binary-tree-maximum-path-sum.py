# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res

            if not root:
                return 0
            
            # If any returned value is -ve, we just don't take that subtree in our path and cap at 0
            left, right = max(dfs(root.left), 0), max(dfs(root.right), 0)
            path_through = root.val + left + right
            res = max(res, path_through)

            return root.val + max(left, right, 0)

        return max(dfs(root), res)


# DFS:
#   Maintain a global result, which is max path sum we saw until now that included the nodes we went through
#   Return value is max downward path, which is node.val + max(path at left, path at right)
#   Use this return value to compute the path through the parent node and update result (if greater)