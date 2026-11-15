"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        def dfs(n):
            if  n in d:
                return d[n] 
            root = Node(n.val)
            d[n] = root
            for nei in n.neighbors:
                root.neighbors.append(dfs(nei))
            return root
        return dfs(node) if node else None
