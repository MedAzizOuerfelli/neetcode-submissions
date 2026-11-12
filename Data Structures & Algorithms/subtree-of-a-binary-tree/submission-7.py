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
        def kmp(text, pattern):
            if not pattern:
                return True
            # Build LPS array
            n, m = len(text), len(pattern)
            LPS = [-1] * m
            j = -1
            for i in range(1, m):
                while pattern[i] != pattern[j + 1] and j != - 1  :
                    j = LPS[j]
                if  pattern[i] == pattern[j + 1]:
                    j += 1
                LPS[i] = j

            j = -1
            for i in range(n):
                while  text[i] != pattern[j + 1] and j != -1:
                    j = LPS[j]
                if  text[i] == pattern[j + 1]:
                    j += 1
                    if j == m - 1:
                        return True
            return False
            
        return kmp(r, subR)