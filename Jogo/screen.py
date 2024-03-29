import os
import sys

import actions
import curses
import menu
import scoreboard
import textPrint

######### REDIMENSIONA A TELA PARA LINUX ##################
def resize_screen_linux():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=135))

def resize_screen_windows():
	os.system('mode con: cols=135 lines=40')

######### REDIMENSIONA A TELA PARA WINDOWS ##################
def show_title_screen(stdscr):
	lista_textos_iniciais = ['Infinity Questions', 'Aperte enter para continuar']
	linhas = 2
	textPrint.print_multi_lines(stdscr, lista_textos_iniciais, linhas)
	
	while True:
		key = stdscr.getch()
		if actions.keyboard(key) == 'enter':
			break

######### TELA DE BEM VINDO ################################
def show_welcome_screen(stdscr):
	lista_texto_rules = ['Bem Vindo ao Infinity Questions!','O objetivo é ver quem consegue acertar o maximo de perguntas sem errar!','Você acha que consegue quebrar o recorde?','Para continuar, aperte qualquer coisa...']
	linhas = 4
	textPrint.print_multi_lines(stdscr, lista_texto_rules, linhas)
	stdscr.getch()

######### REGRAS DO JOGO #########################################
def show_rules_screen(stdscr):
	lista_texto_regras = ['Regras:', '1- Responda somente com (a), (b), (c) ou (d)', '2- Caso nao saiba responder e queira desistir, digite (g)', '3- Caso erre a resposta, o jogo acaba e voce nao ganha nenhum ponto', '4- Caso ganhe ou desista, a quatidade de pontos vai ser quantas peguntas voce acertou', 'Para continuar aperte qualquer coisa...']
	linhas = 6
	textPrint.print_multi_lines(stdscr, lista_texto_regras, linhas)
	stdscr.getch()

######### REGRAS PARA ADICIONAR/EDITAR PERGUNTAS ##################
def show_questions_rules_screen(stdscr, current_row_idx):
	continuar_voltar_menu = ('Continuar', 'Voltar')

	stdscr.clear()

	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

	stdscr.attron(curses.color_pair(1))

	textPrint.print_title(stdscr)

	linha1 = "Ok! Antes de comecar a adicionar/alterar uma pergunta, leia as regras atentamente!"
	linha2 = "Regras: "
	
	linha3 = "1 - Ao editar uma pergunta, voce deve informar o numero dela"
	linha4 = "2 - Em seguida, voce ira informar a nova pergunta"
	linha5 = "3 - Apos isso, voce devera informar 4 possiveis respostas"
	linha6 = "4 - Das respostas, somente 1 podera ser a resposta correta"
	linha7 = "5 - Caso voce informe mais de 1 resposta correta, o programa ira recusar"

	regras_para_adicionar = [linha1, linha2, linha3, linha4, linha5, linha6, linha7]

	# Imprime as regras no centro da tela
	textPrint.print_multi_lines(stdscr, regras_para_adicionar, 7)
        
	# Menu de continuar / voltar
	menu.horizontal_menu(stdscr, current_row_idx, continuar_voltar_menu)
        
	stdscr.refresh()
###################REGRAS PARA EXCLUIR UMA PERGUNTA######################
def show_erase_rules_screen(stdscr,current_row_idx):
	continuar_voltar_menu = ('Continuar','Voltar')

	stdscr.clear()

	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

	stdscr.attron(curses.color_pair(1))

	textPrint.print_title(stdscr)

	linha1 = "Ok! Antes de começar a excluir uma pergunta, leia as regras atentamente"
	linha2 = "Regras: "

	linha3 = "1 - Ao excluir uma pergunta, voce deve informar o numero dela"
	linha4 = "2 - Em seguida, voce ira informar se deseja realmente exclui-la"

	regras_excluir = [linha1, linha2, linha3, linha4]

	#Imprime as regras no centro da tela
	textPrint.print_multi_lines(stdscr, regras_excluir, 4)

	#Menu de continuar / voltar
	menu.horizontal_menu(stdscr, current_row_idx, continuar_voltar_menu)

	stdscr.refresh()

# Tela de fim de jogo
def show_end_screen(stdscr, pontuacao, personal_record, global_record):
	curses.curs_set(0)
	stdscr.clear()

	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

	textPrint.print_title(stdscr)
	texto_pontos = "Pontuacao: " + str(pontuacao)
	
	texto_final = [texto_pontos]

	if global_record != None:
		if global_record == 'First':
			text_global = 1

		elif global_record == 'Second':
			text_global = 2

		elif global_record == 'Third':
			text_global = 3

		elif global_record == 'Fourth':
			text_global = 4

		else:
			text_global = 5

		texto_global_record = "Parabens, voce obteu a " + str(text_global) + "ª posicao no scoreboard!"
		texto_final.append(texto_global_record)

	if global_record != "First":
		texto_tentativa = "Que tal tentar mais uma vez? Talvez voce consiga quebrar o recorde atual!"
		texto_final.append(texto_tentativa)
	
	if personal_record == True:
		texto_recorde_pessoal = "Novo recorde pessoal! Parabens!"

		texto_final.append(texto_recorde_pessoal)

	textPrint.print_multi_lines(stdscr, texto_final, len(texto_final))

	botao = ['Continuar']

	menu.std_btn(stdscr, 0, botao)

	while True:
		key = stdscr.getch()

		if actions.keyboard(key) == 'enter':
			break

# Tela de "deseja sair"
def show_deseja_sair(stdscr):
	curses.curs_set(0)

	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

	textPrint.print_title(stdscr)
	textPrint.print_center(stdscr, 'Tem certeza que deseja sair?')
	botao = ['Sim', 'Não']
	selected_row_idx = 0
	stdscr.refresh()
	menu.horizontal_menu(stdscr, selected_row_idx, botao)
	
	while True:
		key = stdscr.getch()
		stdscr.refresh()
		if actions.keyboard(key) == 'left' and selected_row_idx > 0:
			selected_row_idx -= 1

		elif actions.keyboard(key) == 'right' and selected_row_idx < 1:
			selected_row_idx += 1

		elif actions.keyboard(key) == 'enter':
			if selected_row_idx == 0: #SIM
				return True

			elif selected_row_idx == 1: #NAO
				return False
		
		stdscr.clear()
		textPrint.print_title(stdscr)
		textPrint.print_center(stdscr, 'Tem certeza que deseja sair?')
		menu.horizontal_menu(stdscr, selected_row_idx, botao)
		stdscr.refresh()

# Tela de pergunta apagada
def show_pergunta_apagada(stdscr):
	curses.curs_set(0)

	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
	textPrint.print_title(stdscr)
	textPrint.print_center(stdscr, 'Pergunta Apagada!')
	botao = ["Continuar"]
	menu.std_btn(stdscr, 0, botao)
	stdscr.refresh()
	key = stdscr.getch()
	while True:
		if actions.keyboard(key) == 'enter':
			break

#Adicionando tela de Scoreboard:
def show_scoreboard(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    menu_scoreboard = ["Voltar"]

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(1))

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    textPrint.print_title(stdscr)

    textPrint.print_center(stdscr, "Carregando...")
    stdscr.refresh()

    textPrint.print_title(stdscr)

    textPrint.erase_center(stdscr, "Carregando...")

    scoreboard.print_scoreboard(stdscr)

    menu.std_btn(stdscr, 0, menu_scoreboard)

    textPrint.print_title(stdscr)
    
    stdscr.refresh()

    while True:    
        key = stdscr.getch()   
        if actions.keyboard(key) == 'enter':
            break