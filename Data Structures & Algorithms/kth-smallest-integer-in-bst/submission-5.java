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
    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> s = new ArrayDeque<>();
        int counter = 0;
        TreeNode current_node = root;

        while (true) {
            while (current_node != null) {
                s.push(current_node);
                current_node = current_node.left;
            }
            current_node = s.pop();
            counter++;
            if (counter == k) return current_node.val;
            current_node = current_node.right;
        }
    }
}
