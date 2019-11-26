# Criando arquivo play.py
#arquivo que vai ficar a logica do jogo propriamente dito
#Aqui dentro vai ser chamado as telas de recorde pessoal, global ou não recorde
import curses

import screen
import textPrint 
import getQuestions

def final_game(stdscr):
    # Imprime titulo do jogo
    textPrint.print_title(stdscr)
    # Imprime regras do jogo
    screen.show_welcome_screen(stdscr)
    stdscr.clear()

    # Imprime titulo do jogo
    textPrint.print_title(stdscr)
    # Tela de carregamento
    textPrint.print_center(stdscr, "Carregando...")
    stdscr.refresh()

    # Lista com as perguntas do Jogo
    lista_perguntas = getQuestions.get_questions_data()
    stdscr.clear()

    hasGivenUp = False
    hasLost = False

    for pergunta in range(len(lista_perguntas)):
        pergunta_atual = "Pergunta " + str(pergunta + 1) + ": " + lista_perguntas[pergunta]["Pergunta"]
        id_atual = lista_perguntas[pergunta]["Id"]
        
        dict_respostas = getQuestions.get_answer(id_atual)
        right_answer = getQuestions.get_right_answer(dict_respostas)
        
        resposta_a = 'a)' + str(dict_respostas['a']['valor'])
        resposta_b = 'b)' + str(dict_respostas['b']['valor'])
        resposta_c = 'c)' + str(dict_respostas['c']['valor'])
        resposta_d = 'd)' + str(dict_respostas['d']['valor'])

        text_list = [pergunta_atual, resposta_a, resposta_b, resposta_c, resposta_d]

        textPrint.print_multi_lines(stdscr, text_list, len(text_list))

        desistir = [71, 103]

        while True:
            key = stdscr.getch()

            stdscr.clear()
            stdscr.refresh()

            if key not in [65,66,67,68,71,97,98,99,100,103]:
                print(key)
                textPrint.print_bottom(stdscr, "Entrada Invalida!")

            else:
                if key in desistir:
                    textPrint.print_bottom(stdscr, "Para confirmar desistencia, aperte s, caso contrario aperte outra tecla")
                    textPrint.print_multi_lines(stdscr, text_list, len(text_list))


                    confirm_key = stdscr.getch()

                    if confirm_key in [83, 115]:
                        hasGivenUp = True
                        break

                elif key in right_answer:
                    mensagem = ['Correto!', 'Aperte qualquer tecla para continuar']
                    textPrint.print_multi_lines(stdscr, mensagem, 2)
                    stdscr.getch()
                    stdscr.clear()
                    break

                else:
                    mensagem = ['Errado!', 'Aperte qualquer tecla para continuar']
                    textPrint.print_multi_lines(stdscr, mensagem, 2)
                    hasLost = True
                    stdscr.getch()
                    stdscr.clear()
                    break

            stdscr.clear()
            stdscr.refresh()
            textPrint.print_multi_lines(stdscr, text_list, len(text_list))
            stdscr.refresh()

        if hasGivenUp == True or hasLost == True:
            break
        
curses.wrapper(final_game)