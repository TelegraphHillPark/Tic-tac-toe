import pygame

from game import run


class Context:
    margin = 7
    size_block = 125

    def __init__(self, n):
        # screen params
        self.n = n
        self.top_panel_size_y = 100
        self.w = self.size_block * n + self.margin * 4
        self.h = self.w + self.top_panel_size_y
        self.screen = None

        # map params
        self.ttt_list = None

        # misc
        self.clock = None
        self.colors = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'blue': (0, 0, 255),
            'lightblue': (135, 206, 250),
        }
        self.move = None
        self.game_started = False
        self.game_result = None
        self.player1 = None
        self.player2 = None
        self.menu = None
        self.game = None
        self.mode = None


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
    # ['x', 'o', Piece, False(not finished)]
    context.game_result = False

    context.screen.fill(context.colors['black'])

    pygame.display.update()
    pygame.mouse.set_visible(True)

    while True:
        run(pygame, context)


if __name__ == '__main__':
    main()
