# Arquivo com funcionalidades referentes as
# perguntas adicionadas por usuarios no jogo

# Bibliotecas existentes
import curses
import pyrebase

# Arquivos de funcoes criadas 
import actions
import getData
import math
import menu
import screen
import textPrint

############### ADICIONAR PERGUNTAS ################################
def adiciona_pergunta(stdscr, current_user_id, current_user_data):
    current_row_idx = 0

    while True:   
        screen.show_questions_rules_screen(stdscr, current_row_idx)

        # Entrada do teclado
        key = stdscr.getch()

        # Navegar pelo menu
        if actions.keyboard(key) == 'left' and current_row_idx > 0:
            current_row_idx -= 1
        elif actions.keyboard(key) == 'right' and current_row_idx < 1:
            current_row_idx += 1

        # Caso selecione uma opcao
        elif actions.keyboard(key) == 'enter':
            # Caso selecione continuar
            if current_row_idx == 0:
                stdscr.clear()

                # Funcao que adiciona perguntas no jogo
                escreve_pergunta(stdscr, current_user_id, current_user_data, "Adicionar", -1)
                
                stdscr.clear()

            # Caso selecione voltar
            else:
                break

################### USER INFORMA A PERGUNTA #################

# Entada: interface grafica, id do user, dados do user. modo (Adicionar/ Editar)
def escreve_pergunta(stdscr, current_user_id, current_user_data, mode, question_id):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    stdscr.attron(curses.color_pair(1))

    # Conexao com o banco de dados
    config = {
        "apiKey": "AIzaSyBrarBhWJSP3FnNJurEAtrbmUb1fG_wZFs",
        "authDomain": "teste-python-67d43.firebaseapp.com",
        "databaseURL": "https://teste-python-67d43.firebaseio.com",
        "projectId": "teste-python-67d43",
        "storageBucket": "",
        "messagingSenderId": "581051665954",
        "appId": "1:581051665954:web:6f131448200a100689447b"
    }

    # Dimensoes da tela
    altura_tela, largura_tela = stdscr.getmaxyx()

    # Faz conexao com Firebase
    firebase = pyrebase.initialize_app(config)

    # Pega a quantidade de perguntas que existem no jogo
    db_quantidade_perguntas = firebase.database()
    quantidade_perguntas = db_quantidade_perguntas.child("Quantidade_Perguntas").get().val()

    # Variavel de controle
    exitRegister = False

    exitMessage = "Para sair, digite /exit"

    yes_no_menu = ('Sim', 'Nao')

    while True:
        # Imprime mensagem para sair da tela
        textPrint.print_bottom(stdscr, exitMessage)
        # Imprime o titulo do jogo
        textPrint.print_title(stdscr)

        # Habilita visualizacao do cursor
        curses.curs_set(True)

        if mode == "Editar":
            question_text = getData.get_one_question_data(question_id)
            textPrint.print_center(stdscr, "Pergunta atual: " + question_text)
            pergunta_label = "Pergunta editada: "

        else:
            pergunta_label = "Informe a pergunta: "

        # Coordenadas da area para escrever a pergunta
        x_pergunta = largura_tela//2 - 50 - len(pergunta_label)//2
        y_pergunta = altura_tela//2

        # Imprime a pergunta na tela
        stdscr.addstr(y_pergunta, x_pergunta, pergunta_label)

        # Habilita para o usuarop escrever na tela
        curses.echo()

        user_pergunta = stdscr.getstr(y_pergunta, x_pergunta + len(pergunta_label),100)
        user_pergunta = user_pergunta.decode("utf-8")
        # Verifica se usuario digitou /exit

        if actions.verify_exit(user_pergunta) == True:
            # variavel que indica que o user saiu
            exitRegister = True
            break

        # Desabilita a visualização do cursor 
        curses.echo(False)
        
        # Variavel que verifica se pergunta e unica
        isUnique = True

        # Dados de todas as perguntas
        db_all_perguntas = firebase.database()
        stdscr.clear()

        textPrint.print_title(stdscr)
        textPrint.print_center(stdscr, "Aguarde...")

        stdscr.refresh()

        # Loop para verificar se pergunta e unica
        for pergunta in range (quantidade_perguntas):
            # Dados da pergunta atual
            this_pergunta = db_all_perguntas.child("Perguntas").child(pergunta + 1).child("Pergunta").get().val()

            if user_pergunta == this_pergunta:
                isUnique = False
                break
        
        # Caso a pergunta seja unica
        if isUnique == True and len(user_pergunta) > 3 and len(user_pergunta) <= 100:
            stdscr.clear()
            desistencia_da_resposta = 0

