import pygame
import sys
from classe.classJogador import classJogador

pg = pygame
pg.init()

draw = pg.draw
image = pg.image
transform = pg.transform

jogador = classJogador()
jogador.id = input("Qual Jogador vc é: ")

click = False
dragDrop = True
addCartaMesa = False
preview = False
inicioTurno = True
primeiroTurno = True
fim = False
button2 = False
button3 = False

jogador.socket()
jogador.addMao()
jogador.addMao()
jogador.addMao()

if int(jogador.inimigo['turno']) == int(jogador.id):
	jogador.addMao()

jogador.drawMao()

#Tela de Escolha de carta
escolhendoCarta = True
escolha = True
while escolhendoCarta:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	i = 0
	for carta in jogador.mao:
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and escolha == True and carta['rect'].collidepoint(pg.mouse.get_pos()):
			if i in jogador.escolha:
				jogador.escolha.remove(i)
			else:
				jogador.escolha.append(i)
			escolha = False
		i += 1

	if (event.type != pygame.MOUSEBUTTONDOWN or event.button != 1) and event.type != pygame.MOUSEMOTION:
		escolha = True

	jogador.initDraw("Trocar")
	jogador.drawEscolha()
	pg.display.update()
	pg.time.Clock().tick(60)

	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and jogador.button.collidepoint(pg.mouse.get_pos()):
		jogador.trocaEscolha()
		escolhendoCarta = False

# Add Carta de Mana para jogador número 2
if int(jogador.inimigo['turno']) != int(jogador.id):
	jogador.addMaoMana()
	jogador.drawMao()
	primeiroTurno = False

# Tela jogo
while not fim:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	if int(jogador.inimigo['turno']) != int(jogador.id):
		jogador.initDraw("T Inimigo")
	elif jogador.inimigo == None:
		jogador.initDraw("...")
	else:
		jogador.initDraw("Turno")

		# Click Button
		if inicioTurno:
			if not primeiroTurno:
				jogador.addMao()
				jogador.defesaInimigo()
			jogador.addMana()
			primeiroTurno = False
			inicioTurno = False

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and click and escolhendoCarta != False and jogador.button.collidepoint(pg.mouse.get_pos()):
			print('passou Turno')
			click = False
			jogador.atackBispo()
			jogador.socket(True)
			inicioTurno = True

		elif event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or click != False:
			click = True
			escolhendoCarta = True

		# Drag Drop carta
		i = 0
		for carta in jogador.mao:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and dragDrop and carta['rect'].collidepoint(pg.mouse.get_pos()):
				dragDrop = False
				jogador.cartaSelecionada = i
				jogador.drag = [pygame.mouse.get_pos()[0] - 50, 720 - pygame.mouse.get_pos()[1] - 90]
				addCartaMesa = True
			i += 1

		#Preview
		h = -3
		chavesMesa = list(jogador.mesa.keys())
		chavesMesa.sort()
		for cartaMesa in chavesMesa:
			if dragDrop == False and addCartaMesa == True and jogador.mesa[cartaMesa]['colide'].collidepoint(pg.mouse.get_pos()):
				jogador.previewCartaMesa(h)
				preview = True	
			h += 1

		#Parado
		if (event.type != pygame.MOUSEBUTTONDOWN or event.button != 1 or dragDrop != False) and event.type != pygame.MOUSEMOTION:
			chaves = list(jogador.mesa.keys())
			chaves.sort()	
			for casa in chaves:
				if jogador.mesa[casa]['colide'].collidepoint(pg.mouse.get_pos()):
					if addCartaMesa:
						jogador.addCartaMesa(casa)	
						addCartaMesa = False

			jogador.cartaSelecionada = None
			jogador.drag = False
			dragDrop = True

		chaves = list(jogador.mesa.keys())
		for casa in chaves:
			if jogador.mesa[casa]['colide'].collidepoint(pg.mouse.get_pos()):
				colide = True
		if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 and preview == True) or (dragDrop == False and not colide):
			preview = False
		colide = False

		if jogador.drag != False:
			jogador.drag = [pygame.mouse.get_pos()[0] - 50, 720 - pygame.mouse.get_pos()[1] - 90]

	if jogador.vida <= 0 or jogador.inimigo['vida'] <= 0:
		fim = True

	# CHEAT
	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
		button3 = True

	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:		
		button2 = True

	if (event.type == pygame.MOUSEBUTTONUP and event.button == 3 or event.type == pygame.MOUSEBUTTONUP and event.button == 2):
		button2 = False
		button3 = False
		jogador.cheat = False
	
	if button2 and button3:
		jogador.cheat = True
	#Draws 
	jogador.drawMao()
	if not preview:
		jogador.drawMesa()
	jogador.drawInimigo()
	jogador.drawDrag()
	pg.display.update()
	pg.time.Clock().tick(30)


# Tela Final
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	if jogador.vida <= 0:
		textsurface = jogador.font.render("Derrota", False, (255, 255, 255))
		jogador.canvas.blit(textsurface, [jogador.width/2 - 120, jogador.height/2])
	else:
		textsurface = jogador.font.render("Vitoria", False, (255, 255, 255))
		jogador.canvas.blit(textsurface, [jogador.width/2 - 120, jogador.height/2])

	pg.display.update()
	pg.time.Clock().tick(30)	