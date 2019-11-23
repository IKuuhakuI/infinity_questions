import curses

def print_title(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(1))

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    title = "Infinity Questions"

    # Coordenadas do texto
    x_title = largura_tela//2 - len(title)//2
    y_title = altura_tela//8
 
    stdscr.addstr(y_title, x_title, title)