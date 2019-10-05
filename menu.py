import curses
def print_menu(stdscr, selected_row_idx, current_menu):
    stdscr.clear()
    altura, largura = stdscr.getmaxyx()

    for indice, row in enumerate(current_menu):
        text = row
        x = largura//2 - len(text)//2
        y = altura//2 - len(current_menu)//2 + indice

        if indice == selected_row_idx:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, row)
            stdscr.attron(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    
    stdscr.refresh()