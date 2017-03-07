from Focus import Focus
import sys
import copy


class AlphaBeta:
    def __init__(self, piece, opponents, focus: Focus, max_depth):
        self.piece = piece
        self.opponents = opponents
        self.focus = focus
        self.max_depth = max_depth

    def start(self):
        alpha = -sys.maxsize
        beta = sys.maxsize
        moves = self.focus.generate_moves(self.piece)
        index, i = 0, 0
        if len(moves) == 0:
            return
        for i in range(len(moves)):
            move = moves[i]
            focus = copy.deepcopy(self.focus)
            focus.make_move(move)
            temp = self.alpha_beta(alpha, beta, focus, 1)
            if temp > alpha:
                alpha = temp
                index = i
        self.focus.make_move(moves[index])

    def alpha_beta(self, alpha, beta, focus, depth):
        if focus.game_end() == self.piece:
            return 100
        elif focus.game_end() == self.opponents:
            return -100
        if depth == self.max_depth:
            if self.piece == 'r':
                return focus.tower_height(self.piece)
            return focus.pieces_gone(self.piece)
        if depth % 2 == 0:
            moves = focus.generate_moves(self.piece)
            for move in moves:
                state = copy.deepcopy(focus)
                state.make_move(move)
                alpha = max(alpha, self.alpha_beta(alpha, beta, state, depth + 1))
                if beta <= alpha:
                    break
            return alpha
        else:
            moves = focus.generate_moves(self.opponents)
            for move in moves:
                state = copy.deepcopy(focus)
                state.make_move(move)
                beta = min(beta, self.alpha_beta(alpha, beta, state, depth + 1))
                if beta <= alpha:
                    break
            return beta


if __name__ == "__main__":
    focus = Focus()
    red = AlphaBeta("r", "g", focus, 4)
    green = AlphaBeta("g", "r", focus, 4)
    print(focus)
    while not focus.game_end():
        red.start()
        print("red", focus, sep="\n")
        if focus.game_end():
            break
        green.start()
        print("green", focus, sep="\n")
    print(focus.game_end() + " has won")
