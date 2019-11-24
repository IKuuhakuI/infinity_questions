import pyrebase
import curses

import textPrint
import actions
import timer
import menu

def start_login(stdscr):
    yes_no_menu = ('Sim', 'Nao')

    # Define as cores que serao utilizadas
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(1))

    
    # Configuracoes do banco de dados
    config = {
        "apiKey": "AIzaSyBrarBhWJSP3FnNJurEAtrbmUb1fG_wZFs",
        "authDomain": "teste-python-67d43.firebaseapp.com",
        "databaseURL": "https://teste-python-67d43.firebaseio.com",
        "projectId": "teste-python-67d43",
        "storageBucket": "",
        "messagingSenderId": "581051665954",
        "appId": "1:581051665954:web:6f131448200a100689447b"
    }
    
    # Altura e largura da tela
    altura_tela, largura_tela = stdscr.getmaxyx()
    
    # Faz conexao com Firebase
    firebase = pyrebase.initialize_app(config)

    exitMessage = "Para sair, digite /exit no nome ou senha"

    stop = False

    tentativas_restantes = 8

    while True:
        textPrint.print_title(stdscr)
        textPrint.print_bottom(stdscr, exitMessage)

        curses.curs_set(True)

        # Label das areas do nome e da senha
        name_label = "Nome: "
        pass_label = "Senha: "
    
        # Coordenadas do label do nome
        x_nome = largura_tela//2 - 15
        y_nome = altura_tela//2
    
        # Coordenadas do label da senha
        x_senha = largura_tela//2 - 15
        y_senha = altura_tela//2 + 1
    
        # Imprime o label do nome e da senha na tela
        stdscr.addstr(y_nome, x_nome, name_label)
        stdscr.addstr(y_senha, x_senha, pass_label)
    
        # Permite o usuario ler o que esta digitando
        curses.echo()

        # Le o nome do teclado
        user_name = stdscr.getstr(y_nome,x_nome + len(name_label),15)
        user_name = user_name.decode("utf-8")
        
        if actions.verify_exit(user_name) == True:
            break
        
        # Esconde o que o usuario esta escrevendo
        curses.echo(False)
    
        # Le a senha do teclado
        user_password = stdscr.getstr(y_senha,x_senha + len(pass_label),15)
        user_password = user_password.decode("utf-8")

        if actions.verify_exit(user_password) == True:
            break

        # Conexao com o banco de dados
        db_quantidade_users = firebase.database()
        # Pega o valor da quantidade de usuarios
        quantidade_users = db_quantidade_users.child("Quantidade_Users").get().val()
    
        # Variavel de controle
        logged_in = False
    
        # Converte o que foi lido de bytes para string
        
        stdscr.clear()

        textPrint.print_title(stdscr)
        textPrint.print_center(stdscr, "Aguarde...")
        stdscr.refresh()

        # Loop que verifica se o user existe e se a senha e correta
        for user_id in range(1, quantidade_users + 1):
            # Conexao com o banco de dados
            db_user_name = firebase.database()
            db_user_pass = firebase.database()
        
            # Pega o usuario e senha atual no banco de dados
            current_user_name = db_user_name.child("Users").child(user_id).child("Name").get().val()
            current_user_pass = db_user_pass.child("Users").child(user_id).child("Pass").get().val()
        
            # Converte os dados para string
            current_user_name = str(current_user_name)
            current_user_pass = str(current_user_pass)
        
            # Caso o user exista e a senha esteja correta
            if current_user_name == user_name and current_user_pass == user_password:
                # Muda o estado para True
                logged_in = True

                break
    
        # Limpa a tela
        stdscr.clear()
        
        textPrint.print_title(stdscr)
        
        curses.curs_set(0)

        # Caso esteja logado
        if logged_in == True:
            tentativas_restantes = 8

            text_sucesso = ["Bem vindo " + user_name, "Aperte qualquer coisa para continuar"]

            textPrint.print_multi_lines(stdscr, text_sucesso, 2)
            
            stdscr.refresh()
            stdscr.getch()
            break

        # Caso falhe em logar
        else:
            tentativas_restantes -= 1

            current_row_idx = 0

            while True:
                textPrint.print_title(stdscr)

                menu.horizontal_menu(stdscr, current_row_idx, yes_no_menu)

                text_tentativas = "Tentativas Restantes: " + str(tentativas_restantes)

                tentar_novamente = "Deseja tentar novamente?"

                if(tentativas_restantes == 0):
                    text_error = ["ERRO AO EFETUAR LOGIN", "A tela ira bloquear por 1 minuto", tentar_novamente]
                else:
                    text_error = ["ERRO AO EFETUAR LOGIN", text_tentativas, tentar_novamente]

                textPrint.print_multi_lines(stdscr, text_error, 3)
                        
                stdscr.refresh()

                key = stdscr.getch()

                if key == curses.KEY_LEFT and current_row_idx > 0:
                    current_row_idx -= 1

                elif key == curses.KEY_RIGHT and current_row_idx < 1:
                    current_row_idx += 1

                elif key == curses.KEY_ENTER or key in [10,13]:
                    if tentativas_restantes == 0:
                        timer.block_screen(stdscr)
                        stdscr.clear()

                    if current_row_idx == 0:
                        stop = False
                        break
                    else:
                        stop = True
                        break

                stdscr.clear()

        stdscr.clear()

        if stop == True:
            break
                

