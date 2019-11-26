import sys

import curses
import textPrint
import actions
import menu
import scoreboard

def resize_screen():
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=40, cols=135))

# Tela inicial
def show_title_screen(stdscr):
	lista_textos_iniciais = ['Infinity Questions', 'Aperte enter para continuar']
	linhas = 2
	textPrint.print_multi_lines(stdscr, lista_textos_iniciais, linhas)
	
	while True:
		key = stdscr.getch()
		if actions.keyboard(key) == 'enter':
			break

# Tela que vem logo apos o usuario clicar em 'jogar'
def show_rules_screen(stdscr):
	lista_texto_rules = ['Bem Vindo ao Infinity Questions!','O objetivo é ver quem consegue acertar o maximo de perguntas sem errar!','Você acha que consegue quebrar o recorde?','Para continuar, aperte qualquer coisa...']
	linhas = 4
	textPrint.print_multi_lines(stdscr, lista_texto_rules, linhas)
	stdscr.getch()

# Tela de novo recorde global 
def show_new_global_record(stdscr, pontuacao):
	textPrint.print_title(stdscr)
	lista_texto_global = ['pontuacao: ' + str(pontuacao), 'Novo recorde global! Parabens!']
	linhas = 2
	textPrint.print_multi_lines(stdscr, lista_texto_global, linhas)
	botao = ["continuar"]
	menu.std_btn(stdscr, 0, botao)
	key = stdscr.getch()
	while True:
		if actions.keyboard(key) == 'enter':
			break

# Tela de novo recorde pessoal
def show_new_personal_record(stdscr, pontuacao):
	textPrint.print_title(stdscr)
	lista_texto_personal = ['pontuacao: ' + str(pontuacao), 'Novo recorde pessoal! Parabens!']
	linhas = 2
	textPrint.print_multi_lines(stdscr, lista_texto_personal, linhas)
	botao = ["continuar"]
	menu.std_btn(stdscr, 0, botao)
	key = stdscr.getch()
	while True:
		if actions.keyboard(key) == 'enter':
			break

# Tela de novo recorde global e pessoal ao mesmo tempo
def new_global_personal_record(stdscr, pontuacao):
	curses.curs_set(0)

	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
	textPrint.print_title(stdscr)
	texto_global_pessoal = ['Pontuacão: ' + str(pontuacao), 'Novo recorde pessoal! Parabens!', 'Novo recorde Global! Parabens!']
	linhas = 3
	textPrint.print_multi_lines(stdscr, texto_global_pessoal, linhas)
	botao = ['Continuar']
	menu.std_btn(stdscr, 0, botao)
	key = stdscr.getch()
	while True:
		if actions.keyboard(key) == 'enter':
			break

# Tela caso nao consiga nenhum novo recorde
def show_nenhum_recorde(stdscr, pontuacao, recorde_global, recorde_pessoal):
	textPrint.print_title(stdscr)
	lista_texto_sem_recorde = ['Resposta Errada!! Fim de Jogo :(','Pontuacao: ' + str(pontuacao), 'Que tal tentar mais uma vez? Talvez voce consiga quebrar o recorde atual!', 'Recorde global :' + str(recorde_global), 'Recorde pessoal :' + str(recorde_pessoal)]
	linhas = 5
	textPrint.print_multi_lines(stdscr, lista_texto_sem_recorde, linhas)
	botao = ["continuar"]
	menu.std_btn(stdscr, 0, botao)
	key = stdscr.getch()
	while True:
		if actions.keyboard(key) == 'enter':
			break
	
# Tela de "deseja sair"
def deseja_sair(stdscr):
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
			break
		stdscr.clear()
		textPrint.print_title(stdscr)
		textPrint.print_center(stdscr, 'Tem certeza que deseja sair?')
		menu.horizontal_menu(stdscr, selected_row_idx, botao)
		stdscr.refresh()

# Tela de pergunta apagada
def pergunta_apagada(stdscr):
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
