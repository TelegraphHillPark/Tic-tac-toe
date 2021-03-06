import sys


class Tictactoe:
    def __init__(self, pygame, context):
        self.pygame = pygame
        self.context = context

    # отрисовка "крестиков"
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

    # отрисовка "ноликов"
    def draw_circle(self, x, y):
        self.pygame.draw.circle(
            self.context.screen, self.context.colors['blue'],
            (x + self.context.size_block // 2, y + self.context.size_block // 2),
            self.context.size_block // 2 - 5, 10
        )

    # отрисовка верхней панели со счетом в режиме игры
    def draw_top_panel(self):
        self.pygame.draw.rect(
            self.context.screen, self.context.colors['lightblue'],
            (0, 0, self.context.w, self.context.top_panel_size_y))
        font = self.pygame.font.SysFont('monospace', 35)
        player1 = self.context.player1
        player2 = self.context.player2
        score1 = str(player1.score)
        score2 = str(player2.score)
        score = '{score1}:{score2}'.format(
            score1=score1,
            score2=score2,
        )
        possible_left_len = 9 - len(score1) - 1
        possible_right_len = 9 - len(score2) - 1
        name1 = player1.name[:min(possible_left_len, len(player1.name))]
        name2 = player2.name[:min(possible_right_len, len(player2.name))]
        name1 = name1.ljust(possible_left_len, ' ')
        name2 = name2.rjust(possible_right_len, ' ')
        text1 = font.render(
            '{name1} {score} {name2}'.format(
                name1=name1,
                name2=name2,
                score=score
            ),
            True,
            self.context.colors['black']
        )
        self.context.screen.blit(text1, [0, self.context.top_panel_size_y / 4])

    # возврат результата партии определенной сессии
    def check_win(self, player):
        sign = player.sign
        n = self.context.n
        spisok = self.context.ttt_list

        def increase_score_and_get_sign():
            player.score += 1
            return sign

        # Проверка строк
        for row in spisok:
            if row.count(sign) == n:
                return increase_score_and_get_sign()

        # Проверка столбцов
        for col in range(n):
            win = True
            for i in range(n):
                if spisok[i][col] != sign:
                    win = False
                    break
            if win:
                return increase_score_and_get_sign()

        # Проверка диагонали
        win = True
        for i in range(n):
            if spisok[i][i] != sign:
                win = False
        if win:
            return increase_score_and_get_sign()

        # Проверка другой диагонали
        win = True
        sub = 0
        for i in range(n):
            if spisok[i][n - 1 - sub] != sign:
                win = 0
            sub += 1
        if win:
            return increase_score_and_get_sign()

        # Проверка на ничью
        zero = 0
        for row in spisok:
            zero += row.count(0)
        if zero == 0:
            return 'Piece'

        return False

    # возврат хода текущего игрока
    def get_current_player(self, move):
        if move % 2 == 0:
            return self.context.player1
        return self.context.player2

    # логика игрового процесса
    def calculate_game(self):
        n = self.context.n
        size_block = self.context.size_block
        screen = self.context.screen
        margin = self.context.margin

        self.draw_top_panel()

        player = self.get_current_player(self.context.move)

        if self.context.game_result:
            screen.fill(self.context.colors['black'])
            font = self.pygame.font.SysFont('stxingkai', 80)
            text1 = font.render(
                self.context.game_result, True, self.context.colors['white'])
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])
            self.pygame.time.wait(1000)

        for event in self.pygame.event.get():
            player = self.get_current_player(self.context.move)
            if event.type == self.pygame.QUIT:
                self.finish_game()
            elif (event.type == self.pygame.MOUSEBUTTONDOWN or player.mode == 'bot') \
                    and not self.context.game_result:
                player.move()
            elif (event.type == self.pygame.KEYDOWN
                  and event.key == self.pygame.K_SPACE):
                self.reset()

        # Draw game field
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
            self.context.game_result = self.check_win(player)

    # перезапуск партии
    def reset(self):
        self.context.game_result = False
        self.context.ttt_list = [[0] * self.context.n for _ in range(self.context.n)]
        self.context.move = 0
        self.context.screen.fill(self.context.colors['black'])

    # закрытие программы
    def finish_game(self):
        self.pygame.quit()
        sys.exit()
