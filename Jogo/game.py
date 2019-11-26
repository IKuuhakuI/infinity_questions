import curses

import actions
import getData
import menu
import pyrebase
import textPrint
import scoreboard
import play
import screen
import menuPerguntas

def show_game_menu(stdscr, current_user):
    # Menu com as opcoes para o jogo 
    menu_jogo = ('Jogar', 'Perguntas', 'Scoreboard', 'Logout')

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
    menu.print_menu(stdscr, current_row_idx, menu_jogo)

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

        elif actions.keyboard(key) == 'down' and current_row_idx < len(menu_jogo) - 1:
            textPrint.print_center(stdscr, 'down')
            current_row_idx += 1

        elif actions.keyboard(key) == 'enter':
            stdscr.clear()
            textPrint.print_center(stdscr, 'enter')

            if current_row_idx == len(menu_jogo) - 1:
                break

            elif current_row_idx == 0:
                stdscr.clear()
                play.final_game(stdscr)



            elif current_row_idx == 1:
                 menuPerguntas.show_perguntas_menu(stdscr, current_user)

            elif current_row_idx == 2:
                screen.show_scoreboard(stdscr)

            stdscr.refresh()

        # Imprime o titulo do jogo
        menu.print_menu(stdscr, current_row_idx, menu_jogo)

        # Imprime o usuario atual
        textPrint.print_user_data(stdscr, data_list)        
        
        stdscr.refresh()

        textPrint.print_title(stdscr)