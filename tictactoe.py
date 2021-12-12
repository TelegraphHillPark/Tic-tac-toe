# логика крестиков ноликов
import sys


def check_win(spisok, sign, n):
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


def reset(context):
    context.game_result = False
    context.ttt_list = [[0] * context.n for i in range(context.n)]
    context.move = 0
    context.screen.fill(context.colors['black'])


def finish_game(pygame):
    pygame.quit()
    sys.exit()


def draw_cross(pygame, x, y, context):
    pygame.draw.line(
        context.screen, context.colors['red'], (x + 14, y + 14),
        (x + context.size_block - 14, y + context.size_block - 14), 20
    )
    pygame.draw.line(
        context.screen, context.colors['red'], (x + context.size_block - 14, y + 14),
        (x + 14, y + context.size_block - 14), 20
    )


def draw_circle(pygame, x, y, context):
    pygame.draw.circle(
        context.screen, context.colors['blue'],
        (x + context.size_block // 2, y + context.size_block // 2),
        context.size_block // 2 - 5, 10
    )


def draw_top_panel(pygame, context):
    pygame.draw.rect(
        context.screen, context.colors['white'], (0, 0, context.w, context.top_panel_size_y))
    font = pygame.font.SysFont('stxingkai', 60)  # 60pt = 20 symbols
    text1 = font.render('player1 0:0 player22', True, context.colors['black'])
    # text_rect = text1.get_rect()
    # text_x = screen.get_width() / 2 - text_rect.width / 2
    # text_y = screen.get_height() / 2 - text_rect.height / 2
    context.screen.blit(text1, [0, 0])


def get_current_player(move, context):
    if (move - 1) % 2 == 0:
        return context.player1
    return context.player2


def calculate_game(pygame, context):
    n = context.n
    size_block = context.size_block
    screen = context.screen
    margin = context.margin

    player = get_current_player(context.move, context)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish_game(pygame)
        elif (event.type == pygame.MOUSEBUTTONDOWN or player.mode == 'bot') and not context.game_result:
            player.move()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset(context)

    draw_top_panel(pygame, context)

    if not context.game_result:
        for row in range(n):
            for col in range(n):
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin + context.top_panel_size_y
                pygame.draw.rect(
                    screen, context.colors['white'], (x, y, size_block, size_block))

                if context.ttt_list[row][col] == 'x':
                    player_id = 1
                elif context.ttt_list[row][col] == 'o':
                    player_id = 2
                else:
                    continue

                if player_id == 1:
                    draw_cross(pygame, x, y, context)
                else:
                    draw_circle(pygame, x, y, context)

    if not context.game_result:
        context.game_result = check_win(context.ttt_list, player.sign, n)

    if context.game_result:
        screen.fill(context.colors['black'])
        font = pygame.font.SysFont('stxingkai', 80)
        text1 = font.render(context.game_result, True, context.colors['white'])
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])


def draw_menu():
    pass


def run(pygame, context):
    if context.game_started:
        calculate_game(pygame, context)
    else:
        draw_menu()
    pygame.display.update()
    context.clock.tick(60)
