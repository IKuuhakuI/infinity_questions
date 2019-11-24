import curses

# Imprime o titulo do jogo no topo da tela
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

# Imprime uma linha no centro da tela
def print_center(stdscr, text):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(1))

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    # Coordenadas do texto
    x_text = largura_tela//2 - len(text)//2
    y_text = altura_tela//2
 
    stdscr.addstr(y_text, x_text, text)

# Imprime uma linha no centro da tela
def erase_center(stdscr, text):
    curses.curs_set(0)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(3))

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    # Coordenadas do texto
    x_text = largura_tela//2 - len(text)//2
    y_text = altura_tela//2
 
    stdscr.addstr(y_text, x_text, text)

# Imprime varias linhas no centro da tela
def print_multi_lines(stdscr, text_list, lines):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(1))

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    for linha_atual in range(lines):
        # Coordenadas do texto
        x_text = largura_tela//2 - len(text_list[linha_atual])//2
        y_text = altura_tela//2 - lines + linha_atual
 
        stdscr.addstr(y_text, x_text, text_list[linha_atual])

# Imprime uma linha no final da tela
def print_bottom(stdscr, text):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(1))

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    # Coordenadas do texto
    x_text = largura_tela//2 - len(text)//2
    y_text = altura_tela - altura_tela//8
 
    stdscr.addstr(y_text, x_text, text)

def print_user_data(stdscr, user_data):
    user_name = "Usuario: " + user_data[0]
    user_high_score = "Highscore: " + str(user_data[1])

    text = user_name + " | " + user_high_score

    print_bottom(stdscr, text)
