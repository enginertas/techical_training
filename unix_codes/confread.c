#include <stdio.h>
#include <unistd.h>

void pr_sysconf(int name)
{
	long r;

	r = sysconf(name);
	if(r < 0)
	{
		perror("Sysconf: Error in reading conf");
	}
	else
	{
		printf("Sysconf: Conf for name %d: %ld\n", name, r);
	}
}

void pr_pathconf(const char *path, int name)
{
	long r;

	r = pathconf(path, name);
	if(r < 0)
	{
		perror("Pathconf: Error in reading conf");
	}
	else
	{
		printf("Pathconf: Conf for name %d: %ld\n", name, r);
	}

}


int main(int argc, char *argv[])
{
	pr_sysconf(_SC_OPEN_MAX);
	pr_sysconf(1321231);

	pr_pathconf(".", _PC_NAME_MAX);
	pr_pathconf("/sali", _PC_NAME_MAX);
	pr_pathconf(".", 1321231);

	return 0;
}