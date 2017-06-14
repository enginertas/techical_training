#ifndef _CITY_H_
#define _CITY_H_

#include <string>
#include <iostream>
#include <unordered_map>
#include "config.h"

using namespace std;

class CityTest;

class City
{
private:
	string _city_name;
	string _city_roads[ROAD_COUNT];

public:
	City();
	City(string name, string roads[]);
	string getName();
	string getNeighbour(int);
	void removeNeighbour(int);
	friend CityTest;
};

#endif