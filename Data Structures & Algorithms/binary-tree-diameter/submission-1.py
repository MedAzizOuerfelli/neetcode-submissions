# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def fct(node):
            nonlocal res
            if not node:
                return 0
            left = fct(node.left)
            right = fct(node.right)
            res =  max(res, left + right)
            return 1 + max(left, right)
        fct(root)
        return res