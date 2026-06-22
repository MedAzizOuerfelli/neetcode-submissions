class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        pgcd = math.gcd(n1, n2)
        if n1 < n2:
            prefix = str1[:pgcd]
        else:
            prefix = str2[:pgcd]
        for i in range(0,n1, pgcd):
            if str1[i:i+pgcd] != prefix:
                return ""
        for i in range(0,n2, pgcd):
            if str2[i:i+pgcd] != prefix:
                return ""
        return prefix
        
