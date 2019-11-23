import pyrebase
import curses

import menu
import login
import registrar
import scoreboard
import textPrint

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

    textPrint.print_title(stdscr)

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
                message = "Obrigado por jogar. Aperte qualquer coisa para sair"
                textPrint.print_center(stdscr, message)
                textPrint.print_title(stdscr)
                stdscr.refresh()

                # Espera o user digitar algo pra sair
                stdscr.getch()

                break

            # Caso selecione a opcao de login  
            elif current_row_idx == 0:
                curses.curs_set(True)
                login.start_login(stdscr)
                curses.curs_set(False)

            # Caso selecione a opcao de registrar
            elif current_row_idx == 1:
                curses.curs_set(True)
                registrar.start_registrar(stdscr)
                curses.curs_set(False)

            elif current_row_idx == 2:
                scoreboard.show_scoreboard(stdscr)

            # Mensagem quando user escolhe alguma opcao
            else:
                stdscr.addstr(0, 0, "Voce escolheu: {}" .format(menu_login[current_row_idx]))
                stdscr.getch()
                
            stdscr.refresh()


        # Atualiza o menu
        menu.print_menu(stdscr, current_row_idx, menu_login)
        stdscr.refresh()
        textPrint.print_title(stdscr)
        
curses.wrapper(main)