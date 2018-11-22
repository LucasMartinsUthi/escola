#include<stdio.h>
#include<stdlib.h>
typedef struct vetor{
	int *v;
	int size;
} vetor;


typedef struct matriz{
	int **m;
	int size;
} matriz;

matriz initVetor(int size){
	vetor v;

	v.size = size;
	v.v = (int *)malloc(size*sizeof(int));

	return v;
}

matriz initMatriz(int size){
	matriz m;

	m.size = size;
	m.m = (int **)malloc(size*sizeof(vetor));

	vetor m.m[0] = initVetor(3);
	return m;
}                                                                                                                               

void printMatriz(matriz m){
	for(int i = 0; i < m.size; i++){
		if (m.m[i] == NULL){
			printf("Linha Vazia");	
		}else{
			for(int j = 0; i < m.m[i].size; j++){
				printf("%i", m.m[i][j]);
			}
			printf("\n");	
		}
	}
}

void teste(matriz m){
	for(int i = 0; i < m.size; i++){
		printf("%p", m.m[i]);
				printf("\n");
	}
}


/*
init
addVetor
RemoveVetor

List
Remove

AddSize

*/



int main(){
	int a;
	printf("Tamanho da Matriz: ");
	scanf("%i", &a);

	matriz m = initMatriz(a);
	printMatriz(m);
}


