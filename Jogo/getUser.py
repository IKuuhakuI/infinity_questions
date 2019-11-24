import pyrebase

def get_user_data(user_id):
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

    firebase = pyrebase.initialize_app(config)

    db_current_user_data = firebase.database()

    current_user_data = db_current_user_data.child("Users").child(user_id).get().val()

    return current_user_data.copy()

