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
        self.r = 18
        self.g = 18

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

    def generate_moves(self, player):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                item = self.board[row][col]
                if item:
                    if item[0] == player:
                        for move in self.moves_for_piece(row, col, len(item)):
                            moves.append(move)
        return moves

    def moves_for_piece(self, row, col, height):
        moves = []
        if height > 1:
            for move in self.moves_for_piece(row, col, height - 1):
                (_, [mr, mc], _) = move
                try:
                    if self.board[mr + 1][mc] is not None and ([row, col], [mr + 1, mc], height) not in moves:
                        moves.append(([row, col], [mr + 1, mc], height))
                except IndexError:
                    pass
                try:
                    if self.board[mr - 1][mc] is not None and ([row, col], [mr - 1, mc], height) not in moves:
                        moves.append(([row, col], [mr - 1, mc], height))
                except IndexError:
                    pass
                try:
                    if self.board[mr][mc + 1] is not None and ([row, col], [mr, mc + 1], height) not in moves:
                        moves.append(([row, col], [mr, mc + 1], height))
                except IndexError:
                    pass
                try:
                    if self.board[mr][mc - 1] is not None and ([row, col], [mr, mc - 1], height) not in moves:
                        moves.append(([row, col], [mr, mc - 1], height))
                except IndexError:
                    pass
                moves.append(move)
                moves.append(([row, col], [mr, mc], height))
        else:
            try:
                if self.board[row + 1][col] is not None:
                    moves.append(([row, col], [row + 1, col], height))
            except IndexError:
                pass
            try:
                if self.board[row - 1][col] is not None:
                    moves.append(([row, col], [row - 1, col], height))
            except IndexError:
                pass
            try:
                if self.board[row][col + 1] is not None:
                    moves.append(([row, col], [row, col + 1], height))
            except IndexError:
                pass
            try:
                if self.board[row][col - 1] is not None:
                    moves.append(([row, col], [row, col - 1], height))
            except IndexError:
                pass
        return moves

    def make_move(self, move):
        ([rs, cs], [re, ce], height) = move
        start = self.board[rs][cs][0:height]
        self.board[rs][cs] = self.board[rs][cs][height:]
        end = self.board[re][ce]
        final = (start + end)[0:5]
        gone = (start + end)[5:]
        for char in gone:
            if char == "r":
                self.r -= 1
            elif char == "g":
                self.g -= 1
        self.board[re][ce] = final

    def tower_height(self, player):
        height = 0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                item = self.board[row][col]
                if item:
                    if item[0] == player:
                        height += len(item)
        return height

    def pieces_gone(self, player):
        if player == "r":
            return self.g
        return self.r


focus = Focus()
print(focus)
print(focus.generate_moves("r"))
focus.make_move(focus.generate_moves("r")[0])
focus.make_move(focus.generate_moves("g")[0])
print(focus)
