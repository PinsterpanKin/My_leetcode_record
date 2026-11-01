class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build a trie from the list of words
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True  

        rows, cols = len(board), len(board[0])
        result = set()
        visited = [[False] * cols for _ in range(rows)]

        def backtrack(r, c, node, path):
            if '#' in node:
                result.add(path)  

            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                return

            char = board[r][c]
            if char not in node:
                return

            visited[r][c] = True
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                backtrack(r + dr, c + dc, node[char], path + char)
            visited[r][c] = False

        for r in range(rows):
            for c in range(cols):
                backtrack(r, c, trie, "")

        return list(result)