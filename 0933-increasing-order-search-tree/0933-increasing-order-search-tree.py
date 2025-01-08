# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.inorderHelper(root, nodes)
        for i, node in enumerate(nodes[:-1]):
            node.left = None
            node.right = nodes[i+1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]
    
    def inorderHelper(self, root: TreeNode, nodes: list) -> None:
        if root.left:
            self.inorderHelper(root.left, nodes)
        nodes.append(root)
        if root.right:
            self.inorderHelper(root.right, nodes)
        