import pyrebase
import curses

import textPrint
import actions
import menu

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

	exitRegister = False

	exitMessage = "Para sair, digite /exit no nome ou senha"

	yes_no_menu = ('Sim', 'Nao')

	while True:
		textPrint.print_bottom(stdscr, exitMessage)
		textPrint.print_title(stdscr)

		curses.curs_set(True)

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

		user_name = user_name.decode("utf-8")

		if actions.verify_exit(user_name) == True:
			exitRegister = True
			break

		curses.echo(False)
		user_password = stdscr.getstr(y_senha,x_senha + len(pass_label),15)
		user_password = user_password.decode("utf-8")

		if actions.verify_exit(user_password) == True:
			exitRegister = True
			break

		user_confirm_password = stdscr.getstr(y_confirm, x_confirm + len(confirm_pass_label), 15)
		user_confirm_password = user_confirm_password.decode("utf-8")

		if actions.verify_exit(user_confirm_password) == True:
			exitRegister = True
			break

		isUnique = True

		db_all_users = firebase.database()

		stdscr.clear()

		textPrint.print_title(stdscr)
		textPrint.print_center(stdscr, "Aguarde...")

		stdscr.refresh()

		for user in range(quantidade_users):
			this_user = db_all_users.child("Users").child(user + 1).child("Name").get().val()

			if user_name == this_user:
				isUnique = False
				break


		if isUnique == True and user_password == user_confirm_password and len(user_name) > 3 and len(user_name) <= 20 and len(user_password) > 3 and len(user_password) <= 20:
			stdscr.clear()

			textPrint.print_title(stdscr)
			sucess_message = ["Usuario " + str(user_name) + " registrado!", "Pressione qualquer tecla para continuar"]
			textPrint.print_multi_lines(stdscr,sucess_message, 2)
			
			stdscr.refresh()
			stdscr.getch()
			stdscr.clear()
			break

		else:
			stdscr.clear()

			tentar_novamente = "Deseja tentar novamente?"
			error_message = ["ERRO AO CRIAR USUARIO", tentar_novamente]

			current_row_idx = 0

			while True:
				textPrint.print_title(stdscr)
				textPrint.print_multi_lines(stdscr, error_message, 2)
				menu.horizontal_menu(stdscr, current_row_idx, yes_no_menu)
			
				stdscr.refresh()

				key = stdscr.getch()

				if key == curses.KEY_LEFT and current_row_idx > 0:
				    current_row_idx -= 1

				elif key == curses.KEY_RIGHT and current_row_idx < 1:
				    current_row_idx += 1

				elif key == curses.KEY_ENTER or key in [10,13]:
				    if current_row_idx == 0:
				        exitRegister = False
				        break
				    else:
				        exitRegister = True
				        break

		stdscr.clear()

		if exitRegister == True:
			break

	if exitRegister == False:
		new_user_id = quantidade_users + 1
		db_new_user = firebase.database()
		new_user = db_new_user.child("Users").child(new_user_id)

		new_user = {
			"Name": user_name,
			"Pass": user_password,
			"Highscore": 0,
			"Questions": {"Quantidade_enviadas":0}
		}

		db_qtd_user = firebase.database()

		qtd_user = {
			"Quantidade_Users": new_user_id
		}

		db_new_user.update(new_user)
		db_qtd_user.update(qtd_user)

		stdscr.refresh()