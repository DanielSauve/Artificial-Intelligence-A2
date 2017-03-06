import random


class Focus:
    def __init__(self):
        self.board = [[None, None, "o", "o", "o", "o", None, None],
                      [None, "r", "r", "g", "g", "r", "r", None],
                      ["o", "g", "g", "r", "r", "g", "g", "o"],
                      ["o", "r", "r", "g", "g", "r", "r", "o"],
                      ["o", "g", "g", "r", "r", "g", "g", "o"],
                      ["o", "r", "r", "g", "g", "r", "r", "o"],
                      [None, "g", "g", "r", "r", "g", "g", None],
                      [None, None, "o", "o", "o", "o", None, None]]
        self.generate_board()

    def __str__(self):
        ret = ""
        for row in self.board:
            for item in row:
                if item:
                    ret += item + ", "
                else:
                    ret += " , "
            ret += "\n"
        return ret

    def generate_board(self):
        r, g, i, j = 18, 18, 1, 1
        while r and g:
            rand = random.random()
            if rand > 0.5:
                self.board[i][j] = "r"
                r -= 1
            else:
                self.board[i][j] = "g"
                g -= 1
            if j == 6:
                j = 1
                i += 1
            else:
                j += 1
        while r:
            self.board[i][j] = "r"
            if j == 6:
                j = 1
                i += 1
            else:
                j += 1
            r -= 1
        while g:
            self.board[i][j] = "g"
            if j == 6:
                j = 1
                i += 1
            else:
                j += 1
            g -= 1


focus = Focus()
print(focus)
