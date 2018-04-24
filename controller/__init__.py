from model import *  # imports model

import time


class Game:
    def __init__(self, size=5, board=None, white=HUMAN, black=AI(3)):
        self.board = Board(size) if board is None else board
        self.player_1: Player = self._init_player(Colors.WHITE, white)
        self.player_2: Player = self._init_player(Colors.BLACK, black)
        self.players = [self.player_1, self.player_2]

        self.stones = {i: FLAT for i in Colors}
        self.ptn = PTN()

    def _init_player(self, color, types) -> Player:
        name, depth = types
        if name == HUMAN[0]:
            return Player(self.board, color)
        else:
            return MinimaxAI(self.board, color, depth)

    def viz(self):
        return

    def _run(self, player, turn, input_fn=input):
        self.viz()
        t = time.time()
        if turn <= 1:
            m, c = player.pick_opposing_move(input_fn=input_fn)
            self.stones[c] = STONES
        else:
            m = player.pick_move(input_fn=input_fn)
            c = player.color
            if CAP in str(m):
                self.stones[c] = FLAT + STAND
        print(time.time() - t)
        player._do(m, c)
        self.ptn.append(m)
        return m

    def run(self):
        self.ptn.clear()
        turn = 1
        while True:
            for player in self.players:
                print(self.ptn)
                self._run(player, turn)
                w = self.board.winner(self.players, t=True)
                if w:
                    print(self.ptn)
                    self.viz()
                    print(w, "won!")
                    return
            turn += 1


class TextGame(Game):
    def viz(self):
        print(self.board)
