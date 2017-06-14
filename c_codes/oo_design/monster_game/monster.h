#ifndef _MONSTER_H_
#define _MONSTER_H_

#include <string>
#include "gamemap.h"

using namespace std;

class MonsterTest;

class Monster
{
private:
	int _id;
	bool _alive;
	bool _trapped;
	City* _city;
	GameMap * _game_map;

public:
	Monster();
	int getId();
	void setId(int);
	void setGameMap(GameMap *);
	City* getCity();
	bool isAlive();
	bool isTrapped();
	void kill();
	void placeRandomly();
	void move();
	friend MonsterTest;
};


#endif