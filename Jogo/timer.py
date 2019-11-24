import time
import curses

import textPrint

def block_screen(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    stdscr.attron(curses.color_pair(1))

    for tempo in range(10):
        stdscr.clear()
        
        textPrint.print_title(stdscr)

        tempo_faltando = "Tempo faltando: " + str(10 - tempo)
        
        textPrint.print_center(stdscr,tempo_faltando)

        stdscr.refresh()

        time.sleep(1)