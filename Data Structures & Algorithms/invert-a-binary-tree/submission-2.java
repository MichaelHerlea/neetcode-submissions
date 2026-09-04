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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        ArrayList<TreeNode> queue = new ArrayList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode current_node = queue.getFirst();
            queue.removeFirst();
            if (current_node.left == null && current_node.right == null) {
                continue;
            }
            else if (current_node.left == null) {
                queue.add(current_node.right);
                current_node.left = current_node.right;
                current_node.right = null;
            }
            else if (current_node.right == null){
                queue.add(current_node.left);
                current_node.right = current_node.left;
                current_node.left = null;
            }
            else {
                queue.add(current_node.left);
                queue.add(current_node.right);
                TreeNode temp = current_node.left;
                current_node.left = current_node.right;
                current_node.right = temp;
            }
        }

        return root;
    }
}
