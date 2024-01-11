#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

const int STACK_SIZE=65536; // Tamanho da Stack (65536 bytes ou 64 KiB).


// Codigo da Thread
int thread_code(void *arg){
   int i = 0;
   int n = atoi(arg);
   printf("Executando na tarefa filha %d \n", n);
   for ( i = 1 ; i <= 10 ; i++ )
      printf("\t thread(%d) = %d * %d = %d\n", n, n, i, (n*i));
   printf("\n");
   return 0;
}

void main(int argc, char *argv[]){
  // Ponteiro para a base e topo da Stack
   void* stack_base[argc-1];
   void* stack_top[argc-1];

   // ID de cada thread
   int  pid[argc-1];

   for (int j = 1; j < argc; j++){
     // Alocacao das Stacks de cada thread
   	 stack_base[j-1] = malloc(STACK_SIZE);
     if(stack_base[j-1]==NULL) {
        perror("malloc");
        exit(1);
     }
         // Topo da stack = base + tamanho da stack
     stack_top[j-1] = stack_base[j-1] + STACK_SIZE;
   }

   printf ("Foi alocado espaco para (%d) threads\n", argc-1);
   for (int j = 1; j < argc; j++){
        // Criando Threads
        pid[j-1] = clone(thread_code, stack_top[j-1], CLONE_VM | CLONE_FS | CLONE_FILES | CLONE_SIGHAND, argv[j]);
        if (pid[j-1] < 0) {
            printf("Erro: Nao foi possivel criar a thread.\n");
            exit(EXIT_FAILURE);
        }
   }

   // Aguarda término das threads
   for (int j = 1; j < argc; j ++)
      wait(&pid[j-1]);

   // Libera stack de cada thread
   for (int j = 1; j < argc; j++){
     free(stack_base[j-1]);
   }
   printf("Threads filhas finalizadas.\n");
}
