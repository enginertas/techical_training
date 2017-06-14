#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>
#include <sys/resource.h>


void setProcessLimit(int resource, const char *str, rlim_t value)
{
	int ret;
	struct rlimit rl;

	printf("---------------------------------\n");

	ret = getrlimit(resource, &rl);
	if (ret < 0)
	{
		fprintf(stderr, "Error in reading process limits for %s: %s\n", str, strerror(errno));
		return;
	}
	else
	{
		printf("Previous soft limit for %s: %lld, hard limit: %lld\n", str, (long long int)rl.rlim_cur, (long long int)rl.rlim_max);
	}

	rl.rlim_cur = value;

	ret = setrlimit(resource, &rl);
	if (ret < 0)
	{
		fprintf(stderr, "Error in setting process soft limit for %s to %lld: %s\n", str, (long long int) value, strerror(errno));
	}
	else
	{
		printf("New soft limit for %s: %lld, hard limit: %lld\n", str, (long long int)rl.rlim_cur, (long long int)rl.rlim_max);
	}

}


int main()
{
	setProcessLimit(1231231, "DUMMY", (rlim_t) 3123123);
	setProcessLimit(RLIMIT_NOFILE, "MAX_FD", (rlim_t) 4097);
	setProcessLimit(RLIMIT_NOFILE, "MAX_FD", (rlim_t) 4096);

	return 0;
}