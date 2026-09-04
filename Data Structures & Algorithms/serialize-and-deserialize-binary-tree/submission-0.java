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

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder output = new StringBuilder();
        serializeHelper(root, output);
        return output.toString();
    }

    private void serializeHelper(TreeNode node, StringBuilder output) {
        if (node == null) {
            output.append("N,");
        } else {
            output.append(node.val).append(",");
            serializeHelper(node.left, output);
            serializeHelper(node.right, output);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Deque<String> tokens = new ArrayDeque<>(java.util.Arrays.asList(data.split(",")));
        return deserializeHelper(tokens);
    }

    private TreeNode deserializeHelper(Deque<String> tokens) {
        String val = tokens.poll();
        if (val == null || val.equals("N")) return null;

        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = deserializeHelper(tokens);
        node.right = deserializeHelper(tokens);
        return node;
    }
}
