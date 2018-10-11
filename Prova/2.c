#include <stdio.h>
#include <string.h>

int main(){
	int n;
	int i = 0;
	int k = 0;
	int countPar = 0;
	int countImpar = 0;
	int segmento = 0;

	printf("Tamanho da sequencia :");
	scanf("%i", &n);
	int sequencia[n];	

	for(i=0; i < n; i++){
		scanf("%i", &sequencia[i]);		
	}

	for(i=0; i < n; i){
		if (sequencia[i]%2 == 0){
			countPar = 0;
			countImpar = 0;
			while(sequencia[i]%2 == 0 && i < n){
				countPar++;
				if (i+1 > n) break;
				i++;
			}

			while(sequencia[i]%2 == 1 && i < n){
				countImpar++;
				if (i+1 > n) break;
				i++;
			}
		} else {
			countPar = 0;
			countImpar = 0;
			while(sequencia[i]%2 == 1 && i < n){
				countImpar++;
				if (i+1 > n) break;
				i++;
			}
			while(sequencia[i]%2 == 0 && i < n){
				countPar++;
				if (i+1 > n) break;
				i++;
			}
		}
		printf("%i,%i,%i\n", countPar, countImpar, k);
		if(countPar == countImpar || countPar == 0 && (countImpar == k || k == 0) || countImpar == 0 && (countPar == k || k == 0)) {
			if (countPar == 0)
				k = countImpar;
			else
				k = countPar;
			countPar = 0;
			countImpar = 0;
		} else {
			segmento = 1;
		}
	}
	if (segmento == 1){
		printf("​não é alternante");
	} else{
		printf("​%i-alternante", k);
	}
	return 0;
}