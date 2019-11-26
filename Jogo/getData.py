import pyrebase
import random

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

def random_questions(question_list):
    random.shuffle(question_list)
    return question_list

def create_question_list(question_list):
    final_list = []
    for idx in range(len(question_list)):
        dict_quest = {"Id":idx + 1,
                      "Pergunta":question_list[idx]["Pergunta"]}
        final_list.append(dict_quest)

    return final_list

def get_questions_data():
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

    db_questions = firebase.database()

    question_list = db_questions.child('Perguntas').get().val()

    if question_list[0] == None:
        question_list.pop(0)

    final_list = create_question_list(question_list)

    final_list = random_questions(final_list)

    return final_list

def get_right_answer(dict_respostas):
    if dict_respostas['a']['isCorrect'] == True:
        return [65,97]
    
    elif dict_respostas['b']['isCorrect'] == True:
        return [66,98]
    
    elif dict_respostas['c']['isCorrect'] == True:
        return [67, 99]

    return [68,100]

def get_answer(id):
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

    db_answers = firebase.database()

    answers_list = db_answers.child("Respostas").child(id).get().val()

    return answers_list
