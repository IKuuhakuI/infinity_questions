import pyrebase
import curses
import time
import menu

def main(stdscr):
    menu_login = ('Login', 'Registrar', 'Sair')

    curses.curs_set(0)
    current_row_idx = 0

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    menu.print_menu(stdscr, current_row_idx, menu_login)

    stdscr.refresh()

    stdscr.getch()

curses.wrapper(main)