############################################################
            # Chama funcao que pergunta sobre as respostas
            desistencia_da_resposta = escreve_respostas(stdscr, question_id, mode)

            break
        
        # Caso de errado    
        else:
            stdscr.clear()

            tentar_novamente = "Deseja tentar novamente?"
            error_message = ["ERRO AO ADICIONAR PERGUNTA", tentar_novamente]

            current_row_idx = 0

            # Tela de erro
            while True:
                textPrint.print_title(stdscr)
                textPrint.print_multi_lines(stdscr, error_message, 2)
                menu.horizontal_menu(stdscr, current_row_idx, yes_no_menu)
            
                stdscr.refresh()

                key = stdscr.getch()

                if actions.keyboard(key) == 'left' and current_row_idx > 0:
                    current_row_idx -= 1

                elif actions.keyboard(key) == 'right' and current_row_idx < 1:
                    current_row_idx += 1

                elif actions.keyboard(key) == 'enter':
                    if current_row_idx == 0:
                        exitRegister = False
                        break
                    else:
                        exitRegister = True
                        break

        stdscr.clear()

        # Caso o user queira sair
        if exitRegister == True:
            break
    
    # Escreve os dados obtidos no banco de dados
    if exitRegister == False and desistencia_da_resposta != False:
        if mode == "Adicionar":
            new_pergunta_id = quantidade_perguntas + 1
        else:
            new_pergunta_id = question_id

        db_new_pergunta = firebase.database()
        new_pergunta = db_new_pergunta.child("Perguntas").child(new_pergunta_id)

        new_pergunta = {
            "Pergunta": user_pergunta
        }

        db_new_pergunta.update(new_pergunta)

        if mode == "Adicionar":
            db_qtd_pergunta = firebase.database()

            qtd_pergunta = {
                "Quantidade_Perguntas": new_pergunta_id
            }

            # Pega o valor de quantas perguntas o user ja enviou
            db_user_qtd_perguntas = firebase.database()
            user_qtd_perguntas = db_user_qtd_perguntas.child("Users").child(current_user_id).child("Questions").child("Quantidade_enviadas").get().val()

            # Cria o id pra pergunta que o user vai enviar
            new_user_pergunta_id = int(user_qtd_perguntas) + 1

            # Faz conexao com banco de dados
            db_write_user = firebase.database()
            new_user_pergunta = db_write_user.child("Users").child(current_user_id).child("Questions")

            new_user_pergunta = {
                new_user_pergunta_id:new_pergunta_id,
                "Quantidade_enviadas":new_user_pergunta_id
            }

            db_qtd_pergunta.update(qtd_pergunta)
            db_write_user.update(new_user_pergunta)

        stdscr.clear()
        stdscr.refresh()

