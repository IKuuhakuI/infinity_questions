import curses
import textPrint
import actions

#Tela inicial
def show_title_screen(stdscr):
	lista_textos_iniciais = ['Infinity Questions', 'Aperte enter para continuar']
	linhas = 2
	textPrint.print_multi_lines(stdscr, lista_textos_iniciais, linhas)
	
	while True:
		key = stdscr.getch()
		if actions.keyboard(key) == 'enter':
			break


