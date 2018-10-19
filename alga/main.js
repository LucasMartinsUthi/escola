function ready(){
	let linhas, colunas

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
		let matriz = []
		let linha = []
		for(let i = 0; i < linhas; i++){
			linha = []
			for(let j = 0; j < colunas; j++){
				linha.push(parseInt($("input[name='i_"+(i+1)+":j_"+(j+1)+"']").val()))
			}
			matriz.push(linha)
		}
		console.log(matriz)


	});

};