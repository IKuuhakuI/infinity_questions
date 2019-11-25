import curses
import textPrint
import actions
import menu

#Tela inicial
def show_title_screen(stdscr):
	lista_textos_iniciais = ['Infinity Questions', 'Aperte enter para continuar']
	linhas = 2
	textPrint.print_multi_lines(stdscr, lista_textos_iniciais, linhas)
	
	while True:
		key = stdscr.getch()
		if actions.keyboard(key) == 'enter':
			break
# tela que vem logo apos o usuario entrar em "jogar"
def show_welcome_screen(stdscr):
	lista_texto_welcome = ['Bem Vindo ao Infinity Questions!','O objetivo é ver quem consegue acertar o maximo de perguntas sem errar!','Você acha que consegue quebrar o recorde?','Para continuar, aperte qualquer coisa...']
	linhas = 4
	textPrint.print_multi_lines(stdscr, lista_texto_welcome, linhas)
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

