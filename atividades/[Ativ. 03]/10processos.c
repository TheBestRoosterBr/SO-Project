#include <stdio.h>
#include <unistd.h>

int main()
{
	printf("%d\n",getpid());
	fork();
	printf("%d\n",getpid());


	fork();
	printf("%d\n",getpid());

	fork();
	printf("%d\n",getpid());

    //Apenas adicionar mais 1 fork seguindo a fórmula apresentada anteriormente
    fork();
	printf("%d\n",getpid());

	return 0;
}