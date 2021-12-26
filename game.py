from menu import Menu
from player import Player, RandomBot
from tictactoe import Tictactoe


# определение режима игры
def proceed_game(pygame, context):
    context.screen.fill(context.colors['black'])
    if context.game is None:
        context.player1 = Player(pygame, context, 'x', 'Игрок 1')
        if context.mode == 'two_players':
            context.player2 = Player(pygame, context, 'o', 'Игрок 2 ')
        elif context.mode == 'one_player':
            context.player2 = RandomBot(pygame, context, 'o', 'Бот')

        context.game = Tictactoe(pygame, context)
    context.game.calculate_game()


def initialize_one_player_mode(context):
    context.game_started = True
    context.mode = 'one_player'


def initialize_two_player_mode(context):
    context.game_started = True
    context.mode = 'two_players'


# отрисовка меню приложения
def draw_menu(pygame, context):
    if context.menu is None:
        context.menu = Menu(
            pygame, context,
            button_params=[
                {'text': 'Один игрок',
                 'callback': lambda: initialize_one_player_mode(context)},
                {'text': 'Два игрока',
                 'callback': lambda: initialize_two_player_mode(context)},
                {'text': 'Выход',
                 'callback': lambda: quit(pygame)}
            ]
        )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            context.menu.quit_game()

    context.menu.draw_menu()


# вызывает proceed_game (game_started = True) или draw_menu
def run(pygame, context):
    if context.game_started:
        proceed_game(pygame, context)
    else:
        draw_menu(pygame, context)
    pygame.display.update()
    context.clock.tick(60)
