import pyrebase
import curses

import menu
import login
import registrar
import scoreboard
import textPrint
import screen
import actions

def main():
    screen.resize_screen()
    input("Aperte qualquer coisa para abrir o jogo...")
    curses.wrapper(screen.main_screen)
 
main()