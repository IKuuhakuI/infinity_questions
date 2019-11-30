#Arquivo destinado aos menus de perguntas. Sao dois menus

import curses

import actions
import getData
import menu
import pyrebase
import textPrint
import scoreboard
import play
import screen
import perguntasActions

# funcao destinada ao menu Perguntas onde
# as opcoes sao Adicionao Pergunta, Editar Pergunta e Retornar

def show_perguntas_menu(stdscr, current_user, current_user_id):
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
    current_user_data = getData.get_user_data(current_user_id)
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
            	perguntasActions.adiciona_pergunta(stdscr, current_user_id, current_user_data)
                

            # Opcao Editar Pergunta
            elif current_row_idx == 1:
            	show_editar_perguntas_menu(stdscr, current_user_id)

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
    current_user_data = getData.get_user_data(current_user)

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

def show_all_questions(stdscr, current_user_id, mode):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    stdscr.attron(curses.color_pair(1))
    
    current_page_index = 0

    questions = getData.get_user_questions_data(current_user_id)

    text_questions_ids = perguntasActions.get_questions_ids(questions)

    pages = perguntasActions.get_questions_pages(text_questions_ids)
    quantidade_paginas = len(pages)

    text = ["Pagina " + str(current_page_index + 1), "Para passar a pagina digite 'n'", "Para voltar a pagina, digite 'b'", "Para sair, digite 'e'"]

    while True:
        current_page = pages[current_page_index]
        page_with_numbers = perguntasActions.add_question_number_on_page(current_page)

        textPrint.print_multi_bottom_lines(stdscr, text, len(text))
        textPrint.print_multi_lines(stdscr, page_with_numbers, len(page_with_numbers))
        textPrint.print_title(stdscr)
        stdscr.refresh()

        key = stdscr.getch()

        if actions.verify_exit(key) == True:
            break

        elif actions.verify_next(key) == True and current_page_index < quantidade_paginas - 1:
            current_page_index += 1
            
            text = ["Pagina " + str(current_page_index + 1), "Para passar a pagina digite 'n'", "Para voltar a pagina, digite 'b'", "Para sair, digite 'e'"]

            stdscr.clear()

        elif actions.verify_back(key) == True and current_page_index > 0:
            current_page_index -= 1
            
            text = ["Pagina " + str(current_page_index + 1), "Para passar a pagina digite 'n'", "Para voltar a pagina, digite 'b'", "Para sair, digite 'e'"]
            
            stdscr.clear()

        elif actions.verify_which_question(key) != -1:
            pass

        else:
            stdscr.clear()
            text = ["Entrada Invalida", "Pagina " + str(current_page_index + 1), "Para passar a pagina digite 'n'", "Para voltar a pagina, digite 'b'", "Para sair, digite 'e'"]
            
def test(stdscr):
    show_all_questions(stdscr, 1, 0)

curses.wrapper(test)
