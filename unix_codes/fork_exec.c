#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main(int argc, char *argv[])
{
	int pid;

	if((pid = fork()) > 0)
	{
		printf("Parent: %d\n", pid);
		waitpid(pid);
		exit(0);
	}
	else if(!pid)
	{
		printf("Child \n");
		execlp("/bin/ls", "-al",(char *)NULL);
		perror("exec error");
		exit(-1);
	}
	else
	{
		perror("fork error");
		exit(-1);
	}

	return 0;
}