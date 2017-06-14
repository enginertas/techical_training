#include <iostream>
#include <cstring>

using namespace std;

bool isSubstring(const char *str1, const char *str2)
{
	return strstr(str1, str2) ? true : false;
}

bool isStringRotated(const char *str1, const char *str2)
{
	int len1, len2;
	char *dup_str;
	bool result;

	len1 = strlen(str1);
	len2 = strlen(str2);

	if(len1 != len2)
	{
		return false; 
	}
	
	dup_str = new char[2 * len1 + 1];
	strcpy(dup_str, str1);
	strcat(dup_str, str1);
	result = isSubstring(dup_str, str2);
	delete [] dup_str;

	return result;
}

int main(int argc, char *argv[])
{
	cout << "1\t" << isStringRotated("", "") << endl;
	cout << "0\t" << isStringRotated("a", "") << endl;
	cout << "0\t" << isStringRotated("", "a") << endl;
	cout << "1\t" << isStringRotated("aa", "aa") << endl;
	cout << "1\t" << isStringRotated("ali", "ali") << endl;
	cout << "1\t" << isStringRotated("ali", "lia") << endl;
	cout << "1\t" << isStringRotated("ababaca", "acaabab") << endl;
	cout << "1\t" << isStringRotated("acaabab", "ababaca") << endl;
	cout << "1\t" << isStringRotated("alicim", "imalic") << endl;
	cout << "0\t" << isStringRotated("alicim", "mialic") << endl;
	cout << "1\t" << isStringRotated("fecrxt", "rxtfec") << endl;
	cout << "0\t" << isStringRotated("fecrxt", "rxtfce") << endl;
	cout << "1\t" << isStringRotated("delilerden sen anlarsin konus onlarla", "onlarladelilerden sen anlarsin konus ") << endl;
	cout << "1\t" << isStringRotated("delilerden sen anlarsin konus onlarla", " onlarladelilerden sen anlarsin konus") << endl;
	cout << "0\t" << isStringRotated("delilerden sen anlarsin konus onlarla", "onlarla delilerden sen anlarsin konus") << endl;
	return 0;
}