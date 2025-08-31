# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
                return TreeNode(val)
        def search(node: Optional[TreeNode], val: int):
            if node.val < val:
                if not node.right:
                    return node
                return search(node.right, val)
            elif node.val > val:
                if not node.left:
                    return node
                return search(node.left, val)

        last = search(root, val)
        if last.val < val:
            last.right = TreeNode(val)
        else:
            last.left = TreeNode(val)
        return root