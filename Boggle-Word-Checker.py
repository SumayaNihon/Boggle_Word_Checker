
def find_word(board, word):
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    m = len(board)
    n = len(board[0]) if m > 0 else 0

    def dfs(idx, x, y):
        if idx == len(word):
            return True
        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == '*':
            return False
        if board[x][y] == word[idx]:
            original_char = board[x][y]
            board[x][y] = '*'
            for dx, dy in dir:
                if dfs(idx + 1, x + dx, y + dy):
                    board[x][y] = original_char
                    return True
            board[x][y] = original_char
        return False

    for x in range(m):
        for y in range(n):
            if dfs(0, x, y):
                return True

    return False







    