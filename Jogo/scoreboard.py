import pyrebase
import curses

import menu

def show_scoreboard(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    menu_scoreboard = ["Voltar"]

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(2))

    config = {
        "apiKey": "AIzaSyBrarBhWJSP3FnNJurEAtrbmUb1fG_wZFs",
        "authDomain": "teste-python-67d43.firebaseapp.com",
        "databaseURL": "https://teste-python-67d43.firebaseio.com",
        "projectId": "teste-python-67d43",
        "storageBucket": "",
        "messagingSenderId": "581051665954",
        "appId": "1:581051665954:web:6f131448200a100689447b"
    }

    # Faz conexao com Firebase
    firebase = pyrebase.initialize_app(config)

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    title = "Infinity Questions"

    # Coordenadas do texto
    x = largura_tela//2 - len(title)//2
    y = altura_tela//8
    
    menu.back_btn(stdscr, 0, menu_scoreboard)
    stdscr.addstr(y, x, title)

    stdscr.getch()

    stdscr.refresh()

curses.wrapper(show_scoreboard)