import curses
import pyrebase

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

def update_scoreboard(top_5_list, current_score, current_user_name):
    config = {
        "apiKey": "AIzaSyBrarBhWJSP3FnNJurEAtrbmUb1fG_wZFs",
        "authDomain": "teste-python-67d43.firebaseapp.com",
        "databaseURL": "https://teste-python-67d43.firebaseio.com",
        "projectId": "teste-python-67d43",
        "storageBucket": "",
        "messagingSenderId": "581051665954",
        "appId": "1:581051665954:web:6f131448200a100689447b"
    }

    # Conexao com o Firebase
    firebase = pyrebase.initialize_app(config)

    first_score, first_name = top_5_list[0][1], top_5_list[0][0]
    second_score, second_name = top_5_list[1][1], top_5_list[1][0]
    third_score, third_name = top_5_list[2][1], top_5_list[2][0]
    fourth_score, fourth_name = top_5_list[3][1], top_5_list[3][0]
    fifth_score, fifth_name = top_5_list[4][1], top_5_list[4][0]

    # Caso fique em primeiro
    if current_score > first_score:
        new_top_5_list = [current_user_name, first_name, second_name, third_name, fourth_name]
        new_top_5_score_list = [current_score, first_score, second_score, third_score, fourth_score]

    # Caso fique em segundo
    elif current_score > second_score:
        new_top_5_list = [first_name, current_user_name, second_name, third_name, fourth_name]
        new_top_5_score_list = [first_score, current_score, second_score, third_score, fourth_score]

    # Caso fique em terceiro
    elif current_score > third_score:
        new_top_5_list = [first_name, second_name, current_user_name, third_name, fourth_name]
        new_top_5_score_list = [first_score, second_score, current_score, third_score, fourth_score]

    # Caso fique em quarto
    elif current_score > fourth_score:
        new_top_5_list = [first_name, second_name, third_name, current_user_name, fourth_name]
        new_top_5_score_list = [first_score, second_score, third_score, current_score, fourth_score]

    elif current_score > fifth_name:
        new_top_5_list = [first_name, second_name, third_name, fourth_name, current_user_name]
        new_top_5_score_list = [first_score, second_score, third_score, fourth_score, current_score]
    
    else:
        return None

    db_scoreboard = firebase.database()

    new_scoreboard = db_scoreboard.child("Highscore")

    new_scoreboard = {
        1: { 
            "user":new_top_5_list[0],
            "valor":new_top_5_score_list[0]
        },
        2: { 
            "user":new_top_5_list[1],
            "valor":new_top_5_score_list[1]
        },
        3:{ 
            "user":new_top_5_list[2],
            "valor":new_top_5_score_list[2]
        },
        4:{ 
            "user":new_top_5_list[3],
            "valor":new_top_5_score_list[3]
        },
        5: { 
            "user":new_top_5_list[4],
            "valor":new_top_5_score_list[4]
        }
    }

    db_scoreboard.update(new_scoreboard)

    #for idx in range(5):
    #   this_score = new_top_5_score_list[idx] 
    #   this_name = new_top_5_list[idx]