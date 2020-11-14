import pygame
from .board import Board
from .piece import Piece
from AI.Apodre import rep_board1
from AI.minimax import rep_board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    # atualiza a grelha
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        for row in range(len(rep_board)):
            for col in range(len(rep_board[row])):
                rep_board1[row][col] = 1

        for row in range(len(rep_board)):
            for col in range(len(rep_board[row])):
                rep_board[row][col] = '.'

        self.Winner = None  # vê quem ganhou
        self.board = Board()
        self.turn = 1       # guarda o turno do jogador

    # volta a grelha ao estado original
    def reset(self):
        self._init()

    # função que cria a peça, no ecrã, do turno do jogador
    def create(self, row, col, AI=False):
        piece = self.board.add_piece(row, col, self.turn)
        if piece != 0:
            if AI:
                rep_board1[piece.row][piece.col] = 0

                if self.turn == 1:
                    rep_board[piece.row][piece.col] = 'X'

                elif self.turn == 2:
                    rep_board[piece.row][piece.col] = 'O'

            piece.draw(self.win)
            self.changeTurn()

    # função que determina de quem é o turno
    def changeTurn(self):
        if self.turn > 1:
            self.turn = 0

        self.turn += 1

    # função que vê se alguém ganhou
    def winner(self):

        for i in range(0, 3):
            if all(isinstance(j, Piece) for j in self.board.board[i]):
                if self.board.board[i][0].turn == self.board.board[i][1].turn == self.board.board[i][2].turn:
                    self.Winner = self.board.board[i][0].turn
                    return True
        for i in range(0, 3):
            if type(self.board.board[0][i]) == type(self.board.board[1][i]) == type(self.board.board[2][i]) == Piece:
                if self.board.board[0][i].turn == self.board.board[1][i].turn == self.board.board[2][i].turn:
                    self.Winner = self.board.board[0][i].turn
                    return True

        if type(self.board.board[0][0]) == type(self.board.board[1][1]) == type(self.board.board[2][2]) == Piece:
            if self.board.board[0][0].turn == self.board.board[1][1].turn == self.board.board[2][2].turn:
                self.Winner = self.board.board[0][0].turn
                return True

        if type(self.board.board[0][2]) == type(self.board.board[1][1]) == type(self.board.board[2][0]) == Piece:
            if self.board.board[0][2].turn == self.board.board[1][1].turn == self.board.board[2][0].turn:
                self.Winner = self.board.board[0][2].turn
                return True

        else:
            return None
