<H1> Infinity Questions </H1>
<H4> Trabalho de Computação 1 - UFRJ </H4>
<H4> Grupo: Amanda Pereira da Silva, Luiz Carlos Aguiar Carrion, Maria Eduarda de Souza Mafra, Yuri Pereira Dantas </H4>

<H2> OBJETIVO DO TRABALHO </H2>
<p>O objetivo do trabalho é criar um jogo de perguntas e respostas. Para isso, iremos utilizar o banco de dados do Google (Firebase) em conjunto com o nosso conhecimento de python.</p>

<H2> REQUISITOS </H2>
<p> Para poder testar o nosso programa, você deve ter instalado as seguintes
	bibliotecas em seu computador:

<b>Curses:</b> Essa biblioteca permite criarmos os menus. Para mais informações sobre ela, clique <a href = "https://github.com/zephyrproject-rtos/windows-curses">aqui</a>. Caso você esteja utilizando um sistema Linux, provavelmente você já
 possui essa biblioteca instalada. Caso esteja usando o windows utilize o seguinte comando:</p>

<blockquote> $ pip install windows-curses </blockquote>
<br>

<p><b> Pyrebase: </b>Essa biblioteca é responsável pelo banco de dados Firebase. Com ela poderemos utilizar funcionalidades de login, senha, poderemos salvar as pontuações no Scoreboard e conseguiremos implementar um sistema de sugestões de perguntas. Caso deseja saber mais sobre a biblioteca, clique <a href="https://github.com/thisbejim/Pyrebase">aqui</a> Para instalar-la em seu computador (Linux ou Windows), utilize o seguinte comando:</p>

<blockquote> $ pip3 install pyrebase4 </blockquote>
<br>

<p> Todas as outras bibliotecas utilizadas já são instaladas junto com o Python. É necessário uma conexão com a internet para poder jogar.</p>

<H2> REGRAS </H2>
<p> Ao começar o jogo, teremos todas as perguntas do banco de dados sendo postas de forma aleatória. Um fator de dificuldade é o tempo. O usuário terá 20 segundos para responder cada pergunta. Caso ele acerte, ele avançará para a próxima. O objetivo é responder o máximo que ele conseguir. As perguntas são todas objetivas, restritas a 4 opções, sendo uma, e somente uma delas, correta. Caso ele erre, o jogo acaba.</p>

<H2> FUNCIONALIDADES EXTRAS </H2>
<p> Para deixar o jogo mais divertido, decidmos adicionar algumas funcionalidades. Após discutirmos sobre várias ideias, essas serão as que usaremos no jogo:<br>

<b> Enviar perguntas: </b> Para que o jogo fique mais divertido ainda, decidimos utilizar um sistema no qual o jogador pode sugerir novas perguntas, fazendo com que ele fique cada vez mais desafiador!

<b> Sistema de Login e Scoreboard: </b> Pensando num fator mais competitivo, chegamos a conclusão de que uma funcionalidade que salve o progresso do jogador é essencial. Aproveitando essa ideia, decidimos que iremos criar um Scoreboard com as 5 melhores pontuações e seus respectivos usuários.</p>

<H2> MATERIAIS ADICIONAIS </H2>
<p><b> Wireframe: </b>http://bit.ly/wireframe_show_do_milhao</p>
