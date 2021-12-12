import pygame

from player import Player, RandomBot
from tictactoe import run


class Context:
    margin = 7
    size_block = 125

    def __init__(self, n):
        self.n = n
        self.top_panel_size_y = 100
        self.w = self.size_block * n + self.margin * 4
        self.h = self.w + self.top_panel_size_y
        self.ttt_list = None
        self.screen = None
        self.clock = None
        self.colors = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'blue': (0, 0, 255)
        }
        self.move = None
        self.game_started = True
        self.game_result = None
        self.player1 = None
        self.player2 = None


def main():
    pygame.init()
    context = Context(3)
    size_window = (context.w, context.h)
    context.screen = pygame.display.set_mode(size_window)
    pygame.display.set_caption("Крестики-Нолики")
    # pygame.display.set_icon(pygame.image.load("krasnii krestik.bmp"))

    context.clock = pygame.time.Clock()

    context.ttt_list = [[0] * context.n for _ in range(context.n)]
    context.move = 0
    context.game_result = False

    context.screen.fill(context.colors['black'])

    pygame.display.update()
    pygame.mouse.set_visible(True)

    context.player1 = Player(pygame, context, 'x')
    context.player2 = Player(pygame, context, 'o')

    while True:
        run(pygame, context)


if __name__ == '__main__':
    main()


# add menu
    # add background with rules
    # one player (with bots)
        # ask name
    # two players
        # ask name for player1
        # ask name for player2
    # record table (optional)
    # exit

# добавить панельку со счетом
# <button_go_menu> name1 счет name2

# AI
    # random bot

# Finish game steps
    # show table for 2 sek
    # show who won (2sek)
    # update score
    # drop table

# BUGS
    # RESULT isn't dropped
    # first move 'o'