#Arquivo destinado aos menus de perguntas. Sao dois menus

import curses

import actions
import getUser
import menu
import pyrebase
import textPrint
import scoreboard
import play
import screen

# funcao destinada ao menu Perguntas onde
# as opcoes sao Adicionao Pergunta, Editar Pergunta e Retornar

def show_perguntas_menu(stdscr, current_user):
    # Menu com as opcoes para o jogo 
    menu_perguntas = ('Adicionar Pergunta', 'Editar Pergunta', 'Voltar')

    # Esconde o cursor
    curses.curs_set(0)

    # Opcao atual do menu
    current_row_idx = 0

    # Esquemas de cores
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Mensagem de carregamento
    textPrint.print_center(stdscr, "Carregando...")
    stdscr.refresh()

    # Pega os dados do usuario que esta logado
    current_user_data = getUser.get_user_data(current_user)
    current_user_name = current_user_data["Name"] 
    current_user_high_score = current_user_data["Highscore"]

    data_list = [current_user_name, current_user_high_score]

    # Imprime o menu do Jogo
    menu.print_menu(stdscr, current_row_idx, menu_perguntas)

    # Imprime o usuario atual
    textPrint.print_user_data(stdscr, data_list)
    
    # Imprime o titulo do jogo
    textPrint.print_title(stdscr)

    stdscr.refresh()

    while True:
        key = stdscr.getch()

        stdscr.clear()

        if actions.keyboard(key) == 'up' and current_row_idx > 0:
            textPrint.print_center(stdscr, 'up')
            current_row_idx -= 1

        elif actions.keyboard(key) == 'down' and current_row_idx < len(menu_perguntas) - 1:
            textPrint.print_center(stdscr, 'down')
            current_row_idx += 1

        elif actions.keyboard(key) == 'enter':
            stdscr.clear()
            textPrint.print_center(stdscr, 'enter')


			# Opcao Voltar:            
            if current_row_idx == len(menu_perguntas) - 1:
                break

            # Opcao Adicionar Pergunta
            elif current_row_idx == 0:
            	textPrint.print_center(stdscr, "FALTA CRIAR ESSA PARTE DO JOGO")
            	stdscr.getch()
                

            # Opcao Editar Pergunta
            elif current_row_idx == 1:
            	show_editar_perguntas_menu(stdscr, current_user)

            stdscr.refresh()

        # Imprime o titulo do jogo
        menu.print_menu(stdscr, current_row_idx, menu_perguntas)

        # Imprime o usuario atual
        textPrint.print_user_data(stdscr, data_list)        
        
        stdscr.refresh()

        textPrint.print_title(stdscr)


# menu editar perguntas, onde as opcoes sao: Apagar Pergunta" "Alterar Pergunta" e "voltar"
# esse menu entra na opcao editar perguntas do menu definido acima
def show_editar_perguntas_menu(stdscr, current_user):
    # Menu com as opcoes para o jogo 
    menu_editar_perguntas = ('Apagar Pergunta', 'Alterar Pergunta', 'Voltar')

    # Esconde o cursor
    curses.curs_set(0)

    # Opcao atual do menu
    current_row_idx = 0

    # Esquemas de cores
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Mensagem de carregamento
    textPrint.print_center(stdscr, "Carregando...")
    stdscr.refresh()

    # Pega os dados do usuario que esta logado
    current_user_data = getUser.get_user_data(current_user)
    current_user_name = current_user_data["Name"] 
    current_user_high_score = current_user_data["Highscore"]

    data_list = [current_user_name, current_user_high_score]

    # Imprime o menu do Jogo
    menu.print_menu(stdscr, current_row_idx, menu_editar_perguntas)

    # Imprime o usuario atual
    textPrint.print_user_data(stdscr, data_list)
    
    # Imprime o titulo do jogo
    textPrint.print_title(stdscr)

    stdscr.refresh()

    while True:
        key = stdscr.getch()

        stdscr.clear()

        if actions.keyboard(key) == 'up' and current_row_idx > 0:
            textPrint.print_center(stdscr, 'up')
            current_row_idx -= 1

        elif actions.keyboard(key) == 'down' and current_row_idx < len(menu_editar_perguntas) - 1:
            textPrint.print_center(stdscr, 'down')
            current_row_idx += 1

        elif actions.keyboard(key) == 'enter':
            stdscr.clear()
            textPrint.print_center(stdscr, 'enter')


			# Opcao Voltar:            
            if current_row_idx == len(menu_editar_perguntas) - 1:
                break

            # Opcao Apagar Pergunta
            elif current_row_idx == 0:
            	textPrint.print_center(stdscr, "FALTA CRIAR ESSA PARTE DO JOGO")
            	stdscr.getch()
                

            # Opcao Alterar Pergunta
            elif current_row_idx == 1:
                textPrint.print_center(stdscr, "FALTA ESSA PARTE DO JOGO")
                stdscr.getch()

            stdscr.refresh()

        # Imprime o titulo do jogo
        menu.print_menu(stdscr, current_row_idx, menu_editar_perguntas)

        # Imprime o usuario atual
        textPrint.print_user_data(stdscr, data_list)        
        
        stdscr.refresh()

        textPrint.print_title(stdscr)

