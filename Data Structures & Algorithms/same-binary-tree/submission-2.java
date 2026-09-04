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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        ArrayList<Integer> p_tree_values = treeValues(p);
        ArrayList<Integer> q_tree_values = treeValues(q);

        while (!p_tree_values.isEmpty() && !q_tree_values.isEmpty()) {
            if (p_tree_values.getFirst() != q_tree_values.getFirst()) {
                return false;
            }
            p_tree_values.removeFirst();
            q_tree_values.removeFirst();
        }
        return p_tree_values.isEmpty() && q_tree_values.isEmpty();
    }

    public ArrayList<Integer> treeValues(TreeNode root) {
        ArrayList<Integer> values = new ArrayList<>();
        ArrayList<TreeNode> queue = new ArrayList<>();

        if (root == null) {
            return values;
        }

        values.add(root.val);
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode current_node = queue.getFirst();

            if (current_node.left == null) values.add(null);
            else {
                values.add(current_node.left.val);
                queue.add(current_node.left);
            }
            if (current_node.right == null) values.add(null);
            else {
                values.add(current_node.right.val);
                queue.add(current_node.right);
            }
            
            queue.removeFirst();
        }

        return values;
    }
}
