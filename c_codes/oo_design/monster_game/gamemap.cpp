#include "gamemap.h"


GameMap::GameMap()
{

}


int GameMap::_randomize(int min_elem, int max_elem)
{
	if(min_elem >= max_elem)
	{
		return min_elem;
	}

	std::mt19937 rng(random_dev());
	std::uniform_int_distribution<int> uni(min_elem, max_elem - 1);
	return uni(rng);
}


void GameMap::addCity(City* new_city)
{
	if(! new_city)
	{
		return;
	}

	// Here, I accept only the first declaration. The second city is omitted.
	if(_city_graph.find(new_city->getName()) != _city_graph.end())
	{
		return;
	}

	// Assign city objects and names to city graph
	_city_graph[new_city->getName()] = new_city;
}


void GameMap::destroyCity(City *city)
{
	int dir_i;
	int opposing_dir_i;
	string neighbour;

	if(! city)
	{
		return;
	}

	for(dir_i = 0; dir_i < ROAD_COUNT; dir_i++)
	{
		neighbour = city->getNeighbour(dir_i);
		if (neighbour.size() > 0)
		{
			city->removeNeighbour(dir_i);
			opposing_dir_i = OPPPOSING_DIRECTION_ID(dir_i);
			_city_graph[neighbour]->removeNeighbour(opposing_dir_i);
		}
	}

	_city_graph.erase(city->getName());
	delete city;
}


bool GameMap::isEmpty()
{
	return _city_graph.empty();
}


City* GameMap::moveMonster(City* prev_city)
{
	int dir_i;
	string neighbour;
	string next_city_name;
	vector<string> available_city_names;

	// If previous city is NULL, do not do anything
	if(! prev_city)
	{
		return NULL;
	}

	// If previous city is unknown, do not do anything
	if(_city_graph.find(prev_city->getName()) == _city_graph.end())
	{
		return NULL;
	}


	// Traverse all directions and find which ones a monster can move
	for(dir_i = 0; dir_i < ROAD_COUNT; dir_i++)
	{
		neighbour = prev_city->getNeighbour(dir_i);
		if(neighbour.size() > 0)
		{
			available_city_names.push_back(neighbour);
		}
	}

	// If there are not any available cities, do not move
	if(available_city_names.empty())
	{
		return NULL;
	}

	// If at least one city is available, pick a random one and move monster to it
	next_city_name = available_city_names[_randomize(0, available_city_names.size())];
	return _city_graph.find(next_city_name)->second;
}


City* GameMap::placeMonsterRandomly()
{
	unordered_map<string, City*>::iterator it;
	City *city;

	// If map is empty, do not place a monster to a city
	if(isEmpty())
	{
		return NULL;
	}

	// Place monster to a random city
	it = _city_graph.begin();
	std::advance(it, _randomize(0, _city_graph.size()));
	city = it->second;

	return city;
}


GameMap::~GameMap()
{	
	unordered_map<string, City*>::iterator it;
	for(it = _city_graph.begin(); it != _city_graph.end(); it++)
	{
		delete it->second;
	}

	_city_graph.clear();
}