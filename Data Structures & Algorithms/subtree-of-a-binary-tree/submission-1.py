# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(n):
            res = []

            def dfs(node):
                if node is None:
                    res.append("$#")
                    return

                res.append("$")
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

            dfs(n)
            return "".join(res)
        subR = serialize(subRoot)
        r = serialize(root)
        if subR in r:
            return True
        return False