#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <wait.h>

int valor = 5;

int main(){
	pid_t pid;

	pid = fork();

	if (pid == 0) {
		valor += 15;
        printf ("Processo filho: valor = %d\n",valor);
		return 0;
	}
	else if (pid > 0) {
		wait(NULL);
		printf ("Processo pai: valor = %d\n",valor); /* LINE A */
		return 0;
	}
}