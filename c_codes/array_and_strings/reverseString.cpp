#include <iostream>
#include <cstring>

using namespace std;

void reverseString(char *str)
{
	char tmp, *p, *last_str_p = NULL;

	if(str)
	{
		last_str_p = str;
		while(*last_str_p)
		{
			last_str_p++;
		}
		last_str_p--;

		for(;last_str_p > str; str++, last_str_p--)
		{
			tmp = *str;
			*str = *last_str_p;
			*last_str_p = tmp;
		}
	}
}


int main()
{
	char str[100];

	reverseString(NULL);
	cout << "null" << endl;

	strcpy(str, "");
	reverseString(str);
	cout << str << endl;
	
	strcpy(str, "a");
	reverseString(str);
	cout << str << endl;
	
	strcpy(str, "aa");
	reverseString(str);
	cout << str << endl;
	
	strcpy(str, "ab");
	reverseString(str);
	cout << str << endl;

	strcpy(str, "abc");
	reverseString(str);
	cout << str << endl;

	strcpy(str, "siz hala cekoslavakyalilastiramadiklarimizdan MISINIZ?");
	reverseString(str);
	cout << str << endl;

	return 0;
}