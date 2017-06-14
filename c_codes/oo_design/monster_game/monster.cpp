#include "monster.h"


Monster::Monster()
{
	_city = NULL;
	_game_map = NULL;
	_id = -1;
	_alive = true;
	_trapped = false;
}


void Monster::setId(int monster_id)
{
	_id = monster_id;
}


void Monster::setGameMap(GameMap * map)
{	
	_game_map = map;
}


int Monster::getId()
{
	return _id;
}


City* Monster::getCity()
{
	return _city;
}


bool Monster::isAlive()
{
	return _alive;
}


void Monster::kill()
{
	_alive = false;
}


bool Monster::isTrapped()
{
	return _trapped;
}


void Monster::placeRandomly()
{
	// If the initial placement is not successful, set the state as "trapped"
	_city = _game_map->placeMonsterRandomly();
	if(! _city)
	{
		_trapped = true;
	}
}


void Monster::move()
{
	City *next_city;

	// If no next city is available, set monster as "trapped"
	next_city = _game_map->moveMonster(_city);
	if(next_city)
	{
		_city = next_city;
	}
	else
	{
		_trapped = true;
	}
}