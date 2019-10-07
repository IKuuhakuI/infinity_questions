import curses

# Funcao que cria menus
def print_menu(stdscr, selected_row_idx, current_menu):
    # Limpa a Tela
    stdscr.clear()

    # Altura e Largura da Tela
    altura, largura = stdscr.getmaxyx()
    
    # Pega o indice e o texto do item atual do menu
    for indice, row in enumerate(current_menu):
        text = row
        
        # Coordenadas do texto
        x = largura//2 - len(text)//2
        y = altura//2 - len(current_menu)//2 + indice
        
        # Colore parte selecionada diferente das demais
        if indice == selected_row_idx:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, row)
            stdscr.attron(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    
    stdscr.refresh()
