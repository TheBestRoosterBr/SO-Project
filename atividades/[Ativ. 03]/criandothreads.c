#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h> //usar -lm na hora de compilação por causa da dependencia da math

int f; // Dado compartilhado entre as threads
bool k; //Nova variável da questão 3

void *funcaof(void *param); //Assinatura da função que será executada pela thread.
void *funcaok(void *param); //Assinatura da funçãop da quest]ao 3


int main(int argc, char *argv[]){
    if (argc != 2 && atoi(argv[1]) < 0) {
	    fprintf(stderr,"sintaxe: ./criandothreads <valor inteiro maior que 0>\n");
	    return -1;
    }

    pthread_t thread1; //cria variável do tipo thread
    pthread_attr_t attr; // cria variável do tipo atributo de thread
    pthread_attr_init(&attr); // inicializa attr com valores padroes

    pthread_create(&thread1,&attr,funcaof,argv[1]); // cria a thread

    pthread_t thread2;
    pthread_attr_init(&attr);
    pthread_create(&thread2, &attr, funcaok, argv[1]);

    pthread_join(thread1,NULL);
    pthread_join(thread2,NULL);

    printf("f = %d\n",f);
    printf("k = %s\n", k ? "True" : "False");
}

void *funcaof(void *param) {
    int i, ultimo = atoi(param);
    f = 0;

	if (ultimo > 0)
		for (i = 1; i <= ultimo; i++)
			f += i;
    
    pthread_exit(0);
}

//Questão 3
void *funcaok(void *param)
{
    int num = atoi(param);
    k = true;

    if(num <= 1){
        k = false;
    }
    else{
        int raiz = sqrt(num);
        for(int i = 2; i <= raiz; i++){
            if(num % 2 == 0){
                k = false;
                break;
            }
        }
    }

    pthread_exit(0);
}