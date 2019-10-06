import pyrebase
import curses

def start_registrar(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

	stdscr.attron(curses.color_pair(1))

	config = {
	    "apiKey": "AIzaSyBrarBhWJSP3FnNJurEAtrbmUb1fG_wZFs",
        "authDomain": "teste-python-67d43.firebaseapp.com",
        "databaseURL": "https://teste-python-67d43.firebaseio.com",
        "projectId": "teste-python-67d43",
        "storageBucket": "",
        "messagingSenderId": "581051665954",
        "appId": "1:581051665954:web:6f131448200a100689447b"
    }

	altura_tela, largura_tela = stdscr.getmaxyx()

	# Faz conexao com Firebase
	firebase = pyrebase.initialize_app(config)

	db_quantidade_users = firebase.database()

	quantidade_users = db_quantidade_users.child("Quantidade_Users").get().val()

	name_label = "Nome: "
	pass_label = "Senha: "
	confirm_pass_label = "Confirmar senha: "

	x_nome = largura_tela//2 - 15
	y_nome = altura_tela//2

	x_senha = largura_tela//2 - 15
	y_senha = altura_tela//2 + 1

	x_confirm = largura_tela//2 - 15
	y_confirm = altura_tela//2 + 2

	stdscr.addstr(y_nome, x_nome, name_label)
	stdscr.addstr(y_senha, x_senha, pass_label)
	stdscr.addstr(y_confirm, x_confirm, confirm_pass_label)

	curses.echo()
	user_name = stdscr.getstr(y_nome,x_nome + len(name_label),15)

	curses.echo(False)
	user_password = stdscr.getstr(y_senha,x_senha + len(pass_label),15)

	user_confirm_password = stdscr.getstr(y_confirm, x_confirm + len(confirm_pass_label), 15)

	stdscr.refresh()
	stdscr.getch()

curses.wrapper(start_registrar)