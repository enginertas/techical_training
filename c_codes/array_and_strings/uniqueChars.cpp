#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

int compareChars(const void *elem1, const void *elem2)
{
	char fc, sc;

	fc = *((char *) elem1);
	sc = *((char *) elem2);
	
	if(fc < sc)	
		return -1;

	if(fc > sc)
		return 1;

	return 0;
}

bool areAllCharsUniqueWithoutDS(char *str)
{
	int i, len;

	len = strlen(str);
	qsort(str, len, sizeof(char), compareChars);

	for(i = 1; i < len; i++)
	{
		if (str[i] == str[i - 1])
		{
			return false;
		}
	}

	return true;
}

bool areAllCharsUnique(const char *str)
{
	int i;
	int occurrences[256];

	for(i = 0; i < 256; i++)
	{
		occurrences[i] = 0;
	}

	for(; *str; str++)
	{
		occurrences[*str]++;
		if(occurrences[*str] > 1)
		{
			return false;
		}
	}

	return true;
}



int main(int argc, char *argv[])
{
	int i;
	char buffer[9][100] = 
	{
		"",
		"<",
		"<<",
		"adrtr",
		"adrati",
		"mayakovski",
		"alicancaniminici",
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzA"
	};

	for(i = 0; i < 9; i++)
	{
		cout << i << ":" << buffer[i] << endl;
		cout << "DS \t" << areAllCharsUnique(buffer[i]) << endl;
		cout << "None \t" << areAllCharsUniqueWithoutDS(buffer[i]) << endl;
	} 	

	return 0;
}