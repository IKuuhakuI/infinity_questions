import pyrebase
import curses
import time

import menu
import textPrint
import actions

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

    text_list = []

    for score in range(len(score_list)):
        user_name = score_list[score][0]
        user_score = score_list[score][1]

        if user_name == "Nil":
            text = str(score + 1) + "- --------------" 
        else:
            text = str(score + 1) + "- " + user_name + " - Score: " + str(user_score)

        text_list.append(text)

        #x = largura_tela//2 - 5 - len(text)//2
        #y = altura_tela//2 - len(score_list) + score

        #stdscr.addstr(y, x, text)

    textPrint.print_multi_lines(stdscr, text_list, len(text_list))

def show_scoreboard(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    menu_scoreboard = ["Voltar"]

    # Coloca a cor atual como sendo o primeiro par
    stdscr.attron(curses.color_pair(1))

    # Altura e Largura da Tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    textPrint.print_center(stdscr, "Carregando...")
    stdscr.refresh()

    textPrint.print_title(stdscr)

    textPrint.erase_center(stdscr, "Carregando...")

    print_scoreboard(stdscr)

    menu.back_btn(stdscr, 0, menu_scoreboard)

    textPrint.print_title(stdscr)
    
    stdscr.refresh()

    while True:    
        key = stdscr.getch()   
        if actions.keyboard(key) == 'enter':
            break

    