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
        pergunta_atual = "Pergunta: " + lista_perguntas[pergunta]["Pergunta"]
        id_atual = lista_perguntas[pergunta]["Id"]
        
        dict_respostas = getQuestions.get_answer(id_atual)
        right_answer = getQuestions.get_right_answer(dict_respostas)
        
        resposta_a = 'a)' + str(dict_respostas['a']['valor'])
        resposta_b = 'b)' + str(dict_respostas['b']['valor'])
        resposta_c = 'c)' + str(dict_respostas['c']['valor'])
        resposta_d = 'd)' + str(dict_respostas['d']['valor'])

        text_list = [pergunta_atual, resposta_a, resposta_b, resposta_c, resposta_d]

        textPrint.print_multi_lines(stdscr, text_list, len(text_list))

        key = stdscr.getch()

        stdscr.clear()
        stdscr.refresh()

        if key in right_answer:
            textPrint.print_center(stdscr, "Correto")
        else:
            textPrint.print_center(stdscr, "Errado")

        stdscr.getch()
        
curses.wrapper(final_game)