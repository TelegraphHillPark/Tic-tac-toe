import sys

from button import Button


class Menu:
    def __init__(self, pygame, context, button_params):
        self.buttons = []
        self.pygame = pygame
        self.context = context
        self.create_buttons(button_params)

    # инициализация необходимых для отрисовки кнопок
    def create_buttons(self, button_params):
        for idx, params in enumerate(button_params):
            self.buttons.append(
                Button(
                    self.context,
                    text=params['text'],
                    pos=(self.context.w // 2 - 100, self.context.h // 3 + 50*idx),
                    elevation=5,
                    callback=params['callback']
                ))

    def _draw_buttons(self):
        for b in self.buttons:
            b.draw()
        for b in self.buttons:
            b.check_click()

    # в методе вызывается _draw_buttons и закрашивается фон меню серым
    def draw_menu(self):
        self.context.screen.fill('#DCDDD8')
        self._draw_buttons()

    # закрытие программы
    def quit_game(self):
        self.pygame.quit()
        sys.exit()
