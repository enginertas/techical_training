#ifndef _UTILS_H_
#define _UTILS_H_

#include <iostream>
#include <sstream>
#include <fstream>
#include <iterator>
#include <string>
#include <vector>
#include <errno.h>
#include <cstring>
#include "gamemap.h"
#include "city.h"
#include "config.h"

using namespace	std;

class UtilsTest;

class Utils
{
private:
	static City* _parseMapLine(string);

public:
	static bool loadMapFromFile(GameMap &, const char*);
	friend UtilsTest;
};

#endif