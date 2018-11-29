#include<stdio.h>
#include<stdlib.h>


void main(){
	int *v;
	int n, temp;
	

	printf("Tamanho do vetor:\n");
	scanf("%i", &n);
	
	v = (int *)malloc(n*sizeof(int));

	printf("Valores do vetor:\n");
	for (int i = 0; i < n; i++){
		scanf("%i", &v[i]);
	}

	printf("Vetor Normal:");
	for (int i = 0; i < n; i++){
		printf("%i", v[i]);
	}
	printf("\n");

	printf("Vetor Descompactado:");
	for (int i = 0; i < n; i++){
		if(i%2 == 0){
			temp = v[i];
		}else{
			for(int j = 0; j < v[i]; j++){
				printf("%i", temp)	;		
			}
		}
	}
	printf("\n");

	
}
