class MySolution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        used = [[0] * len(board[0]) for _ in range(len(board))]

        def match(used, word, row, col):
            if len(word) == 1:
                return True
            used[row][col] = 1

            res = \
            (match(used, word[1:], row+1, col) if \
            row+1 < len(board) and not used[row+1][col] and board[row+1][col] == word[1] else False) or \
            (match(used, word[1:], row-1, col) if \
            row-1 > -1 and not used[row-1][col] and board[row-1][col] == word[1] else False) or \
            (match(used, word[1:], row, col+1) if \
            col+1 < len(board[0]) and not used[row][col+1] and board[row][col+1] == word[1] else False) or \
            (match(used, word[1:], row, col-1) if \
            col-1 > -1 and not used[row][col-1] and board[row][col-1] == word[1] else False)

            used[row][col] = 0
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if match(used, word, i, j):
                        return True

        return False

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False