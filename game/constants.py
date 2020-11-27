import pygame

WIDTH, HEIGHT = 500, 500    # definir as dimenções da janela
ROWS, COLS = 3, 3           # definir as fimenções da grelha
SQUARE_SIZE = WIDTH//COLS   # definir o tamanho de cada quadrado da grelha

# definir as cores do jogo no formato RGB
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
DARK_GREY = (75, 75, 75)
DARKER_GREY = (25, 25, 25)
BLUEISH_PURPLE = (50, 50, 200)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
DARK_RED = (150, 0, 0)

WIDTH = 500
HEIGHT = 500
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 40
SMALL_BW = 50
SMALL_BH = 30
MICRO_BW = 30
MICRO_BH = 18

IMG = pygame.transform.scale(pygame.image.load(
    'assets/wall-murals-play-the-game-tic-tac-toe-with-red-and-black-sign.jpg.jpg'), (WIDTH, HEIGHT))

# importar a imagem do X para o jogo
X = pygame.transform.scale(pygame.image.load(
    'assets/fotoX.png'), (170, 160))

ICON = pygame.image.load('assets/images.png')

