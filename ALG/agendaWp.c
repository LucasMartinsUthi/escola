#include <stdio.h>
#include <string.h>
#define TAM 3

typedef struct _pessoa{
	char nome[20];
	int numero;
	char email[50];
} Pessoa;

typedef struct _grupo{
	char nome[20];
} Grupo;

typedef struct _pessoaGrupo{
	Pessoa pessoa;
	Grupo grupo;
	
} PessoaGrupo;

Pessoa addPessoa(char nome[20], char email[50], int numero){
	Pessoa P;
	strcpy(P.nome, nome);
	strcpy(P.email, email);
	P.numero  = numero;	
	return P;
}

Grupo addGrupo(char nome[20]){
	Grupo G;
	strcpy(G.nome, nome);
	return G;
}

PessoaGrupo addPessoaGrupo(Pessoa pessoa, Grupo grupo){
	PessoaGrupo PG;
	PG.pessoa = pessoa;
	PG.grupo = grupo;
	return PG;
}


int main(){
	PessoaGrupo a[TAM];
	Pessoa Lucas = addPessoa("Lucas", "l@gmail.com", 12334);
	Pessoa Pinha = addPessoa("Pinha", "p@gmail.com", 43221);
	
	Grupo snc = addGrupo("Soco na Cara");

	a[0] = addPessoaGrupo(Lucas, snc);
	a[1] = addPessoaGrupo(Pinha, snc);

	printf("%i", a[0].pessoa.numero);
}