################### ESCREVER RESPOSTAS #######################
def escreve_respostas(stdscr, question_id, mode):
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

    db_quantidade_resposta = firebase.database()

    quantidade_resposta = db_quantidade_resposta.child("Quantidade_Perguntas").get().val()
    
    exitRegister = False

    exitMessage = "Para sair, digite /exit em qualquer item"

    yes_no_menu = ('Sim', 'Nao')


    while True:
        textPrint.print_bottom(stdscr, exitMessage)
        textPrint.print_title(stdscr)

        curses.curs_set(True)

        resposta_labelA = "Informe a resposta item a): "
        resposta_labelB = "Informe a resposta item b): "
        resposta_labelC = "Informe a resposta item c): "
        resposta_labelD = "Informe a resposta item d): "
        
        trueFalseA_label = "Insira 1 caso seja verdadeiro e 0 caso seja falso: "
        trueFalseB_label = "Insira 1 caso seja verdadeiro e 0 caso seja falso: "
        trueFalseC_label = "Insira 1 caso seja verdadeiro e 0 caso seja falso: "
        trueFalseD_label = "Insira 1 caso seja verdadeiro e 0 caso seja falso: "
        

        x_respostaA = largura_tela//2 - 50
        y_respostaA = altura_tela//2

        x_respostaB = largura_tela//2 - 50
        y_respostaB = altura_tela//2 + 2

        x_respostaC = largura_tela//2 - 50
        y_respostaC = altura_tela//2 + 4

        x_respostaD = largura_tela//2 - 50
        y_respostaD = altura_tela//2 + 6

        x_trueFalseA = largura_tela//2 - 50
        y_trueFalseA = altura_tela//2 + 1

        x_trueFalseB = largura_tela//2 - 50
        y_trueFalseB = altura_tela//2 + 3

        x_trueFalseC = largura_tela//2 - 50
        y_trueFalseC = altura_tela//2 + 5

        x_trueFalseD = largura_tela//2 - 50
        y_trueFalseD = altura_tela//2 + 7

        stdscr.addstr(y_respostaA, x_respostaA, resposta_labelA)
        stdscr.addstr(y_trueFalseA, x_trueFalseA, trueFalseA_label)
        
        stdscr.addstr(y_respostaB, x_respostaB, resposta_labelB)
        stdscr.addstr(y_trueFalseB, x_trueFalseB, trueFalseB_label)
        
        stdscr.addstr(y_respostaC, x_respostaC, resposta_labelC)
        stdscr.addstr(y_trueFalseC, x_trueFalseC, trueFalseC_label)

        stdscr.addstr(y_respostaD, x_respostaD, resposta_labelD)
        stdscr.addstr(y_trueFalseD, x_trueFalseD, trueFalseD_label)

        curses.echo()

        user_respostaA = stdscr.getstr(y_respostaA, x_respostaA + len(resposta_labelA),50)
        user_respostaA = user_respostaA.decode("utf-8")

        if actions.verify_exit(user_respostaA) == True:
            exitRegister = True
            break

        #curses.echo(False)
    
        user_trueFalseA = stdscr.getstr(y_trueFalseA, x_trueFalseA + len(trueFalseA_label),50)
        user_trueFalseA = user_trueFalseA.decode("utf-8")
        
        if actions.verify_exit(user_trueFalseA) == True:
            exitRegister = True
            break

        user_trueFalseA = actions.verify_0_ou_1(user_trueFalseA)

        user_respostaB = stdscr.getstr(y_respostaB, x_respostaB + len(resposta_labelB),50)
        user_respostaB = user_respostaB.decode("utf-8")

        if actions.verify_exit(user_respostaB) == True:
            exitRegister = True
            break

        user_trueFalseB = stdscr.getstr(y_trueFalseB, x_trueFalseB + len(trueFalseB_label),50)
        user_trueFalseB = user_trueFalseB.decode("utf-8")
        
        if actions.verify_exit(user_trueFalseB) == True:
            exitRegister = True
            break

        user_trueFalseB = actions.verify_0_ou_1(user_trueFalseB)

        user_respostaC = stdscr.getstr(y_respostaC, x_respostaC + len(resposta_labelC),50)
        user_respostaC = user_respostaC.decode("utf-8")

        if actions.verify_exit(user_respostaC) == True:
            exitRegister = True
            break

        user_trueFalseC = stdscr.getstr(y_trueFalseC, x_trueFalseC + len(trueFalseC_label),50)
        user_trueFalseC = user_trueFalseC.decode("utf-8")

        if actions.verify_exit(user_trueFalseC) == True:
            exitRegister = True
            break

        user_trueFalseC = actions.verify_0_ou_1(user_trueFalseC)

        user_respostaD = stdscr.getstr(y_respostaD, x_respostaD + len(resposta_labelD),50)
        user_respostaD = user_respostaD.decode("utf-8")


        if actions.verify_exit(user_respostaD) == True:
            exitRegister = True
            break
        
        user_trueFalseD = stdscr.getstr(y_trueFalseD, x_trueFalseD + len(trueFalseD_label),50)
        user_trueFalseD = user_trueFalseD.decode("utf-8")

        if actions.verify_exit(user_trueFalseD) == True:
            exitRegister = True
            break
        user_trueFalseD = actions.verify_0_ou_1(user_trueFalseD)

        curses.echo(False)
        
        isUnique = True

        db_all_resposta = firebase.database()

        stdscr.clear()

        textPrint.print_title(stdscr)
        textPrint.print_center(stdscr, "Aguarde...")

        stdscr.refresh()
        if isUnique == True and (user_trueFalseA == True or user_trueFalseA == False) and (user_trueFalseB == True or user_trueFalseB == False) and (user_trueFalseC == True or user_trueFalseC == False) and (user_trueFalseD == True or user_trueFalseD == False) and ((user_trueFalseA == True and user_trueFalseB == False and user_trueFalseC == False and user_trueFalseD == False) or (user_trueFalseA == False and user_trueFalseB == True and user_trueFalseC == False and user_trueFalseD == False) or (user_trueFalseA == False and user_trueFalseB == False and user_trueFalseC == True and user_trueFalseD == False) or (user_trueFalseA == False and user_trueFalseB == False and user_trueFalseC == False and user_trueFalseD == True)): 

            stdscr.clear()

            textPrint.print_title(stdscr)
            sucess_message = ["Pergunta adicionada com sucesso", "Pressione qualquer tecla para continuar"]
            textPrint.print_multi_lines(stdscr,sucess_message, 2)
            
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()
            break

        else:
            stdscr.clear()

            tentar_novamente = "Deseja tentar novamente?"
            error_message = ["ERRO AO CADASTRAR RESPOSTA", tentar_novamente]

            current_row_idx = 0

            while True:
                textPrint.print_title(stdscr)
                textPrint.print_multi_lines(stdscr, error_message, 2)
                menu.horizontal_menu(stdscr, current_row_idx, yes_no_menu)
            
                stdscr.refresh()

                key = stdscr.getch()

                if actions.keyboard(key) == 'left' and current_row_idx > 0:
                    current_row_idx -= 1

                elif actions.keyboard(key) == 'right' and current_row_idx < 1:
                    current_row_idx += 1

                elif actions.keyboard(key) == 'enter':
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
        if mode == "Editar":
            new_resposta_id = question_id
            
        else:        
            new_resposta_id = quantidade_resposta + 1
            
        db_new_resposta = firebase.database()
        new_resposta = db_new_resposta.child("Respostas").child(new_resposta_id)

        new_resposta = {
        "a": {"isCorrect": user_trueFalseA, "valor": user_respostaA },
        "b": {"isCorrect": user_trueFalseB, "valor": user_respostaB },
        "c": {"isCorrect": user_trueFalseC, "valor": user_respostaC },
        "d": {"isCorrect": user_trueFalseD, "valor": user_respostaD }
        }

        db_new_resposta.update(new_resposta)

        if mode == "Adicionar":
            db_qtd_resposta = firebase.database()

            qtd_resposta = {
                "Quantidade_Perguntas": new_resposta_id 
            }

            db_qtd_resposta.update(qtd_resposta)
        
        stdscr.refresh()

    else:
        return False

