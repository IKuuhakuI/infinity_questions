import pyrebase
import curses

def start_login(stdscr):
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

    curses.echo()
    user_name = stdscr.getstr(0,0,15)
    user_password = stdscr.getstr(2,0,15)

    stdscr.getch()

curses.wrapper(start_login)