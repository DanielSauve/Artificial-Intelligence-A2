import random
import copy


class Focus:
    def __init__(self):
        self.board = [[None, None, "", "", "", "", None, None],
                      [None, "r", "r", "g", "g", "r", "r", None],
                      ["", "g", "g", "r", "r", "g", "g", ""],
                      ["", "r", "r", "g", "g", "r", "r", ""],
                      ["", "g", "g", "r", "r", "g", "g", ""],
                      ["", "r", "r", "g", "g", "r", "r", ""],
                      [None, "g", "g", "r", "r", "g", "g", None],
                      [None, None, "", "", "", "", None, None]]
        self.generate_board()
        self.r_count = 18
        self.g_count = 18
        self.r_height = 18
        self.g_height = 18

    def __str__(self):
        ret = ""
        for row in self.board:
            for item in row:
                if item is None:
                    ret += "x, "
                elif item:
                    ret += item + ", "
                else:
                    ret += " , "
            ret += "\n"
        return ret

    def tower_height(self, player):
        if player == 'r':
            return self.r_height - self.g_height
        return self.g_height - self.r_height

    def pieces_gone(self, player):
        if player == "r":
            return self.r_count - self.g_count
        return self.g_count - self.r_count

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

    def game_end(self):
        if self.g_count < 10:
            print("g_count", self.g_count)
            return 'r'
        if self.r_count < 10:
            print("r_count", self.r_count)
            return 'g'
        if self.g_height <= 0:
            print("g_height", self.g_height)
            return 'r'
        if self.r_height <= 0:
            print("r_height", self.r_height)
            return 'g'
        return ''

    def generate_moves(self, player):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                item = self.board[row][col]
                if item:
                    if item[0] == player:
                        generated = self.moves_for_piece(row, col, len(item))
                        for move in generated:
                            moves.append(move)
        return moves

    def moves_for_piece(self, row, col, height):
        moves = []
        for i in range(height):
            try:
                if self.board[row + i + 1][col] is not None:
                    moves.append(([row, col], [row + i + 1, col], height))
            except IndexError:
                pass
            try:
                if self.board[row - i - 1][col] is not None:
                    moves.append(([row, col], [row - i - 1, col], height))
            except IndexError:
                pass
            try:
                if self.board[row][col + i + 1] is not None:
                    moves.append(([row, col], [row, col + i + 1], height))
            except IndexError:
                pass
            try:
                if self.board[row][col - i - 1] is not None:
                    moves.append(([row, col], [row, col - i - 1], height))
            except IndexError:
                pass

        if height > 1:
            sub_stack = self.moves_for_piece(row, col, height - 1)
            for move in sub_stack:
                moves.append(move)

        return moves

    def make_move(self, move):
        ([rs, cs], [re, ce], height) = move
        start = self.board[rs][cs][0:height]
        self.board[rs][cs] = self.board[rs][cs][height:]
        end = self.board[re][ce]
        if end:
            if end[0] == 'r':
                self.r_height -= len(end)
            elif end[0] == 'g':
                self.g_height -= len(end)
        final = (start + end)[0:5]
        if start[0] == 'r':
            self.r_height -= len(start)
            self.r_height += len(final)
        elif start[0] == 'g':
            self.g_height -= len(start)
            self.g_height += len(final)
        gone = (start + end)[5:]
        for char in gone:
            if char == "r":
                self.r_count -= 1
            elif char == "g":
                self.g_count -= 1
        self.board[re][ce] = final

if __name__ == "__main__":
    focus = Focus()
    print(focus)
    print(focus.generate_moves("r"))
    focus.make_move(focus.generate_moves("r")[0])
    focus.make_move(focus.generate_moves("g")[0])
    print(focus)
