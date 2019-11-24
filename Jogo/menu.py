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

# Funcao que cria botao voltar
def back_btn(stdscr, selected_row_idx, current_menu):
    # Limpa a Tela
    stdscr.clear()

    # Altura e Largura da Tela
    altura, largura = stdscr.getmaxyx()
    
    # Pega o indice e o texto do item atual do menu
    for indice, row in enumerate(current_menu):
        text = row
        
        # Coordenadas do texto
        x = largura//2 - len(text)//2
        y = altura - (altura//8) - len(current_menu)//2 + indice
        
        # Colore parte selecionada diferente das demais
        if indice == selected_row_idx:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, row)
            stdscr.attron(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    
    stdscr.refresh()

def horizontal_menu(stdscr, selected_row_idx, current_menu):
    # Altura e Largura da Tela
    altura, largura = stdscr.getmaxyx()

    total_menu_len = 0

    for indice,row in enumerate(current_menu):
        total_menu_len += len(row)
    
    # Pega o indice e o texto do item atual do menu
    for indice, row in enumerate(current_menu):
        text = row
        
        # Coordenadas do texto
        x = largura//2 - total_menu_len//2 - len(row) + total_menu_len * indice
        y = altura - altura//8
        
        # Colore parte selecionada diferente das demais
        if indice == selected_row_idx:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, row)
            stdscr.attron(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    
    stdscr.refresh()