import pyrebase
import curses

import menu

def get_top_5_high_score():
    config = {
        "apiKey": "AIzaSyBrarBhWJSP3FnNJurEAtrbmUb1fG_wZFs",
        "authDomain": "teste-python-67d43.firebaseapp.com",
        "databaseURL": "https://teste-python-67d43.firebaseio.com",
        "projectId": "teste-python-67d43",
        "storageBucket": "",
        "messagingSenderId": "581051665954",
        "appId": "1:581051665954:web:6f131448200a100689447b"
    }

    firebase = pyrebase.initialize_app(config)

    score_list = []

    for idx in range(1, 6):
        db_high_score = firebase.database()

        user = db_high_score.child("Highscore").child(idx).child("user").get().val()
        score = db_high_score.child("Highscore").child(idx).child("valor").get().val()

        par = (user, score)

        score_list.append(par)

    return score_list

def print_scoreboard(stdscr):
    altura_tela, largura_tela = stdscr.getmaxyx()

    score_list = get_top_5_high_score()

    for score in range(len(score_list)):
        user_name = score_list[score][0]
        user_score = score_list[score][1]

        if user_name == "Nil":
            text = str(score + 1) + "-\t----------------" 
        else:
            text = str(score + 1) + "-\t" + user_name + "\t- Score: " + str(user_score)

        x = largura_tela//2 - 5 - len(text)//2
        y = altura_tela//2 - len(score_list) + score

        stdscr.addstr(y, x, text)

def show_scoreboard(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    menu_scoreboard = ["Voltar"]

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(2))

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    title = "Infinity Questions"

    # Coordenadas do texto
    x_title = largura_tela//2 - len(title)//2
    y_title = altura_tela//8
    
    menu.back_btn(stdscr, 0, menu_scoreboard)
    stdscr.addstr(y_title, x_title, title)

    print_scoreboard(stdscr)

    stdscr.getch()

    stdscr.refresh()

curses.wrapper(show_scoreboard)