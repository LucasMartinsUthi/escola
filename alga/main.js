function ready(){
	let linhas, colunas
	let matriz = {}

	$('#linhaColuna').on('submit', function(e){
		e.preventDefault();
		let ij = $(this).serializeArray();
		// $(this).hide();
		linhas = ij[0].value;
		colunas = ij[1].value;
		montarMatriz()
	})

	function montarMatriz(){
		let html = ""
		for(let i=1; i <= linhas; i++){
			for(let j = 1; j <= colunas; j++){
				html += "<input style='width: 100px;' required type='number' name='i_"+i+":j_"+j+"' placeholder='i="+i+", j="+j+"'>"
			}
			html += "<br>"
		}
		html += "<button type='submit'>Escalonar</button>"
		$('#matriz').html(html)
	}

	$('#matriz').on('submit', function(e){
		e.preventDefault();
		let linha = []
		for(let i = 0; i < linhas; i++){
			linha = []
			for(let j = 0; j < colunas; j++){
				linha.push(parseInt($("input[name='i_"+(i+1)+":j_"+(j+1)+"']").val()))
			}
			matriz[i] = linha
		}

		tempMatriz = []
		count = 0
		i = 0
		j = 0

		for (linha in matriz){
			console.log(linha, count)
			if (matriz[linha][0] == 1){
				i++
			} else if(matriz[linha][0] == 0){
				j++
			}
			tempMatriz.push(matriz[linha])
			count++

		}
		console.log(tempMatriz)
		matrizEscalonamento = tempMatriz.slice()
		coluna = 0
		cont_linha = 0

		while (coluna < colunas && cont_linha < linhas)
			matrizEscalonamento, i, coluna, cont_linha = escalonamento(matrizEscalonamento, i, j, coluna, cont_linha)

		console.log(matrizEscalonamento)
	});

	function escalonamento(matriz,cont1,cont0,coluna,cont_linha){
		cont = cont_linha
		while ((cont > matriz.length) || (cont < matriz.length)){
		
			linha = matriz[cont]
			pivo = linha[coluna]
		
			cont_elem = 0
			if (linha[coluna] != 0){
				for (elem in linha){
					linha[cont_elem] = elem/pivo //divide a linha pelo primeiro termo
					cont_elem += 1
				}
			}
			matriz[cont] = linha
			cont += 1
		}

		// cont = cont1 + 1
		cont = cont1
		prime = matriz[cont_linha]
		while ((cont > matriz.length) || (cont < matriz.length)){//: #zero os elementos abaixo do pivo
			linha = matriz[cont]
			cont_elem = coluna
			

			if (linha[coluna] != 0){
				while (cont_elem < linha.length){
					linha[cont_elem] = linha[cont_elem] - prime[cont_elem]
					cont_elem += 1
				}
			}
			matriz[cont] = linha
			cont += 1
		}
		cont1 += 1
		coluna += 1
		cont_linha += 1

		return matriz, cont1, coluna, cont_linha
	}
};