#include <stdio.h>
#include <unistd.h>

int main()
{
	off_t cur_offset;

	printf("Trying seek...\n");

	cur_offset = lseek(STDIN_FILENO, 0, SEEK_CUR);
	if(cur_offset < 0)
	{
		perror("Error in seeking on file from stdin");
	}
	else
	{
		printf("Current position on file from stdin: %lld\n", (long long) cur_offset);
	}

	return 0;
}