#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>


void createHoleFile()
{
	int fd;
	long long retval;
	char buf1[] = "abcdefghij";
	char buf2[] = "ABCDEFGHIJ";
	mode_t mode;

	printf("Creating hole file...\n");

	mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;
	fd = open("hole.txt", O_WRONLY | O_CREAT | O_TRUNC, mode);
	if(fd < 0)
	{
		perror("Error creating the file");
		return;
	}

	retval = (long long) write(fd, buf1, 10);
	if (retval != 10)
	{
		perror("1st Write error");
		return;
	}
	/* offset 10 */

	retval = (long long) lseek(fd, 16384, SEEK_SET);
	if(retval < 0)
	{
		perror("lseek error");
		return;
	}
	/* offset 16384 */

	retval = (long long) write(fd, buf2, 10);
	if (retval != 10)
	{
		perror("2nd Write error");
	}
	/* offset 16394 */
}


void createNonholeFile()
{
	int i;
	int fd;
	long long retval;
	char buf1[16384];
	char buf2[] = "ABCDEFGHIJ";
	mode_t mode;

	printf("Creating nonhole file...\n");

	for(i = 0; i < 16384; i++)
	{
		buf1[i] = 'a';
	}
	
	mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;
	fd = open("nonhole.txt", O_WRONLY | O_CREAT | O_TRUNC, mode);
	if(fd < 0)
	{
		perror("Error creating the file");
		return;
	}

	retval = (long long) write(fd, buf1, 16384);
	if (retval != 16384)
	{
		perror("1st Write error");
		return;
	}

	retval = (long long) write(fd, buf2, 10);
	if (retval != 10)
	{
		perror("2nd Write error");
	}
}


int main()
{
	createHoleFile();
	createNonholeFile();

	return 0;
}