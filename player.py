import random


class Player:
    mode = 'human'

    def __init__(self, pygame, context, sign):
        self.pygame = pygame
        self.context = context
        self.sign = sign

    def move(self):
        context = self.context
        x_mouse, y_mouse = self.pygame.mouse.get_pos()
        if y_mouse < context.top_panel_size_y:
            return
        col = x_mouse // (context.size_block + context.margin)
        row = (y_mouse - context.top_panel_size_y) // (
                    context.size_block + context.margin)
        if context.ttt_list[row][col] == 0:
            context.ttt_list[row][col] = self.sign
            context.move += 1


class RandomBot(Player):
    mode = 'bot'

    def move(self):
        # def get_possible_points():
        #     n = self.context.n
        #     for i in range(n):
        #         for j in range(n):
        #             if self.context.ttt_list[i][j]
        #     pass

        print('here')
        self.context.move += 1
        # x, y = random.choice(get_possible_points())
        #
        # self.context.ttt_list[x][y] = self.sign


class HardBot(RandomBot):
    def move(self):
        # Просканировать поле
        # выбрать выигрышную стратегию
        # сделать шаг
        pass
