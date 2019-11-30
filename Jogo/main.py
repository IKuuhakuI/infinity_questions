import curses
import os
import pyrebase

import actions
import login
import menu
import registrar
import scoreboard
import screen
import textPrint


def start_screen():
    # Windows 
    if os.name == "nt":
        screen.resize_screen_windows()
    # Linux
    else:
        screen.resize_screen_linux()

    input("Aperte qualquer coisa para abrir o jogo...")
    curses.wrapper(main)

def main(stdscr):
    # Menu com as opcoes de login
    menu_login = ('Login', 'Registrar', 'Scoreboard', 'Sair')

    # Esconde o cursor 
    curses.curs_set(0)

    # tela inicial do jogo

    screen.show_title_screen(stdscr)

    # Opcao atual do menu
    current_row_idx = 0

    # Esquemas de cores
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Imprime o menu de login na tela
    menu.print_menu(stdscr, current_row_idx, menu_login)

    textPrint.print_title(stdscr)

    selected_row_idx = 0

    while True:
        # Recebe a entrada do teclado
        key = stdscr.getch()
        stdscr.clear()

        # Mover para cima no menu
        if actions.keyboard(key) == 'up' and current_row_idx > 0:
            current_row_idx -= 1
        
        # Mover para baixo no menu
        elif actions.keyboard(key) == 'down' and current_row_idx < len(menu_login) - 1:
            current_row_idx += 1

        # Seleciona uma opcao do menu
        elif actions.keyboard(key) == 'enter':
            stdscr.clear()
            
            # Caso selecione a opcao de sair
            if current_row_idx == len(menu_login) - 1:

                # Confirmar se deseja mesmo sair     
                saiu = screen.show_deseja_sair(stdscr)      

                stdscr.clear()
                textPrint.print_title(stdscr)
                
                if saiu == True:
                    # Mensagem de agradecimento por ter entrado no jogo
                    message = "Obrigado por jogar. Aperte qualquer coisa para sair"
                    textPrint.print_center(stdscr, message)
                    textPrint.print_title(stdscr)
                    stdscr.refresh()
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

            # Caso selecione a opcao de scoreboard  
            elif current_row_idx == 2:
                screen.show_scoreboard(stdscr)


            # Mensagem quando user escolhe alguma opcao
            else:
                stdscr.addstr(0, 0, "Voce escolheu: {}" .format(menu_login[current_row_idx]))
                stdscr.getch()
                
            stdscr.refresh()


        # Atualiza o menu
        menu.print_menu(stdscr, current_row_idx, menu_login)
        stdscr.refresh()
        textPrint.print_title(stdscr)
 
start_screen()       
#curses.wrapper(main)