import pygame
from .constants import BLACK, ROWS, WHITE, WIDTH, HEIGHT, COLS, SQUARE_SIZE
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.creatBoard()

    # desenha a grelha no ecrã
    def drawGrid(self, win):
        win.fill(WHITE)
        for x in range(WIDTH):
            for y in range(HEIGHT):
                rect = pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE,
                                   SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(win, BLACK, rect, 3)

    # vê se há uma peça no local onde o jogador clicou
    def add_piece(self, row, col, turn):
        piece = Piece(row, col, turn)

        if self.board[piece.row][piece.col] != 0:
            return 0
        else:
            self.board[piece.row][piece.col] = piece
            return piece

    # cria a grelha num formato que o python consegue perceber
    def creatBoard(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    # atualiza o ecrã e desenha as peças que existem
    def draw(self, win):
        self.drawGrid(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
