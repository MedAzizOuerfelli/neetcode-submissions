class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(x, l, r):
            while l < r:
                if x[l] != x[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        result = []
        def dfs(i, cur):
            if i == len(s):
                result.append(cur[:])
                return 
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    cur.append(s[i: j+1])
                    dfs(j + 1, cur)
                    cur.pop()
        dfs(0, [])
        return result
            