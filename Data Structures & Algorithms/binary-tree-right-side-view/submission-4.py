# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        parent = [root]
        children = []
        output = []

        while parent:
            output.append(parent[0].val)
          
            for node in parent:
                if node.right: children.append(node.right)
                if node.left: children.append(node.left)

            parent = children
            children = []
        
        return output