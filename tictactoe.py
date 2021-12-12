import sys


class Tictactoe:
    def __init__(self, pygame, context):
        self.pygame = pygame
        self.context = context

    def draw_cross(self, x, y):
        self.pygame.draw.line(
            self.context.screen, self.context.colors['red'], (x + 14, y + 14),
            (x + self.context.size_block - 14, y + self.context.size_block - 14), 20
        )
        self.pygame.draw.line(
            self.context.screen, self.context.colors['red'],
            (x + self.context.size_block - 14, y + 14),
            (x + 14, y + self.context.size_block - 14), 20
        )

    def draw_circle(self, x, y):
        self.pygame.draw.circle(
            self.context.screen, self.context.colors['blue'],
            (x + self.context.size_block // 2, y + self.context.size_block // 2),
            self.context.size_block // 2 - 5, 10
        )

    def draw_top_panel(self):
        self.pygame.draw.rect(
            self.context.screen, self.context.colors['white'],
            (0, 0, self.context.w, self.context.top_panel_size_y))
        font = self.pygame.font.SysFont('stxingkai', 60)  # 60pt = 20 symbols
        text1 = font.render('player1 0:0 player22', True, self.context.colors['black'])
        # text_rect = text1.get_rect()
        # text_x = screen.get_width() / 2 - text_rect.width / 2
        # text_y = screen.get_height() / 2 - text_rect.height / 2
        self.context.screen.blit(text1, [0, 0])

    def check_win(self, sign):
        n = self.context.n
        spisok = self.context.ttt_list
        zero = 0
        for row in spisok:
            zero += row.count(0)
            if row.count(sign) == n:
                return sign

        for col in range(n):
            k = 1
            for i in range(n):
                if spisok[i][col] != sign:
                    k = 0
            if k == 1:
                return sign

        k = 1
        for i in range(n):
            if spisok[i][i] != sign:
                k = 0
        if k == 1:
            return sign

        k = 1
        sub = 0
        for i in range(n):
            if spisok[i][n - 1 - sub] != sign:
                k = 0
            sub += 1
        if k == 1:
            return sign

        if zero == 0:
            return 'Piece'

        return False

    def get_current_player(self, move):
        if (move - 1) % 2 == 0:
            return self.context.player1
        return self.context.player2

    def calculate_game(self):
        n = self.context.n
        size_block = self.context.size_block
        screen = self.context.screen
        margin = self.context.margin

        player = self.get_current_player(self.context.move)

        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.finish_game()
            elif (event.type == self.pygame.MOUSEBUTTONDOWN or player.mode == 'bot') \
                    and not self.context.game_result:
                player.move()
            elif (event.type == self.pygame.KEYDOWN
                  and event.key == self.pygame.K_SPACE):
                self.reset()

        self.draw_top_panel()

        if not self.context.game_result:
            for row in range(n):
                for col in range(n):
                    x = col * size_block + (col + 1) * margin
                    y = (row * size_block + (row + 1) * margin
                         + self.context.top_panel_size_y)
                    self.pygame.draw.rect(
                        screen, self.context.colors['white'],
                        (x, y, size_block, size_block))

                    if self.context.ttt_list[row][col] == 'x':
                        player_id = 1
                    elif self.context.ttt_list[row][col] == 'o':
                        player_id = 2
                    else:
                        continue

                    if player_id == 1:
                        self.draw_cross(x, y)
                    else:
                        self.draw_circle(x, y)

        if not self.context.game_result:
            self.context.game_result = self.check_win(player.sign)

        if self.context.game_result:
            screen.fill(self.context.colors['black'])
            font = self.pygame.font.SysFont('stxingkai', 80)
            text1 = font.render(
                self.context.game_result, True, self.context.colors['white'])
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])

    def reset(self):
        self.context.game_result = False
        self.context.ttt_list = [[0] * self.context.n for _ in range(self.context.n)]
        self.context.move = 0
        self.context.screen.fill(self.context.colors['black'])

    def finish_game(self):
        self.pygame.quit()
        sys.exit()
