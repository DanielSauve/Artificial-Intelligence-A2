from Focus import Focus
import sys
import copy
import random


class AlphaBeta:
    def __init__(self, piece: str, opponents: str, board: Focus, max_depth: int):
        self.piece = piece
        self.opponents = opponents
        self.focus = board
        self.max_depth = max_depth

    def start(self):
        alpha = -sys.maxsize
        beta = sys.maxsize
        moves = self.focus.generate_moves(self.piece)
        possible_moves = []
        for move in moves:
            temp_state = copy.deepcopy(self.focus)
            temp_state.make_move(move)
            if temp_state.game_end() == self.piece:
                (start, end, height) = move
                print("From: ", start, " To: ", end, " Height: ", height)
                self.focus.make_move(move)
                return
            temp = self.alpha_beta(alpha, beta, temp_state, 1)
            if temp > alpha:
                alpha = temp
                possible_moves = [move]
            if temp == alpha:
                possible_moves.append(move)
        random.shuffle(possible_moves)
        self.focus.make_move(possible_moves[0])
        (start, end, height) = possible_moves[0]
        print("From: ", start, " To: ", end, " Height: ", height)

    def alpha_beta(self, alpha, beta, board, depth):
        if board.game_end() == self.piece:
            return sys.maxsize
        elif board.game_end() == self.opponents:
            return -sys.maxsize
        if depth == self.max_depth:
            if self.piece == 'r':
                return board.tower_height(self.piece)
            return board.pieces_gone(self.piece)
        if depth % 2 == 0:
            moves = board.generate_moves(self.piece)
            for move in moves:
                state = copy.deepcopy(board)
                state.make_move(move)
                alpha = max(alpha, self.alpha_beta(alpha, beta, state, depth + 1))
                if beta <= alpha:
                    break
            return alpha
        else:
            moves = board.generate_moves(self.opponents)
            for move in moves:
                state = copy.deepcopy(board)
                state.make_move(move)
                beta = min(beta, self.alpha_beta(alpha, beta, state, depth + 1))
                if beta <= alpha:
                    break
            return beta


if __name__ == "__main__":
    depth_i = int(input("What depth would you like to search to: "))
    focus = Focus()
    red = AlphaBeta("r", "g", focus, depth_i)
    green = AlphaBeta("g", "r", focus, depth_i)
    print(focus)
    while not focus.game_end():
        red.start()
        print("red", focus, sep="\n")
        focus.update()
        if focus.game_end():
            break
        green.start()
        print("green", focus, sep="\n")
        focus.update()
    print(focus.game_end() + " has won")
