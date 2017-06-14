#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>

int main(int argc, char *argv[])
{
	int fd;
	int file_status;

	if(argc != 2)
	{
		printf("Usage: ./test <descriptor#>\n");
		return -1;
	}

	fd = atoi(argv[1]);
	file_status = fcntl(fd, F_GETFL, 0);
	if(file_status < 0)
	{
		fprintf(stderr, "fcntl - error in getting status of fd %d: %s\n", fd, strerror(errno));
		return -2;
	}

	switch(file_status & O_ACCMODE)
	{
		case O_RDONLY:
			printf("read only");
			break;

		case O_WRONLY:
			printf("write only");
			break;

		case O_RDWR:
			printf("read write");
			break;

		default:
			printf("Unknown access mode! \n");
			return -3;
	}

	if(file_status & O_APPEND)
	{
		printf(", append");
	}
	if(file_status & O_NONBLOCK)
	{
		printf(", nonblocking");
	}
#if defined(O_SYNC)
	if(file_status & O_SYNC)
	{
		printf(", sync writes");
	}
#endif
	printf("\n");

	return 0;
}