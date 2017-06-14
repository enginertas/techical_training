#include <stdio.h>
#include <dirent.h>

int main(int argc, char *argv[])
{
	char * dir_path;
	DIR * dirp;
	struct dirent * dir_entry;

	if (argc < 2)
	{
		dir_path = ".";
	}
	else
	{
		dir_path = argv[1];
	}

	dirp = opendir(dir_path);
	if(! dirp)
	{
		perror(dir_path);
		return -1;
	}

	while((dir_entry = readdir(dirp)))
	{
		printf("%s\n", dir_entry->d_name);
	}

	closedir(dirp);

	return 0;
}