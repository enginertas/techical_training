#ifndef _GAMEMAP_H_
#define _GAMEMAP_H_

#include <unordered_map>
#include <vector>
#include <random>
#include "city.h"

class GameMapTest;

class GameMap
{
private:
	std::random_device random_dev;
	unordered_map<string, City*> _city_graph;
	int _randomize(int, int);

public:
	GameMap();
	void addCity(City*);
	void destroyCity(City *);
	bool isEmpty();
	City* moveMonster(City*);
	City* placeMonsterRandomly();
	~GameMap();
	friend GameMapTest;
};

#endif

