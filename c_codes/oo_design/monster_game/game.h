#ifndef _GAME_H_
#define _GAME_H_

#include <string>
#include <vector>
#include "gamemap.h"
#include "monster.h"

class Game
{
protected:
	GameMap *_game_map;
	int _monster_count;
	int _killed_count;
	int _trapped_count;
	int _iteration_count;
	Monster *_monster_array;
	void _resolveConflicts();
	bool _placeMonsters();
	void _runGameLoop();
	void _killMonsters(string, vector<Monster *> &);

public:
	Game(GameMap *, int, int);
	void playGame();
	~Game();
};

#endif