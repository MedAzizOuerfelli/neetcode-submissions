class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        lS1 = [0]*26
        for char in s1:
            lS1[ord("a") - ord(char)] += 1
        window = [0]*26
        for i in range(len(s1)):
            window[ord("a") - ord(s2[i])] += 1
        if window == lS1:
            return True
        left = 0
        for i in range(len(s1), len(s2)):
            window[ord("a") - ord(s2[left])] -= 1
            left += 1
            window[ord("a") - ord(s2[i])] += 1
            if window == lS1:
                return True
        return False

        