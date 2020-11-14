from .constants import WHITE, BLACK, SQUARE_SIZE, X
import pygame


class Piece:
    PADDING = 30  # distancia da peça à borda da grelha
    OUTLINE = 10  # grossura da bola

    def __init__(self, row, col, turn=None):
        self.row = row      # posição numa linha da peça
        self.col = col      # posição numa coluna da peça
        self.turn = turn    # mostra a que jogador a peça pertence
        self.x = 0          # posição exata em que a peça vai ser desenhada na cordenada x
        self.y = 0          # posição exata em que a peça vai ser desenhada na cordenada y
        self.calc_pos()     # calcula as posições das cordenadas em que a peça vai ser desenhada

    # calcula as posições das cordenadas em que a peça vai ser desenhada
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # desenha as peças no ecrã

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING

        # vê a quem pertence a peça e desenha a peça correspondente
        if self.turn == 2:
            # desenha um circulo no ecrã
            pygame.draw.circle(win, BLACK, (self.x, self.y),
                               radius + self.OUTLINE)
            pygame.draw.circle(win, WHITE, (self.x, self.y), radius)

        else:
            # desenha um X no ecrã
            win.blit(X, (self.x - X.get_width()//2, self.y - X.get_height()//2))

    # coloca o jogador a que a peça pertence na lista que representa e grelha do jogo para o pyhton usar
    def __repr__(self):
        return self.turn
