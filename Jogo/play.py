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

    textPrint.print_center(stdscr, lista_perguntas[0]["Pergunta"])

    stdscr.getch()

curses.wrapper(final_game)