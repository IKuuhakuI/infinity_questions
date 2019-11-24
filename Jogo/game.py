import curses

import menu

def show_game_menu(stdscr, user_id):
    # Menu com as opcoes para o jogo 
    menu_jogo = ('Jogar', 'Perguntas', 'Scoreboard', 'Logout')

    