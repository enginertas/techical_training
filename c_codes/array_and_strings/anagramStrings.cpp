#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

bool isStringPairAnagram(char* str1, char *str2)
{
	int i;
	char ref_count_first[256], ref_count_second[256];

	for(i = 0; i < 256; i++)
	{
		ref_count_first[i] = ref_count_second[i] = 0;
	}

	for(; *str1; str1++)
	{
		ref_count_first[*str1]++; 
	}
		
	for(; *str2; str2++)
	{
		ref_count_second[*str2]++;
	}

	for(i = 0; i < 256; i++)
	{
		if(ref_count_first[i] != ref_count_second[i])
		{
			return false;
		}
	}

	return true;
}


int main(int argc, char *argv[])
{
	int i;
	char buffer[16][100] = 
	{
		"",
		"",
		"<<a",
		"<<b",
		"<a<",
		"<b<",
		"axx",
		"xxa",
		"abbaza",
		"baaaaz",
		"abbaza",
		"baaazb",
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefhhijklmnopqrstuvwxyz",
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
		"ijklKLMNOPQRSTUVWXYZabcdefghmnopqrwxyzABCDEFHIJstuvG"
	};

	for(i = 0; i < 8; i++)
	{
		cout << i << ":" << buffer[2*i] << "\tAnagram?\t" << isStringPairAnagram(buffer[2*i], buffer[2*i + 1]) << endl;
	} 	

	return 0;
}