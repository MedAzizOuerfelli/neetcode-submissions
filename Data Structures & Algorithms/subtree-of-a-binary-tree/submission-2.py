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
            # Build LPS array
            lps = [0] * len(pattern)
            length = 0
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length > 0:
                    length = lps[length - 1]
                else:
                    i += 1

            # Search pattern in text
            i = j = 0

            while i < len(text):
                if text[i] == pattern[j]:
                    i += 1
                    j += 1

                    if j == len(pattern):
                        return True

                elif j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

            return False
            
        return kmp(r, subR)