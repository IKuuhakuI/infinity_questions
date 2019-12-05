# Criando arquivo play.py
#arquivo que vai ficar a logica do jogo propriamente dito
#Aqui dentro vai ser chamado as telas de recorde pessoal, global ou não recorde
import curses

import actions
import getData
import screen
import scoreboard
import textPrint 

def final_game(stdscr, current_user_name, current_user_id, current_user_high_score):
    # A, B, C, D, G, a, b, c, d, g
    caracteres_permitidos = [65,66,67,68,71,97,98,99,100,103]

    # Imprime titulo do jogo
    textPrint.print_title(stdscr)

    # Imprimir mensagem de 'Bem Vindos' 
    screen.show_welcome_screen(stdscr)
    stdscr.clear()

    # Imprimir Titulo do jogo
    textPrint.print_title(stdscr)

    # Imprime regras do jogo
    screen.show_rules_screen(stdscr)
    stdscr.clear()

    # Imprime titulo do jogo
    textPrint.print_title(stdscr)
    # Tela de carregamento
    textPrint.print_center(stdscr, "Carregando...")
    stdscr.refresh()

    # Lista com as perguntas do Jogo
    lista_perguntas = getData.get_questions_data()
    stdscr.clear()

    hasGivenUp = False
    hasLost = False
    hasWon = False

    pontos = 0

    for pergunta in range(len(lista_perguntas)):
        pergunta_atual = "Pergunta " + str(pergunta + 1) + ": " + lista_perguntas[pergunta]["Pergunta"]
        id_atual = lista_perguntas[pergunta]["Id"]
        
        dict_respostas = getData.get_answer(id_atual)
        right_answer = getData.get_right_answer(dict_respostas)
        
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
    textPrint.print_title(stdscr)
    textPrint.print_center(stdscr, "Carregando...")
    stdscr.refresh()
    # Alterar scoreboard e recorde pessoal
    top_5_list = scoreboard.get_top_5_high_score()

    globalRecord = scoreboard.update_scoreboard(top_5_list, pontos, current_user_name)
    personalRecord = scoreboard.set_user_high_score(pontos, current_user_high_score, current_user_id)


    # Logica para imprimir na tela mensagens com a pontuacao e as congratulaçoes caso haja novo recorde pessoal ou global, ou se nao houver novo recorde 

    if globalRecord == "First":
        stdscr.clear()
        screen.show_new_global_record(stdscr, pontos)
      

    elif globalRecord == "Second" and personalRecord == True: 
        stdscr.clear()
        screen.show_new_global_personal_record(stdscr, pontos, actions.verify_posicao(globalRecord))
       

    elif globalRecord == "Third" and personalRecord == True: 
        stdscr.clear()
        screen.show_new_global_personal_record(stdscr, pontos, actions.verify_posicao(globalRecord))
       

    elif globalRecord == "Fourth" and personalRecord == True: 
        stdscr.clear()
        screen.show_new_global_personal_record(stdscr, pontos, actions.verify_posicao(globalRecord))
    

    elif globalRecord == "Fifth" and personalRecord == True: 
        stdscr.clear()
        screen.show_new_global_personal_record(stdscr, pontos, actions.verify_posicao(globalRecord))
    

    elif globalRecord == "First" and personalRecord == False: 
        stdscr.clear()
        screen.show_new_posicao_record(stdscr, pontos, actions.verify_posicao(globalRecord))

    elif globalRecord == "Second" and personalRecord == False: 
        stdscr.clear()
        screen.show_new_posicao_record(stdscr, pontos, actions.verify_posicao(globalRecord))
    
    elif globalRecord == "Third" and personalRecord == False: 
        stdscr.clear()
        screen.show_new_posicao_record(stdscr, pontos, actions.verify_posicao(globalRecord))
    
    elif globalRecord == "Fourth" and personalRecord == False: 
        stdscr.clear()
        screen.show_new_posicao_record(stdscr, pontos, actions.verify_posicao(globalRecord))
    
    elif globalRecord == "Fifth" and personalRecord == False: 
        stdscr.clear()
        screen.show_new_posicao_record(stdscr, pontos, actions.verify_posicao(globalRecord))

    
    elif globalRecord == None and personalRecord == True:
        stdscr.clear()
        screen.show_new_personal_record(stdscr, pontos)
       
    else:
    #elif globalRecord != None and personalRecord == False:
        
        recordeGlobal = scoreboard.retorna_global_record(stdscr)
        recordePessoal = scoreboard.retorna_personal_record(stdscr, current_user_id)
        stdscr.clear()

        screen.show_nenhum_recorde(stdscr, pontos, recordeGlobal, recordePessoal)



        #stdscr.clear()
        #pontuacao_final = str(pontos)
        #textPrint.print_center(stdscr, pontuacao_final)
        #textPrint.print_title(stdscr)
        #stdscr.getch()