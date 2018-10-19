import math as mt
colunas = 4
#import numpy as np
linhas = eval(raw_input('informe o numero de linhas: '))
colunas = eval(raw_input('informe o numero de colunas: '))


matriz = []
cont_linhas = 1

while cont_linhas <= linhas:
	Linha = []
	cont_colunas = 1
	
	while cont_colunas <= colunas:
		elemento = float(raw_input('informe o elemento ('+str(cont_linhas)+','+str(cont_colunas)+'): '))
		Linha.append(elemento)
		cont_colunas += 1
	
	matriz.append(Linha)
	cont_colunas = 1
	cont_linhas += 1

#matriz = [[0.0,1.0,2.0,6.0],[0.0,7.0,0.0,5.0],[0.0,3.0,4.0,3.0],[0.0,3.0,7.0,9.0]]

def print_matriz(matriz):
	cont_print = 0
	while cont_print < linhas:
		print matriz[cont_print]
		cont_print += 1




print 'sua matriz'
print_matriz(matriz)

matriz2 = [] #linhas q comecam com 1
matriz3 = [] #linhas q comecam com 0
cont = 0
cont1 = 0
cont0 = 0

for linha in matriz:
	if linha[0] == 1:
		matriz2.append(linha)
		matriz.pop(cont)
		cont1 += 1
	elif linha[0] == 0:
		matriz3.append(linha)
		matriz.pop(cont)
		cont0 += 1

	cont += 1


matriz4 = matriz 
matriz = matriz2 + matriz4 + matriz3




coluna = 0
cont_linha = 0

def escal(matriz,cont1,cont0,coluna,cont_linha):
	cont = cont_linha
	while (cont > len(matriz)) or (cont < len(matriz))  : #transformo em 1 os elementos abaixo do pivo
	
		linha = matriz[cont]
		pivo = linha[coluna]
	
		cont_elem = 0
		if (linha[coluna] != 0):
			for elem in linha:
				linha[cont_elem] = elem/pivo #divide a linha pelo primeiro termo
				cont_elem += 1
		matriz[cont] = linha
		cont += 1


	cont = cont1 + 1
	prime = matriz[cont_linha]
	while (cont > len(matriz)) or (cont < len(matriz)): #zero os elementos abaixo do pivo
		linha = matriz[cont]
		cont_elem = coluna
		

		if (linha[coluna] != 0):
			while cont_elem < len(linha):
		
				linha[cont_elem] = linha[cont_elem] - prime[cont_elem]
				cont_elem += 1
		matriz[cont] = linha
		cont += 1
	cont1 += 1
	coluna += 1
	cont_linha += 1

	return matriz, cont1, coluna, cont_linha

	
	
while coluna < colunas and cont_linha < linhas:

	matriz, cont1, coluna, cont_linha = escal(matriz, cont1, cont0, coluna, cont_linha)


print 'sua matriz escalonada:'
print_matriz(matriz)



