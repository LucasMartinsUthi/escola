#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define LEN_AMIGOS 100

typedef struct Pessoa{
	int id;
	char nome[50];
	char email[50];
	char telefone[13];
	int amigos[LEN_AMIGOS];
}Pessoa;

Pessoa redeSocial[100];

void viewAmigo(Pessoa p){
	printf("    Nome:%s\n", p.nome);
	printf("    Email:%s\n", p.email);
	printf("    Telefone:%s\n", p.telefone);
	printf("-----------------------------\n");	
}

void viewPessoa(Pessoa p){
	printf("Seu Perfil!\n");
	printf("Nome:%s\n", p.nome);
	printf("Email:%s\n", p.email);
	printf("Telefone:%s\n", p.telefone);

	printf("Amigos:\n");
	for(int i = 0; i < LEN_AMIGOS; i++){
		if(p.amigos[i] != 0){
			viewAmigo(redeSocial[p.amigos[i]]);
		}
	}
}

void viewAmigosComum(Pessoa p){
	Pessoa a;
	for(int i = 0; i < LEN_AMIGOS; i++){
		if(p.amigos[i] != 0){
			a = redeSocial[p.amigos[i]];
			//a é meu amigo
			printf("Amigos em comum com %s:\n",a.nome);
			for(int j = 0; j < LEN_AMIGOS; j++){
				// para todo amigo de a diferente de 0
				if(a.amigos[j] != 0){
					//Circular pelos meus amigos
					for(int m = 0; m < LEN_AMIGOS; m++){
						if(p.amigos[m] == a.amigos[j]){
							viewAmigo(redeSocial[a.amigos[j]]);
						}
					}
				}
			}
		}
		
	}
}


void main(){
	Pessoa a,b,c;
	
	a.id = 1;
	strcat(a.nome,"Lucas");
	strcat(a.email,"lucas@email.com");
	strcat(a.telefone,"(54)996870594");
	for(int i = 0; i < 100; i++){
		a.amigos[i] = 0;
	}
	a.amigos[0] = 2;
	a.amigos[1] = 3;

	b.id = 2;
	strcat(b.nome,"Pedro");
	strcat(b.email,"pedro@email.com");
	strcat(b.telefone,"(53)12345678");
	for(int i = 0; i < 100; i++){
		b.amigos[i] = 0;
	}
	b.amigos[0] = 3;

	c.id = 3;
	strcat(c.nome,"Bianca");
	strcat(c.email,"bianca@email.com");
	strcat(c.telefone,"(54)87654321");
	for(int i = 0; i < 100; i++){
		c.amigos[i] = 0;
	}
	c.amigos[0] = 1;

	redeSocial[a.id] = a;
	redeSocial[b.id] = b;
	redeSocial[c.id] = c;

	viewPessoa(redeSocial[1]);
	printf("\n\n");
	viewAmigosComum(redeSocial[1]);
}
