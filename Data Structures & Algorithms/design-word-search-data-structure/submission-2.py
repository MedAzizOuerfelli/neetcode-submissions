class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_word
            c = word[index]
            if c == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                node = node.children[c]
                return dfs(node, index + 1)
        return dfs(self.root, 0)
