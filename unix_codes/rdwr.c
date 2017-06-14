#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main()
{
	char ch;
	int fd, flags;
	char buf[11] = "0123456789";

	scanf("%c", &ch);
	if(ch == 't')
	{
		flags = O_WRONLY | O_TRUNC;	
	}
	else
	{
		flags = O_WRONLY;
	}

	fd = open("./faruk", flags);
	if (fd < 0)
	{
		perror("Error in opening file");
		return -1;
	}
	
	write(fd, buf, 10);
	close(fd);

	return 0;
}