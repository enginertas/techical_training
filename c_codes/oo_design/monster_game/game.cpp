#include "game.h"


Game::Game(GameMap * map, int m_count, int i_count)
{
	_game_map = map;
	_monster_count = m_count;
	_killed_count = 0;
	_trapped_count = 0;
	_iteration_count = i_count;
	_monster_array = new Monster[m_count];
}


Game::~Game()
{
	delete _monster_array;
}


void Game::_killMonsters(string city_name, vector<Monster *> & monsters)
{
	vector<Monster *>::iterator it;
	bool is_any_monster_printed = false;

	cout << city_name << " has been destroyed by";
	for(it = monsters.begin(); it != monsters.end(); it++)
	{
		if(is_any_monster_printed)
		{
			cout << " and";
		}
		else
		{
			is_any_monster_printed = true;
		}

		cout << " monster " << (*it)->getId();
		(*it)->kill();
	}

	monsters.clear();
	cout << endl;
}


void Game::_resolveConflicts()
{
	int i;
	int l, r;
	City *cur_city;
	unordered_map<City*, vector<Monster *>> city_monsters;
	unordered_map<City*, vector<Monster *>>::iterator it;

	// In first pass, just mark the cities in conflict
	for(i = 0; i < _monster_count; i++)
	{
		cur_city = _monster_array[i].getCity();
		if(city_monsters.find(cur_city) == city_monsters.end())
		{
			city_monsters[cur_city] = vector<Monster *>();
		}
		city_monsters[cur_city].push_back(& _monster_array[i]);
	}

	// In second pass, kill the monsters in conflicting cities, and destroy the cities itself
	for(it = city_monsters.begin(); it != city_monsters.end(); it++)
	{
		if((it->second).size() > 1)
		{
			_killMonsters(it->first->getName(), it->second);
			_game_map->destroyCity(it->first);
		}
	}
	city_monsters.clear();

	// In the last pass, clear the killed or trapped monsters from list
	for(l = 0, r = 0; r < _monster_count; r++)
	{
		if(_monster_array[r].isAlive() && !_monster_array[r].isTrapped())
		{
			_monster_array[l] = _monster_array[r];
			l++;
		}
		else
		{
			if(! _monster_array[r].isAlive())
			{
				_killed_count += 1;
			}
			else if(_monster_array[r].isTrapped())
			{
				_trapped_count += 1;
			}
		}
	}
	_monster_count = l;
}


bool Game::_placeMonsters()
{
	int i;

	cout << "Randomly placing monsters..." << endl;

	// Place monsters one by one randomly
	for(i = 0; i < _monster_count; i++)
	{
		_monster_array[i].setId(i);
		_monster_array[i].setGameMap(_game_map);
		_monster_array[i].placeRandomly();
	}
	
	// If two monsters end up the same place, kill them and destroy cities
	_resolveConflicts();

	// If all monsters are dead even in start-up :) , do not start
	if(! _monster_count)
	{
		cout << "All monsters are dead at start-up! Game is aborted." << endl;
		return false;
	}
	
	return true;
}


void Game::_runGameLoop()
{
	int i, j;

	cout << "Game iteration is started!" << endl;
	
	/*
	In each iteration,
		1. Move each alive monster one by one
		2. Resolve conflicts in all cities (and destroy the conflicting ones)
		3. Clear dead monsters
		4. Check if all monsters dead. If it is so, terminate game
	*/
	for(i = 0; i < _iteration_count; i++)
	{
		for(j = 0; j < _monster_count; j++)
		{
			_monster_array[j].move();
		}

		_resolveConflicts();

		if (! _monster_count)
		{
			cout << "Game over! No movable monsters remained!" << endl;
			cout << "Movable: 0, Killed: " << _killed_count << " Trapped: " << _trapped_count << endl;
			return;
		}
	}

	cout << "Game over! Iteration limit " << _iteration_count << " is exceeded!" << endl;
	cout << "Movable: " << _monster_count << " Killed: " << _killed_count << " Trapped: " << _trapped_count << endl;
}


void Game::playGame()
{
	// If map is already empty, abort the game and report it
	if (_game_map->isEmpty())
	{
		cout << "Map is empty! Game is aborted!" << endl;
		return;
	}

	// Place monsters and start the game only if operation is successful
	if(_placeMonsters())
	{
		_runGameLoop();
	}
}