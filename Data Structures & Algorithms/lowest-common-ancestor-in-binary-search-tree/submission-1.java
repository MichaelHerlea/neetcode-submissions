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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root.val == p.val || root.val == q.val) return root;
        int lower_bound = Math.min(p.val, q.val);
        int upper_bound = Math.max(p.val, q.val);

        ArrayList<TreeNode> queue = new ArrayList<>();

        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode current_node = queue.getFirst();

            if (current_node.val == lower_bound || current_node.val == upper_bound) return current_node;
            if (current_node.val > lower_bound && current_node.val < upper_bound) return current_node;

            if (current_node.left != null) queue.add(current_node.left);
            if (current_node.right != null) queue.add(current_node.right);

            queue.removeFirst();
        }

        return null;
    }
}
