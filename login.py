import pyrebase
import curses

def start_login(stdscr):
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

    name_label = "Nome: "
    pass_label = "Senha: "

    x_nome = largura_tela//2 - 15
    y_nome = altura_tela//2

    x_senha = largura_tela//2 - 15
    y_senha = altura_tela//2 + 1

    stdscr.addstr(y_nome, x_nome, name_label)
    stdscr.addstr(y_senha, x_senha, pass_label)

    curses.echo()
    user_name = stdscr.getstr(y_nome,x_nome + len(name_label),15)

    curses.echo(False)
    user_password = stdscr.getstr(y_senha,x_senha + len(pass_label),15)

    db_quantidade_users = firebase.database()
    quantidade_users = db_quantidade_users.child("Quantidade_Users").get().val()

    logged_in = False

    user_name = user_name.decode("utf-8")
    user_password = user_password.decode("utf-8")

    for user_id in range(1, quantidade_users + 1):
        db_user_name = firebase.database()
        db_user_pass = firebase.database()

        current_user_name = db_user_name.child("Users").child(user_id).child("Name").get().val()
        current_user_pass = db_user_pass.child("Users").child(user_id).child("Pass").get().val()

        current_user_name = str(current_user_name)
        current_user_pass = str(current_user_pass)

        stdscr.clear()

        if current_user_name == user_name and current_user_pass == user_password:
            stdscr.clear()
            logged_in = True

            break

    stdscr.clear()

    x_mensagem = largura_tela//2 - len("Bem vindo") // 2
    y_mensagem = altura_tela//2

    if logged_in == True:
        stdscr.addstr(y_mensagem,x_mensagem,"Bem vindo")
        stdscr.addstr(y_mensagem + 1, x_mensagem + (len("Bem vindo") - len("Aperte qualquer coisa para continuar"))//2, "Aperte qualquer coisa para continuar")
        stdscr.refresh()
        stdscr.getch()


    else:
        stdscr.addstr(y_mensagem, x_mensagem + (len("Bem vindo") - len("ERRO AO EFETUAR LOGIN")) // 2,"ERRO AO EFETUAR LOGIN")
        stdscr.addstr(y_mensagem + 1, x_mensagem + (len("Bem vindo")-len("Aperte qualquer coisa para continuar"))//2, "Aperte qualquer coisa para continuar")
        stdscr.refresh()
        stdscr.getch()


curses.wrapper(start_login)