import pyrebase
import curses
import time
import menu

def main(stdscr):
    # Menu com as opcoes de login
    menu_login = ('Login', 'Registrar', 'Scoreboard', 'Sair')

    # Esconde o cursor 
    curses.curs_set(0)

    # Opcao atual do menu
    current_row_idx = 0

    # Esquemas de cores
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Imprime o menu de login na tela
    menu.print_menu(stdscr, current_row_idx, menu_login)

    while True:
        # Recebe a entrada do teclado
        key = stdscr.getch()
        stdscr.clear()

        # Mover para cima no menu
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        
        # Mover para baixo no menu
        elif key == curses.KEY_DOWN and current_row_idx < len(menu_login) - 1:
            current_row_idx += 1

        # Seleciona uma opcao do menu
        elif key == curses.KEY_ENTER or key in [10,13]:
            stdscr.clear()
            
            # Caso selecione a opcao de sair
            if current_row_idx == len(menu_login) - 1:
                # Mensagem ao sair
                stdscr.addstr(0, 0, "Obrigado por jogar. Aperte qualquer coisa para sair")
                stdscr.refresh()

                # Espera o user digitar algo pra sair
                stdscr.getch()

                break
            
            # Mensagem quando user escolhe alguma opcao
            stdscr.addstr(0, 0, "Voce escolheu: {}" .format(menu_login[current_row_idx]))

            stdscr.refresh()
            stdscr.getch()

        # Atualiza o menu
        menu.print_menu(stdscr, current_row_idx, menu_login)
        stdscr.refresh()
        
curses.wrapper(main)