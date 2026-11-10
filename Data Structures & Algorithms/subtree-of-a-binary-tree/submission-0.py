# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return False
            if sameTree(node, subRoot):
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right

        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)
            return left and right
        return dfs(root)