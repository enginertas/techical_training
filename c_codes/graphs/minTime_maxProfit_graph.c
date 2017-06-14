#include <stdio.h>

int findMax(int input1, char* input2)
{
	int i, j;
	char **citymap;
	int **maxarray;

	citymap = (char **) malloc(sizeof(char *) * input1);
	maxarray = (int **) malloc(sizeof(int *) * input1);

	for(i = 0; i < input1; i++)
	{
		citymap[i] = (char *) malloc(sizeof(char) * input1);
		maxarray[i] = (int *) malloc(sizeof(int) * input1);
		for(j = 0; j < input1; j++)
		{
			maxarray[i][j] = 0;
			citymap[i][j] = *input2;
			input2++;
		}
	}

	for(i = 0; i < input1; i++)
	{
		for(j = 0; j < input1; j++)
		{
			if(!i && !j)
			{
				maxarray[i][j] = citymap[i][j];
			}
			else if(!i)
			{
				maxarray[i][j] = maxarray[i][j-1] + citymap[i][j];
			}
			else if(!j)
			{
				maxarray[i][j] = maxarray[i-1][j] + citymap[i][j];
			}
			else
			{
				maxarray[i][j] = maxarray[i][j-1];
				if(maxarray[i][j] < maxarray[i-1][j])
				{
					maxarray[i][j] = maxarray[i-1][j];
				}
				maxarray[i][j] += citymap[i][j];
			}
		}
	}

	return maxarray[i -1][j-1];

}
int main()
{
	int retval;
	char arr[16] = {1, 5, 6, 9, 7, 12, 14, 25, 13, 100, 24, 44, 8, 9, 57, 12};
	retval = findMax(4, arr);
	printf("%d\n", retval);
	return 0;
}