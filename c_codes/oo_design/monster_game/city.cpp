#include "city.h"

City::City()
{

}


City::City(string name, string roads[ROAD_COUNT])
{
	int i;

	_city_name = name;
	for(i = 0; i < ROAD_COUNT; i++)
	{
		_city_roads[i] = roads[i];
	}
}


string City::getName()
{
	return _city_name;
}


string City::getNeighbour(int direction_i)
{
	if(direction_i >= ROAD_COUNT)
	{
		return string("");
	}
	
	return _city_roads[direction_i];
}


void City::removeNeighbour(int direction_i)
{
	if(direction_i >= ROAD_COUNT)
	{
		return;
	}

	_city_roads[direction_i] = "";
}