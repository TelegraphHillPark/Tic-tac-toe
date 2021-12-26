import pygame


class Button:
    def __init__(self, context, text, pos, elevation, callback):
        # основные атрибуты
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]
        self.context = context
        self.gui_font = pygame.font.Font(None, 30)

        # верхний прямоугольник
        width = 200
        height = 40
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # нижний прямоугольник
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        # текст
        self.text = text
        self.text_surf = self.gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

        # callback
        self.callback = callback

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(self.context.screen, self.bottom_color, self.bottom_rect,
                         border_radius=12)
        pygame.draw.rect(
            self.context.screen, self.top_color, self.top_rect, border_radius=12)
        self.context.screen.blit(self.text_surf, self.text_rect)

    def check_click(self):
        # отбражение изменения кнопки при нажатии
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed:
                    self.callback()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'
