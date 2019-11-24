import curses

import actions
import menu
import textPrint

def show_game_menu(stdscr):
    # Menu com as opcoes para o jogo 
    menu_jogo = ('Jogar', 'Perguntas', 'Scoreboard', 'Logout')

    # Esconde o cursor
    curses.curs_set(0)

    # Opcao atual do menu
    current_row_idx = 0

    # Esquemas de cores
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Imprime o menu do Jogo
    menu.print_menu(stdscr, current_row_idx, menu_jogo)

    # Imprime o titulo do jogo
    textPrint.print_title(stdscr)

    while True:
        key = stdscr.getch()

        stdscr.clear()

        if actions.keyboard(key) == 'up':
            textPrint.print_center(stdscr, 'up')

        elif actions.keyboard(key) == 'down':
            textPrint.print_center(stdscr, 'down')

        elif actions.keyboard(key) == 'enter':
            textPrint.print_center(stdscr, 'enter')

curses.wrapper(show_game_menu)