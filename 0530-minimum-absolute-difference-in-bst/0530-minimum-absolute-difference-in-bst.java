/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

import java.lang.Math;

class Solution {
    public int getMinimumDifference(TreeNode root) {
        // General idea: inorder traversal and track minimum difference between two consecutive nodes
        List<TreeNode> nodes = new ArrayList<TreeNode>();
        inorder_helper(root, nodes);
        int diff = Integer.MAX_VALUE;
        for (int i = 1; i < nodes.size(); i++) {
            int current_diff = Math.abs(nodes.get(i).val - nodes.get(i-1).val);
            if (current_diff < diff) {
                diff = current_diff;
            }
        }
        return diff;
    }

    public void inorder_helper(TreeNode root, List<TreeNode> nodes) {
        if (root == null) {
            return;
        }
        inorder_helper(root.left, nodes);
        nodes.add(root);
        inorder_helper(root.right, nodes);
    }
}