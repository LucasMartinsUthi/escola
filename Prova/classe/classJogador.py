import pygame
from random import randint
import copy
import socket
import json
# from signal import signal, SIGPIPE, SIG_DFL

# signal(SIGPIPE, SIG_DFL)

class classJogador:

	def __init__(self):
		self.width = 1280
		self.height = 720
		self.canvas = pygame.display.set_mode([self.width, self.height])
		pygame.font.init()
		self.font = pygame.font.SysFont('Helvetica', 20)
		self.id = None
		self.deck = [{'name': "queen",  'mana': 7, 'atack': 4, 'life': 6, 'lifeTotal': 6, 'cor': [0, 0, 255]},
                    {'name': "knight", 'mana': 4, 'atack': 4, 'life': 3, 'lifeTotal': 3, 'cor': [0, 255, 0]},
                    {'name': "knight", 'mana': 4, 'atack': 4, 'life': 3, 'lifeTotal': 3, 'cor': [0, 255, 0]},
                    {'name': "bishop", 'mana': 3, 'atack': 0, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 0]},
                    {'name': "bishop", 'mana': 3, 'atack': 0, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 0]},
                    {'name': "rook", 'mana': 3, 'atack': 2, 'life': 6, 'lifeTotal': 6, 'cor': [255, 255, 0]},
                    {'name': "rook", 'mana': 3, 'atack': 2, 'life': 6, 'lifeTotal': 6, 'cor': [255, 255, 0]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 255]},
                    {'name': "pawn", 'mana': 1, 'atack': 1, 'life': 6, 'lifeTotal': 6, 'cor': [255, 0, 255]}]
		self.mesa = {-3: {'ocupado': False, 'pos': [70, self.height/2 + 30], 'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([70, self.height/2 + 30],[140,150]))},
                   -2: {'ocupado': False, 'pos': [210, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([210, self.height/2 + 30],[140,150]))},
                   -1: {'ocupado': False, 'pos': [350, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([350, self.height/2 + 30],[140,150]))},
                    0: {'ocupado': False, 'pos': [490, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([490, self.height/2 + 30],[140,150]))},
                    1: {'ocupado': False, 'pos': [630, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([630, self.height/2 + 30],[140,150]))},
                    2: {'ocupado': False, 'pos': [770, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([770, self.height/2 + 30],[140,150]))},
                    3: {'ocupado': False, 'pos': [910, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([910, self.height/2 + 30],[140,150]))}}
		self.vida = 1
		self.manaTotal = 0
		self.mana = 0
		self.fadiga = 1
		self.mao = []
		self.cartaSelecionada = None
		self.button = None
		self.bkpMesa  = copy.deepcopy(self.mesa)
		self.inimigo = None
		self.drag = False
		self.cheat = False
		self.escolha = []
		self.geraDeck()

	def initDraw(self, textButton):
		self.canvas.fill([0, 0, 0])

		mesa = pygame.draw.rect(self.canvas, [130, 89, 9], ([0,540], [1280, 180]))
		textsurface = self.font.render(str(self.vida) + " - " + str(self.mana) + "/" + str(self.manaTotal), False, (0, 0, 0))
		self.canvas.blit(textsurface, [1200, self.height-170])
		textsurface = self.font.render(str(len(self.deck)), False, (0, 0, 0))
		self.canvas.blit(textsurface, [1240, self.height-150])

		inimigo = pygame.draw.rect(self.canvas, [130, 89, 9], ([0,0], [1280, 180]))
		if self.inimigo != None and list(self.inimigo.keys()) != ['turno'] :
			textsurface = self.font.render(str(self.inimigo['vida']) + " - " + str(self.inimigo['mana']) + "/" + str(self.inimigo['manaTotal']), False, (0, 0, 0))
			self.canvas.blit(textsurface, [1200, 10])
			textsurface = self.font.render(str(self.inimigo['lenDeck']), False, (0, 0, 0))
			self.canvas.blit(textsurface, [1240, 30])
		else:
			textsurface = self.font.render("Procurando por Inimigos", False, (0, 0, 0))
			self.canvas.blit(textsurface, [self.width/2 - 120, 10])

		self.button = pygame.draw.rect(self.canvas, [130, 130, 10], ([self.width - 100, self.height/2 -25], [100, 50]))
		textsurface = self.font.render(textButton, False, (0, 0, 0))
		self.canvas.blit(textsurface, self.button)

	def socket(self, turno = False):
		con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		con.connect(('localhost', 4000))
		if turno:
			arr = json.dumps({'id': '3'}, ensure_ascii=False).encode('utf8')
			con.send(arr)
			return True

		mesa = {}
		chavesMesa = [key for key, val in self.mesa.items()]
		for chave in chavesMesa:
			mesa.update({chave : self.mesa[chave]['ocupado']})

		dragCarta = 0
		if self.cartaSelecionada != None:
			carta = self.mao[self.cartaSelecionada]['carta']
			dragCarta = {'cor': carta['cor'], 'atack': carta['atack'], 'life': carta['life'], 'mana': carta['mana']}

		arr = json.dumps({'id': self.id, 'lenMao' : len(self.mao), 'mesa' : mesa, 'lenDeck': len(self.deck), 'vida': self.vida, 'mana': self.mana, 'manaTotal': self.manaTotal, 'drag': self.drag, 'dragCarta': dragCarta, 'cartaSelecionada': self.cartaSelecionada}, ensure_ascii=False).encode('utf8')
		con.send(arr)
		resposta = con.recv(1024).decode()
		resposta = json.loads(resposta)
		self.inimigo = resposta
		self.con = True
		return True

	def geraDeck(self):
		for i in reversed(range(0, len(self.deck))):
			randI = randint(0,14)
			randItem = self.deck[randI]

			self.deck[randI] = self.deck[i]
			self.deck[i] = randItem
		
	def addMao(self):
		if len(self.mao) == 10:
			print('Mão Cheia')
		else:
			if len(self.deck) > 0:
				self.mao.append({'carta': self.deck[0]})
				self.deck.pop(0)
			else:
				self.vida = self.vida - self.fadiga
				self.fadiga += 1
				
		return self.mao

	def addCartaMesa(self, pos, cartaRearranjo = False):
		# Testa se existe uma carta selecionada
		if self.cartaSelecionada == None and not cartaRearranjo:
			return True
		print('Add carta mesa')
		print(cartaRearranjo)
		if not cartaRearranjo:
			# Verifica mana
			if 	self.mana - int(self.mao[self.cartaSelecionada]['carta']['mana']) < 0:
				print("Mana Insuficiente")
				return True
			else:
				 self.mana -= int(self.mao[self.cartaSelecionada]['carta']['mana'])

			# É uma moeda?
			if self.mao[self.cartaSelecionada]['carta']['name'] == 'coin':
				self.mana += 1
				self.mao.pop(self.cartaSelecionada)
				return True
			ocupado = copy.deepcopy(self.mao[self.cartaSelecionada]['carta'])

		else:
			ocupado = cartaRearranjo
			# print(ocupado)

		chaves = [key for key, val in self.mesa.items() if val['ocupado']]
		if not chaves:
			self.mesa[0]['ocupado'] = ocupado
			self.mesa[0]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[0]['pos'] ,[100,150]))
			if not cartaRearranjo:
				self.mao.pop(self.cartaSelecionada)
			return True

		menor = min(chaves)
		maior = max(chaves)

		if abs(menor) == 3:
			print('cheio')
			return False
		else:
			if abs(menor) == abs(maior):
				if pos <= menor:
					i = maior
					while i >= menor:
						self.mesa[i+1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i -= 1
					pos = menor
				elif menor < pos <= maior:
					i = maior
					while i >= pos:
						self.mesa[i+1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i -= 1
				elif pos > maior:
					pos = maior + 1
			else:
				# pos1 -
				if pos >= maior:
					i = menor
					while i <= maior:
						self.mesa[i-1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i-1]['pos'] ,[100,150]))
						i += 1
					pos = maior
				elif menor <= pos < maior:
					i = menor
					while i <= pos:
						self.mesa[i-1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i += 1
				elif pos < menor:
					pos = menor - 1

			self.mesa[pos]['ocupado'] = ocupado
			self.mesa[pos]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[pos]['pos'] ,[100,150]))

		if not cartaRearranjo:
			self.mao.pop(self.cartaSelecionada)
		return True

	def previewCartaMesa(self, pos):
		ocupado = True
		self.bkpMesa = copy.deepcopy(self.mesa)
		chaves = [key for key, val in self.mesa.items() if val['ocupado']]
		if not chaves:
			self.mesa[0]['ocupado'] = ocupado
			self.mesa[0]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[0]['pos'] ,[100,150]))
			self.drawMesa(True)
			return True

		menor = min(chaves)
		maior = max(chaves)

		if abs(menor) == 3:
			print('cheio')
			self.drawMesa(True)
			return False
		else:
			if abs(menor) == abs(maior):
				if pos <= menor:
					i = maior
					while i >= menor:
						self.mesa[i+1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i -= 1
					pos = menor
				elif menor < pos <= maior:
					i = maior
					while i >= pos:
						self.mesa[i+1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i+1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i -= 1
				elif pos > maior:
					pos = maior + 1
			else:
				# pos1 -
				if pos >= maior:
					i = menor
					while i <= maior:
						self.mesa[i-1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i-1]['pos'] ,[100,150]))
						i += 1
					pos = maior
				elif menor <= pos < maior:
					i = menor
					while i <= pos:
						self.mesa[i-1]['ocupado'] = self.mesa[i]['ocupado']
						self.mesa[i-1]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[i+1]['pos'] ,[100,150]))
						i += 1
				elif pos < menor:
					pos = menor - 1

			self.mesa[pos]['ocupado'] = ocupado
			self.mesa[pos]['rect'] = pygame.draw.rect(self.canvas, [0, 0, 0], (self.mesa[pos]['pos'] ,[100,150]))
		
		self.drawMesa(True)
		return True

	def drawMao(self):
		pos = [20, 564]
		i = 0
		for carta in self.mao:
			if i == self.cartaSelecionada:
				pos[0] += 104
				i += 1
				continue				
			self.mao[i].update({'rect': pygame.draw.rect(self.canvas, carta['carta']['cor'], (pos,[100,180]))})
			atackVida = self.font.render(str(self.mao[i]['carta']['atack']) + "/" + str(self.mao[i]['carta']['life']) + "  -- " + str(self.mao[i]['carta']['mana']), False, (0, 0, 0))
			self.canvas.blit(atackVida, self.mao[i]['rect'])
			pos[0] += 120
			i += 1

		return True

	def drawMesa(self, preview = False):
		lenChaves = len([key for key, val in self.mesa.items() if val['ocupado']])
		ajuste = 0
		if lenChaves % 2 == 0 and lenChaves != 0:
			ajuste  = -70
		chaves = list(self.mesa.keys())
		chaves.sort()

		for casa in chaves:
			pos = list(self.mesa[casa]['pos'])
			pos[0] += ajuste
			if self.mesa[casa]['ocupado'] != False and self.mesa[casa]['ocupado'] != True:
				atack = self.mesa[casa]['ocupado']['atack']
				atack = str(atack)
				vida = self.mesa[casa]['ocupado']['life']
				vida = str(vida)
				mana = self.mesa[casa]['ocupado']['mana']
				mana = str(mana)
				self.mesa[casa]['rect']	= pygame.draw.rect(self.canvas, self.mesa[casa]['ocupado']['cor'], (pos ,[100,100]))
				atackVida = self.font.render(atack + "/" + vida + " -- " + mana, False, (0, 0, 0))
				self.canvas.blit(atackVida, self.mesa[casa]['rect'])
			elif self.mesa[casa]['ocupado'] == True:
				self.mesa[casa]['rect']	= pygame.draw.rect(self.canvas, [155, 155, 155], (pos ,[100,100]), 1)
			else:
				self.mesa[casa]['rect']	= pygame.draw.rect(self.canvas, [0, 0, 0], (pos ,[100,150]), 1)
		if preview:
			self.mesa = copy.deepcopy(self.bkpMesa)
		return True

	def drawDrag(self):
		i = 0
		pos = [pygame.mouse.get_pos()[0]-50, pygame.mouse.get_pos()[1] - 90]
		for carta in self.mao:
			if i == self.cartaSelecionada:				
				self.mao[i].update({'rect': pygame.draw.rect(self.canvas, carta['carta']['cor'], (pos, [100,180]))})
				atackVida = self.font.render(str(carta['carta']['atack']) + "/" + str(carta['carta']['life']) + "  -- " + str(carta['carta']['mana']), False, (0, 0, 0))
				self.canvas.blit(atackVida, self.mao[i]['rect'])
			i += 1

		return True

	def drawInimigo(self):
		if self.con:
			self.con = False
			self.socket()

		if self.inimigo != None and list(self.inimigo.keys()) != ['turno']:
			mao = self.inimigo['lenMao']
			pos = [20, -24]
			for i in range(mao):
				if i != self.inimigo['cartaSelecionada']:
					cartaInimiga = pygame.draw.rect(self.canvas, (158, 100, 0), (pos,[100,180]))
				pos[0] += 120

			mesa = {}
			for carta in self.inimigo['mesa'].items():
				mesa.update({carta[0]: carta[1]})

			lenChaves = len([key for key, val in mesa.items() if val])
			ajuste = 0
			if lenChaves % 2 == 0 and lenChaves != 0:
				ajuste  = -70
			chaves = list(mesa.keys())
			chaves.sort()
			for casa in chaves:
				pos = (copy.deepcopy(self.mesa[int(casa)]['pos']))
				pos[0] += ajuste
				pos[1] -= 160
				if mesa[casa] != False:
					cartaInimigo = pygame.draw.rect(self.canvas, mesa[casa]['cor'], (pos ,[100,100]))
					atackVida = self.font.render(str(mesa[casa]['atack']) + "/" + str(mesa[casa]['life']) + "  -- " + str(mesa[casa]['mana']), False, (0, 0, 0))
					self.canvas.blit(atackVida, cartaInimigo)

				else:
					pygame.draw.rect(self.canvas, [0, 0, 0], (pos ,[100,150]), 1)
			if self.inimigo['drag'] != False:
				if self.cheat:
					cor = self.inimigo['dragCarta']['cor']
					atack = self.inimigo['dragCarta']['atack']
					vida = self.inimigo['dragCarta']['life']
					mana = self.inimigo['dragCarta']['mana']

					cartaInimiga = pygame.draw.rect(self.canvas, cor, (self.inimigo['drag'], [100,180]))
					atackVida = self.font.render(str(atack) + "/" + str(vida) + "  -- " + str(mana), False, (0, 0, 0))
					self.canvas.blit(atackVida, cartaInimiga)
				else:
					cartaInimiga = pygame.draw.rect(self.canvas, (158, 100, 0), (self.inimigo['drag'], [100,180]))
				

		else:
			print('Nenhum Inimigo Encontrado')

		return True

	def defesaInimigo(self):
		try:
			self.inimigo['mesa']
		except:
			return True

		inimigo = self.inimigo['mesa']
		mesa = self.mesa
		removeCartaMesa = False
		removidas = []
		listaInimigo = [key for key, val in inimigo.items() if val]
		lenInimigo = len(listaInimigo)
		lenMesa = len([key for key, val in mesa.items() if val['ocupado']])

		# print("Inimigo: len =", lenInimigo, "Lista:", listaInimigo)
		# print("Defendendo: len =", lenMesa)

		for i in range(-3, 4):
			if (lenInimigo - lenMesa) % 2 == 0:
				# print('Defesa em linha')
				if inimigo[str(i)] != False:
					# print('inimigo existe')
					if mesa[i]['ocupado'] != False:
						# print('Defesa existe')
						mesa[i]['ocupado']['life'] = mesa[i]['ocupado']['life'] - inimigo[str(i)]['atack']
						# print("Vida apos atak:", mesa[i]['ocupado']['life'])
						if mesa[i]['ocupado']['life'] <= 0:
							# print('Remove Carta', mesa[i]['ocupado'])
							removeCartaMesa = True
							removidas.append(i)
					else:
						# print('Não teve atack, atacar cara')
						self.vida -= inimigo[str(i)]['atack']
			else:
				atacou = False
				menor = 0
				maior = 0
				ajuste = 0

				# print('Atack crusado lenInimigo:', lenInimigo)
				if lenInimigo > 0:
					menor = int(min(listaInimigo))
					maior = int(max(listaInimigo))
					if abs(menor) == abs(maior): #menor == maior
						ajuste = +1
					else:
						ajuste = -1

				# print('Maior:', maior, 'Menor:', menor, 'Ajuste:', ajuste)

				if inimigo[str(i)] != False:
					if mesa[i]['ocupado'] != False:
						mesa[i]['ocupado']['life'] = mesa[i]['ocupado']['life'] - inimigo[str(i)]['atack']
						# print('inimigo:', inimigo[str(i)], 'atacou', mesa[i]['ocupado'])
						if mesa[i]['ocupado']['life'] <= 0:
							removeCartaMesa = True
							if i not in removidas:
								# print('Remover carta do index:', i+ajuste)
								removidas.append(i)
						atacou = True

					if -3 <= i+ajuste <= 3:
						if mesa[i+ajuste]['ocupado'] != False:
							mesa[i+ajuste]['ocupado']['life'] = mesa[i+ajuste]['ocupado']['life'] - inimigo[str(i)]['atack']
							# print('inimigo:', inimigo[str(i)], 'atacou', mesa[i+ajuste]['ocupado'])
							if mesa[i+ajuste]['ocupado']['life'] <= 0:
								removeCartaMesa = True
								if i+ajuste not in removidas:
									# print('Remover carta do index:', i+ajuste)
									removidas.append(i+ajuste)
							atacou = True

					if not atacou:
						# print('Cara')
						# print(i,"atacou cara dano:",inimigo[str(i)]['atack'])
						self.vida -= inimigo[str(i)]['atack']

		# print('Carta para remover:', removidas, 'rerranjo:', removeCartaMesa)
		for i in removidas:
			mesa[i]['ocupado'] = False
			mesa[i]['rect'] = None
		if removeCartaMesa:
			self.rearranjarMesa()
		return True

	def atackBispo(self):
		for i in range(-3, 3):
			try: 
				 self.mesa[i]['ocupado']['name']
			except:
				continue

			if self.mesa[i]['ocupado']['name'] == "bishop":
				if i+1 <= 3 and self.mesa[i+1]['ocupado'] != False:
					self.mesa[i+1]['ocupado']['life'] += 2
					if self.mesa[i+1]['ocupado']['life'] > self.mesa[i+1]['ocupado']['lifeTotal']:
						self.mesa[i+1]['ocupado']['life'] = self.mesa[i+1]['ocupado']['lifeTotal']
				if i-1 >= -3 and self.mesa[i-1]['ocupado'] != False:
					self.mesa[i-1]['ocupado']['life'] += 2
					if self.mesa[i-1]['ocupado']['life'] > self.mesa[i-1]['ocupado']['lifeTotal']:
						self.mesa[i-1]['ocupado']['life'] = self.mesa[i-1]['ocupado']['lifeTotal']
		return True

	def rearranjarMesa(self):
		bkpMesa = copy.deepcopy(self.mesa) #Rearranjar a mesa
		# reinicia Mesa
		self.mesa = {-3: {'ocupado': False, 'pos': [70, self.height/2 + 30], 'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([70, self.height/2 + 30],[140,150]))},
        			-2: {'ocupado': False, 'pos': [210, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([210, self.height/2 + 30],[140,150]))},
        			-1: {'ocupado': False, 'pos': [350, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([350, self.height/2 + 30],[140,150]))},
        			0: {'ocupado': False, 'pos': [490, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([490, self.height/2 + 30],[140,150]))},
        			1: {'ocupado': False, 'pos': [630, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([630, self.height/2 + 30],[140,150]))},
        			2: {'ocupado': False, 'pos': [770, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([770, self.height/2 + 30],[140,150]))},
        			3: {'ocupado': False, 'pos': [910, self.height/2 + 30],'rect': None, 'colide': pygame.draw.rect(self.canvas, [0, 0, 0], ([910, self.height/2 + 30],[140,150]))}}       
        # chaves das cartas nas mesa
		# print(bkpMesa, '#############', self.mesa)
		cartasMesa = [key for key, val in bkpMesa.items() if val['ocupado']]
		cartasMesa.sort()
		# Adiciona as carta em ordem da esquerda para direita
		# print(cartasMesa)
		for carta in cartasMesa:
			# print("Rearranjo: addCartaMesa(pos:", 3, "carta:",bkpMesa[carta]['ocupado'],")")
			self.addCartaMesa(3, bkpMesa[carta]['ocupado'])

		# self.debug()
		return True

	def addMana(self):
		self.manaTotal += 1
		self.mana = int(self.manaTotal)

	# Funçoes de Escolha de Carta
	def drawEscolha(self):
		pos = [self.width/2 - 170, self.height/2 - 90]
		if len(self.mao) == 4:
			pos = [self.width/2 - 230, self.height/2 - 90]

		i = 0
		for carta in self.mao:
			if i in self.escolha:				
				self.mao[i].update({'rect': pygame.draw.rect(self.canvas, carta['carta']['cor'], (pos,[100,180]))})
				pygame.draw.rect(self.canvas, [255, 0 ,0], ([pos[0] - 5, pos[1] - 5],[110,190]), 5)
				atackVida = self.font.render(str(self.mao[i]['carta']['atack']) + "/" + str(self.mao[i]['carta']['life']) + "  -- " + str(self.mao[i]['carta']['mana']), False, (0, 0, 0))
				self.canvas.blit(atackVida, self.mao[i]['rect'])
			else:
				self.mao[i].update({'rect': pygame.draw.rect(self.canvas, carta['carta']['cor'], (pos,[100,180]))})
				atackVida = self.font.render(str(self.mao[i]['carta']['atack']) + "/" + str(self.mao[i]['carta']['life']) + "  -- " + str(self.mao[i]['carta']['mana']), False, (0, 0, 0))
				self.canvas.blit(atackVida, self.mao[i]['rect'])
			pos[0] += 120
			i += 1

		return True

	def trocaEscolha(self):
		lenEscolha = len(self.escolha)
		self.escolha.sort(reverse=True)

		for i in range(0, lenEscolha):
			randIndex = randint(0, len(self.deck) - 1)
			self.deck.insert(randIndex, self.mao[self.escolha[i]]['carta'])
			self.mao.pop(self.escolha[i])
			self.addMao()

		self.escolha = []
		self.drawMao()
		return True

	def addMaoMana(self):
		self.mao.append({'carta': {'name': "coin",  'mana': 0, 'atack': 0, 'life': 0, 'cor': [66, 244, 244]}})
		return True

	def debug(self):
		print(self.mao)
		print("##################")
		print(self.mesa)
