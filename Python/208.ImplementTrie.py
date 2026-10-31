class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True  # Mark the end of a word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node  # Check if it's the end of a word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

#My solution: not an efficient structure
class MyTrie:
    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        self.trie.append(word)

    def search(self, word: str) -> bool:
        return word in self.trie

    def startsWith(self, prefix: str) -> bool:
        for word in self.trie:
            if word.startswith(prefix):
                return True
        return False