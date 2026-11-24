class TicTacToe:  
    def __init__(self):  
        self.board = [[' ']*3 for _ in range(3)]  

    def is_win(self, p):  
        b = self.board
        lines = b + list(zip(*b)) + [[b[i][i] for i in range(3)], [b[i][2-i] for i in range(3)]]
        return any(all(c == p for c in line) for line in lines)

    def dfs(self, p):  
        if self.is_win('X'): return 1  
        if self.is_win('O'): return -1  
        if not any(' ' in r for r in self.board): return 0  
        
        scores = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = p
                    scores.append(self.dfs('O' if p == 'X' else 'X'))
                    self.board[i][j] = ' '
        return max(scores) if p == 'X' else min(scores)

    def play(self):  
        p = 'X'
        while not (self.is_win('X') or self.is_win('O') or not any(' ' in r for r in self.board)):  
            for r in self.board: print(' | '.join(r) + '\n-----')
            if p == 'X':  
                moves = []
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == ' ':
                            self.board[i][j] = 'X'
                            moves.append((self.dfs('O'), i, j))
                            self.board[i][j] = ' '
                _, r, c = max(moves)
                self.board[r][c] = 'X'
            else:  
                while True:
                    try:
                        r, c = map(int, input("Row Col (e.g. 0 0): ").split())
                        if self.board[r][c] == ' ': self.board[r][c] = 'O'; break
                    except: print("Invalid!")
            p = 'O' if p == 'X' else 'X'  
        
        for r in self.board: print(' | '.join(r))
        print("X wins!" if self.is_win('X') else "O wins!" if self.is_win('O') else "Draw!")

if __name__ == '__main__':  
    TicTacToe().play()