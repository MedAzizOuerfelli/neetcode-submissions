# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fct(node):
            if not node:
                return 
            left = fct(node.left)
            right = fct(node.right)
            node.left, node.right = node.right, node.left
        fct(root)
        return root