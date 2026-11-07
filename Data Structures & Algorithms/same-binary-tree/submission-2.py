# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and p or not p and q:
            return False
        if not q and not p:
            return True
        q1 = deque([q])
        q2 = deque([p])
        while q1 and q2:
            nodeP = q1.popleft()
            nodeQ = q2.popleft()
            if nodeP.val != nodeQ.val:
                return False
            if nodeP.right and nodeQ.right:
                q1.append(nodeQ.right)
                q2.append(nodeP.right)
            if nodeP.left and nodeQ.left:
                q1.append(nodeQ.left)
                q2.append(nodeP.left)
            if not nodeP.left and nodeQ.left or not nodeQ.left and nodeP.left:
                return False
            if not nodeP.right and nodeQ.right or not nodeQ.right and nodeP.right:
                return False
        return True
            