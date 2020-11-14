from AI.minimax import minimaxAB
from AI.Amedio import minimaxMed
from game.constants import DARKER_GREY, DARK_RED, ICON, MICRO_BH, MICRO_BW, RED, SMALL_BH, SMALL_BW, SQUARE_SIZE, BLACK, BLUEISH_PURPLE, BUTTON_HEIGHT, BUTTON_WIDTH, WHITE, WIDTH, HEIGHT, IMG, GREY, DARK_GREY
import pygame
import os
import pyautogui
from AI.Apodre import positi
from game.game import Game
from tkinter import *
import time

screen_width, screen_height = pyautogui.size()  # vê o tamanho do ecrã
# descobre a posição onde tem de criar
pos_x = screen_width / 2 - WIDTH / 2
# a janela para que a mesma fique no meio do ecrã
pos_y = screen_height - HEIGHT
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (
    pos_x, pos_y)   # posiciona a janela no meio do ecrã
os.environ['SDL_VIDEO_CENTERED'] = '0'
FPS = 60    # define a velocidade máxima a q o jogo pode correr
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # cria a janela do jogo
pygame.display.set_caption('Tic-Tac-Toe')       # muda o nome da aplicação
pygame.display.set_icon(ICON)
clock = pygame.time.Clock()  # cria a velocidade do jogo
game = Game(WIN)


def popUpMsg(message, win, text):
    global root
    root = Tk()
    root.title('winner')
    x, y = win.get_size()
    root.geometry(f'+{x+345}+{y-20}')
    m = message
    m += '\n'
    w = Label(root, text=m, width=30, height=5)
    w.pack()
    Button(root, text=text,
           command=root.destroy, width=10).place(x=20, y=48)
    Button(root, text='main menu',
           command=back, width=10).place(x=115, y=48)

    mainloop()


def back():
    root.destroy()
    game.reset()
    main_menu()


def getRowColFromMouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def game_loop(AI=False, dif=1):
    try:
        run = True
        pause = False

        # corre enquanto o jogo estiver aberto
        while run:
            clock.tick(FPS)  # define a velocidade do jogo

            # vê se alguém ganhou e cria uma janela a dizer o jogador que ganhou
            if game.winner():
                if game.Winner == 2:
                    popUpMsg('Circle Won!', WIN, 'restart')

                else:
                    popUpMsg('Cross Won!', WIN, 'restart')

                game.reset()

            elif game.board.board[1].count(0) + game.board.board[0].count(0) + game.board.board[2].count(0) == 0:
                popUpMsg('It\'s a tie', WIN, 'restart')
                game.reset()

            if AI and game.turn == 2 and dif == 1:
                row, col = positi(0, 1, 0)
                game.create(row, col, AI)

            elif AI and game.turn == 2 and dif == 2:
                eval, row, col = minimaxMed(4, True)
                game.create(row, col, AI)

            elif AI and game.turn == 2 and dif == 3:
                eval, row, col = minimaxAB(0, -10, 10, True)
                game.create(row, col, AI)

            # observa eventos e guarda-os numa lista
            for event in pygame.event.get():  # for event in pygame.event.get():
                # se for um evento de fechar o programa para o while
                if event.type == pygame.QUIT:
                    run = False

                if not pause:
                    if not AI:
                        # se for um evento de clicar na tela cria uma peça de X ou O dependendo do jogador que selecionou
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            row, col = getRowColFromMouse(pos)
                            game.create(row, col)

                    if AI and game.turn == 1:
                        # se for um evento de clicar na tela cria uma peça de X ou O dependendo do jogador que selecionou
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            row, col = getRowColFromMouse(pos)
                            game.create(row, col, AI)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = not pause

            if pause:
                popUpMsg('Pause menu', WIN, 'continue')
                pause = not pause

            game.update()  # atualiza todos os objetos no ecrã

        pygame.quit()  # fecha o programa

    except:
        pygame.quit()  # fecha o programa


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(cd, cl, pos_x, pos_y, btw, bth, text, ct, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if pos_x + btw > mouse[0] > pos_x and pos_y + bth > mouse[1] > pos_y:
        pygame.draw.rect(
            WIN, cl, (pos_x, pos_y, btw, bth))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(
            WIN, cd, (pos_x, pos_y, btw, bth))

    smallText = pygame.font.SysFont("cambria", 15)
    textSurf, textRect = text_objects(text, smallText, ct)
    textRect.center = ((pos_x + (btw//2)),
                       (pos_y + (bth//2) - 2))
    WIN.blit(textSurf, textRect)


def quitGame():
    pygame.quit()


def change(action, isUp):
    if isUp:
        if action < 3:
            action += 1
            return action

        else:
            action = 1
            return action
    else:

        if action > 1:
            action -= 1
            return action

        else:
            action = 3
            return action


def main_menu():
    try:
        dif = 1
        intro = True
        pygame.font.init()

        while intro:
            predif = dif

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False

            WIN.blit(IMG, (WIDTH//1000, HEIGHT//510))
            largeText = pygame.font.SysFont('cambria', 30)
            TextSurf, TextRect = text_objects(
                "Welcome,", largeText, BLUEISH_PURPLE)
            TextRect.center = (WIDTH//2, HEIGHT//5)
            WIN.blit(TextSurf, TextRect)

            largeText2 = pygame.font.SysFont('cambria', 30)
            TextSurf2, TextRect2 = text_objects(
                "to Tic-Tac-Toe", largeText2, BLUEISH_PURPLE)
            TextRect2.center = (WIDTH//2, int(HEIGHT//3.5))
            WIN.blit(TextSurf2, TextRect2)

            button(DARK_GREY, GREY, WIDTH//2 - BUTTON_WIDTH//2, 200, BUTTON_WIDTH,
                   BUTTON_HEIGHT, 'Jogador vs Jogador', BLACK, game_loop)

            button(DARK_GREY, GREY, WIDTH//2 - BUTTON_WIDTH//2, 260, BUTTON_WIDTH,
                   BUTTON_HEIGHT, 'Jogador vs CPU', BLACK)

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if WIDTH//2 - BUTTON_WIDTH//2 + BUTTON_WIDTH > mouse[0] > WIDTH//2 - BUTTON_WIDTH//2 and 260 + BUTTON_HEIGHT > mouse[1] > 260:
                if click[0] == 1:
                    game_loop(True, dif)

            pygame.draw.rect(
                WIN, DARK_GREY, (WIDTH//2 - BUTTON_WIDTH//2, 320, BUTTON_WIDTH, BUTTON_HEIGHT))

            smallText = pygame.font.SysFont("cambria", 15)
            textSurf, textRect = text_objects(
                'dificuldade: ', smallText, BLACK)
            textRect.center = (((WIDTH//2 - BUTTON_WIDTH//2) + (60)),
                               330)
            WIN.blit(textSurf, textRect)

            smallText = pygame.font.SysFont("cambria", 15)
            textSurf, textRect = text_objects(
                str(dif), smallText, BLACK)
            textRect.center = (((WIDTH//2 - BUTTON_WIDTH//2) + (60)),
                               348)
            WIN.blit(textSurf, textRect)

            button(DARKER_GREY, GREY, WIDTH//2 + 45,
                   320, MICRO_BW, MICRO_BH, '/\\', WHITE)

            if WIDTH//2 + 35 + MICRO_BW > mouse[0] > WIDTH//2 + 35 and 320 + MICRO_BH > mouse[1] > 320:
                if click[0] == 1:
                    dif = change(dif, True)

            button(DARKER_GREY, GREY, WIDTH//2 + 45,
                   342, MICRO_BW, MICRO_BH, '\\/', WHITE)

            if WIDTH//2 + 35 + MICRO_BW > mouse[0] > WIDTH//2 + 35 and 342 + MICRO_BH > mouse[1] > 342:
                if click[0] == 1:
                    dif = change(dif, False)

            button(DARK_RED, RED, WIDTH//2 - SMALL_BW//2, 400, SMALL_BW, SMALL_BH,
                   'Quit', BLACK, quitGame)

            pygame.display.update()
            if dif != predif:
                time.sleep(0.5)

            clock.tick(15)

        pygame.quit()

    except:
        pygame.quit()


main_menu()