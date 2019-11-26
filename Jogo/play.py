# Criando arquivo play.py
#arquivo que vai ficar a logica do jogo propriamente dito
#Aqui dentro vai ser chamado as telas de recorde pessoal, global ou não recorde
import curses

import actions
import screen
import textPrint 
import getQuestions

def final_game(stdscr):
    # A, B, C, D, G, a, b, c, d, g
    caracteres_permitidos = [65,66,67,68,71,97,98,99,100,103]

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

    pontos = 0

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
        textPrint.print_title(stdscr)

        desistir = [71, 103]

        while True:
            key = stdscr.getch()

            stdscr.clear()
            stdscr.refresh()

            if key not in caracteres_permitidos:
                textPrint.print_bottom(stdscr, "Entrada Invalida!")
                textPrint.print_title(stdscr)

            else:
                if actions.verify_giveup(key) == True:
                    textPrint.print_bottom(stdscr, "Para confirmar desistencia, aperte s, caso contrario aperte outra tecla")
                    textPrint.print_multi_lines(stdscr, text_list, len(text_list))
                    textPrint.print_title(stdscr)

                    confirm_key = stdscr.getch()

                    if confirm_key in [83, 115]:
                        hasGivenUp = True
                        break

                    else:
                        stdscr.clear()
                        textPrint.print_multi_lines(stdscr, text_list, len(text_list))
                        textPrint.print_title(stdscr)
                        stdscr.refresh()


                elif key in right_answer:
                    pontos += 1
                    mensagem = ['Correto!', 'Aperte qualquer tecla para continuar']
                    textPrint.print_multi_lines(stdscr, mensagem, 2)
                    textPrint.print_title(stdscr)
                    stdscr.getch()
                    stdscr.clear()
                    break

                else:
                    pontos = 0
                    mensagem = ['Errado!', 'Aperte qualquer tecla para continuar']
                    textPrint.print_multi_lines(stdscr, mensagem, 2)
                    textPrint.print_title(stdscr)
                    hasLost = True
                    stdscr.getch()
                    stdscr.clear()
                    break

            textPrint.print_multi_lines(stdscr, text_list, len(text_list))
            textPrint.print_title(stdscr)
            stdscr.refresh()

        if hasGivenUp == True or hasLost == True:
            break

    stdscr.clear()
    textPrint.print_center(stdscr, "Pontuacao final = " + str(pontos))
    textPrint.print_title(stdscr)
    stdscr.getch()