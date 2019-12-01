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
            	show_editar_perguntas_menu(stdscr, current_user, current_user_id)

            stdscr.refresh()

        # Imprime o titulo do jogo
        menu.print_menu(stdscr, current_row_idx, menu_perguntas)

        # Imprime o usuario atual
        textPrint.print_user_data(stdscr, data_list)        
        
        stdscr.refresh()

        textPrint.print_title(stdscr)


# menu editar perguntas, onde as opcoes sao: Apagar Pergunta" "Alterar Pergunta" e "voltar"
# esse menu entra na opcao editar perguntas do menu definido acima
def show_editar_perguntas_menu(stdscr, current_user_data, current_user):
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

            ### Opcao Apagar Pergunta ##############
            elif current_row_idx == 0:
                current_row_idx = 0

                while True:
                    screen.show_questions_rules_screen(stdscr,current_row_idx)

                    # Entrada do teclado
                    key = stdscr.getch()

                    # Navegar pelo menu
                    if actions.keyboard(key) == 'left' and current_row_idx > 0:
                        current_row_idx -= 1
                    elif actions.keyboard(key) == 'right' and current_row_idx < 1:
                        current_row_idx += 1

                    # Caso selecione uma opcao
                    elif actions.keyboard(key) == 'enter':
                        # Caso selecione continuar
                        if current_row_idx == 0:
                            stdscr.clear()

                            escolha = show_all_questions(stdscr, current_user, "Apagar")

                            if escolha == -1:
                                stdscr.clear()
                                textPrint.print_center(stdscr, "Usuario ainda nao enviou perguntas")

                                stdscr.getch()

                            elif escolha != -2:
                                stdscr.clear()

                                pergunta_text = getData.get_one_question_data(escolha)

                                warning = ["Aperte 's' para confirmar que deseja deletar a seguinte pergunta:", pergunta_text, "Para cancelar, aperte qualquer outra tecla"]

                                textPrint.print_multi_lines(stdscr, warning, len(warning))

                                stdscr.getch()
                        else:
                            current_row_idx = 0
                            break

            ### Opcao Alterar Pergunta##############
            elif current_row_idx == 1:
                current_row_idx = 0

                while True:
                    screen.show_questions_rules_screen(stdscr,current_row_idx)

                    # Entrada do teclado
                    key = stdscr.getch()

                    # Navegar pelo menu
                    if actions.keyboard(key) == 'left' and current_row_idx > 0:
                        current_row_idx -= 1
                    elif actions.keyboard(key) == 'right' and current_row_idx < 1:
                        current_row_idx += 1

                    # Caso selecione uma opcao
                    elif actions.keyboard(key) == 'enter':
                        # Caso selecione continuar
                        if current_row_idx == 0:
                            stdscr.clear()

                            escolha = show_all_questions(stdscr, current_user, "Editar")

                            if escolha == -1:
                                stdscr.clear()
                                textPrint.print_center(stdscr, "Usuario ainda nao enviou perguntas")

                                stdscr.getch()

                            elif escolha != -2:
                                stdscr.clear()
                                perguntasActions.escreve_pergunta(stdscr, current_user, current_user_data, "Editar", escolha)



                        # Caso selecione voltar
                        else:
                            break
                
        
        stdscr.refresh()

        # Imprime o titulo do jogo
        menu.print_menu(stdscr, current_row_idx, menu_editar_perguntas)

        # Imprime o usuario atual
        textPrint.print_user_data(stdscr, data_list)        
        
        stdscr.refresh()

        textPrint.print_title(stdscr)


########### MOSTRA AS PERGUNTAS FEITAS PELO USER ###########
def show_all_questions(stdscr, current_user_id, mode):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    stdscr.attron(curses.color_pair(1))
    
    current_page_index = 0

    textPrint.print_center(stdscr, "Carregando...")
    stdscr.refresh()

    questions_data = getData.get_user_questions_data(current_user_id)

    # Caso user nao tenha enviado perguntas
    if len(questions_data) == 1:
        return -1

    questions_ids = perguntasActions.get_questions_ids(questions_data)

    questions = perguntasActions.get_question_list(questions_ids)

    pages_id = perguntasActions.get_questions_pages(questions_ids)
    pages = perguntasActions.get_questions_pages(questions)
    quantidade_paginas = len(pages)

    text = ["Pagina " + str(current_page_index + 1) + " / " + str(quantidade_paginas), "Para passar a pagina digite 'n'", "Para voltar a pagina, digite 'b'", "Para sair, digite 'e'"]

    stdscr.clear()

    while True:
        current_page = pages[current_page_index]
        page_with_numbers = perguntasActions.add_question_number_on_page(current_page)

        textPrint.print_multi_bottom_lines(stdscr, text, len(text))
        textPrint.print_multi_lines(stdscr, page_with_numbers, len(page_with_numbers))
        textPrint.print_title(stdscr)
        stdscr.refresh()

        key = stdscr.getch()

        # Caso user queira sair
        if actions.verify_exit(key) == True:
            return -2

        elif actions.verify_next(key) == True and current_page_index < quantidade_paginas - 1:
            current_page_index += 1
            
            text = ["Pagina " + str(current_page_index + 1) + " / " + str(quantidade_paginas), "Para passar a pagina digite 'n'", "Para voltar a pagina, digite 'b'", "Para sair, digite 'e'"]

            stdscr.clear()

        elif actions.verify_back(key) == True and current_page_index > 0:
            current_page_index -= 1
            
            text = ["Pagina " + str(current_page_index + 1) + " / " + str(quantidade_paginas), "Para passar a pagina digite 'n'", "Para voltar a pagina, digite 'b'", "Para sair, digite 'e'"]
            
            stdscr.clear()

        # Retorna a pergunta selecionada
        elif actions.verify_which_question(key) != -1 and actions.verify_which_question(key) < len(current_page) + 1:
            return pages_id[current_page_index][actions.verify_which_question(key)-1]

        else:
            stdscr.clear()
            text = ["Entrada Invalida", "Pagina " + str(current_page_index + 1) + " / " + str(quantidade_paginas), "Para passar a pagina digite 'n'", "Para voltar a pagina, digite 'b'", "Para sair, digite 'e'"]
            
#def test(stdscr):
#    while True:
#        a = show_all_questions(stdscr, 1, 0)
#        stdscr.clear()
#        textPrint.print_center(stdscr, str(a))
#        stdscr.refresh()
#        stdscr.getch()

#        if a == -1:
#            break

#curses.wrapper(test)