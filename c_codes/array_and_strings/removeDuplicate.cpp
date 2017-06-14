#include <iostream>
#include <cstring>

using namespace std;

void removeDuplicate(char *str)
{
	int i;
	bool occurrence[256];
	char *place_p;

	for(i = 0; i < 256; i++)
	{
		occurrence[i] = false;
	}

	for(place_p = str;	*str; str++)
	{
		if(!occurrence[*str])
		{
			*place_p = *str;
			place_p++;
			occurrence[*str] = true;
		}
	}

	*place_p = 0;
}


int main()
{
	char str[100];

	strcpy(str, "");
	removeDuplicate(str);
	cout << str << endl;
	
	strcpy(str, "a");
	removeDuplicate(str);
	cout << str << endl;
	
	strcpy(str, "aa");
	removeDuplicate(str);
	cout << str << endl;
	
	strcpy(str, "ab");
	removeDuplicate(str);
	cout << str << endl;

	strcpy(str, "abababaababababababaababababagabcccafafdd");
	removeDuplicate(str);
	cout << str << endl;

	strcpy(str, "siz hala cekoslavakyalilastiramadiklarimizdan MISINIZ?");
	removeDuplicate(str);
	cout << str << endl;

	return 0;
}