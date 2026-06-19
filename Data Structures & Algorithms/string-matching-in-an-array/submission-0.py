class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        words.sort(key = len)
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result