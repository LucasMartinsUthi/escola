Ol�, instru��es para iniciar o jogo:

As configura��es atuais est�o para criar um servidor local e jogar o jogo em dois terminais diferentes no mesmo computador, caso queira testar o jogo entre dosi computadores entras no arquivo server.py e mudar a na linha 6 o 'localhost', para o ip do host, a mesa altera��o deve ser feita em classe/classJogador.py na linha 79.

Para iniciar ser� necess�rio o uso de 3 terminais, 1 servidor e 2 clientes. Primeiro iniciali�e o server.py, ap�s isso execute os main.py em ambos clientes, um sendo o jogador n�mero 1 e o outro o jogador n�mero 2. Feito isso s� jogar.

Regras:
No primeiro momento os jogadores recebem uma m�o inicial, o jogador n�mero 1 come�a com 4 cartas, e o jogador n�mero 2 com 3 cartas mais uma moeda(ganha 1 de mana nesse turno). Essa primeira m�o � poss�vel descartar quantas cartas desejadas, que elas ser�o substitu�das por outras no deck, as descartadas voltam para o deck.

Para colocar uma carta da  sua m�o � mesa, � necess�rio que o jogador tenha a quantidade certa de mana para jogar a carta, cada jogador come�a com 1 de mana m�xima, que vai aumentado por turno. Ao olhar a carta � poss�vel perceber 3 valores, que s�o attack, vida, custo de mana. Attack: indica a quantidade de dano que uma carta causa. Vida: indica quanto dano uma carta pode receber antes de ser eliminado do tabuleiro. Custo de Mana: quantidade de mana necess�rio para coloc�-la no tabuleiro.

Ao terminar o turno as cartas do tabuleiro atacam. Elas seguem as seguintes regras, cartas atacam inimigas opostas, ou seja, uma carta ataca a carta a sua frente, por�m � poss�vel que uma carta ataque duas cartas ao mesmo tempo. Caso n�o houver nenhuma carta inimiga para defender seu ataque, a carta ataca o advers�rio. Quando a vida de um jogador chega 0 ou menor o jogo acaba.

Av ida do jogador pode ser vista ao lado das cartas na m�o, onde informa a vida, mana atual, mana total, cartas no deck. Quando acaba as cartas do deck o jogador come�a a receber dano de fadiga, que aumenta 1 de dano a cada turno que passa.