########## ORDENA PERGUNTAS PARA SEREM MOSTRADAS DE 8 EM 8 ############
def get_questions_pages(questions):
    tamanho = len(questions)

    quantidade_paginas = math.ceil(tamanho/8)
    lista_perguntas = [0] * quantidade_paginas

    for pagina_atual in range(quantidade_paginas):
        this_page = []

        for in_page_question in range(8):
            this_question = pagina_atual*8 + in_page_question

            this_page.append(questions[this_question])

            if this_question == tamanho - 1:
                break

        lista_perguntas[pagina_atual] = this_page

    return lista_perguntas

########## RETORNA OS IDS DAS PERGUNTAS DOS USERS ###################
def get_questions_ids(questions):
    quantidade_perguntas = len(questions)

    questions_ids = []

    for pergunta_atual in range(1, quantidade_perguntas):
        id_atual = str(questions[str(pergunta_atual)])

        questions_ids.append(id_atual)

    return questions_ids

########### PEGA O TEXTO DAS PERGUNTAS ############################
def get_question_list(questions_ids):
    question_list = []

    quantidade = len(questions_ids)

    for pergunta_atual in range(quantidade):
        this_question = getData.get_one_question_data(questions_ids[pergunta_atual])

        question_list.append(this_question)

    return(question_list)

########## RETORNA OS IDS DAS PERGUNTAS RECEBIDAS ORDENADAS DE 1 A 8 #####
def add_question_number_on_page(current_page):
    tamanho = len(current_page)

    page_with_number = []

    for linha in range(tamanho):
        text = str(linha + 1) + " - " + current_page[linha]

        page_with_number.append(text)

    return page_with_number