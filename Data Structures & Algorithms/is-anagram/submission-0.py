class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS = Counter(s)
        for char in t:
            if char not in mapS:
                return False
            mapS[char] -= 1
            if mapS[char] == 0:
                del mapS[char]
        return True
            