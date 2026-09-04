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

class Solution {
    private int max_value = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        max_value = Integer.MIN_VALUE;
        maxSubPathSum(root);
        return max_value;
    }

    public int maxSubPathSum(TreeNode root) {
        if (root == null) return 0;
        int left_value = Math.max(maxSubPathSum(root.left), 0);
        int right_value = Math.max(maxSubPathSum(root.right), 0);
        max_value = Math.max(max_value, Math.max(left_value + right_value + root.val, root.val));
        return Math.max(left_value, right_value) + root.val;
    }
}
