# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        output = 0

        def dfs(node):
            nonlocal output
            if not node: return 0
            left_tree_height = dfs(node.left)
            right_tree_height = dfs(node.right)

            output = max(output, left_tree_height + right_tree_height)
            return max(left_tree_height, right_tree_height) + 1

        dfs(root)
        return output
    
    