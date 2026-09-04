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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();

        List<List<Integer>> output = new ArrayList<>();
        ArrayList<TreeNode> q = new ArrayList<>();
        q.add(root);

        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode current_node = q.removeFirst();
                level.add(current_node.val);
                if (current_node.left != null) q.add(current_node.left);
                if (current_node.right != null) q.add(current_node.right);
            }
            output.add(level);
        }
        return output;
    }
}
