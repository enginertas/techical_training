#include "utils.h"


City* Utils::_parseMapLine(string file_line)
{
	unsigned i;
	string city_name;
	string destination_name;
	string city_roads[ROAD_COUNT];
	vector<string> splitted_line;

	// If file_line is empty, return an empty city
	if(! file_line.size())
	{
		return NULL;
	}

	// Split line. If it is full of whitespaces, do not process it
	istringstream iss(file_line);
	copy(istream_iterator<string>(iss), istream_iterator<string>(), back_inserter(splitted_line));
	if(splitted_line.empty())
	{
		return NULL;
	}

	// Accept first element as city
	city_name = splitted_line[0];

	/*
	Traverse all remaining strings
	Only consider strings with valid assingment strings
	Accept (key, value) as valid pair, only if they are not empty
	*/
	for (i = 1; i < splitted_line.size(); i++)
	{
		if(splitted_line[i].size() > PREFIX_NORTH_LENGTH && (! splitted_line[i].find(PREFIX_NORTH)))
		{
			city_roads[DIRECTION_ID_NORTH] = splitted_line[i].substr(PREFIX_NORTH_LENGTH);
		}
		else if(splitted_line[i].size() > PREFIX_EAST_LENGTH && (! splitted_line[i].find(PREFIX_EAST)))
		{
			city_roads[DIRECTION_ID_EAST] = splitted_line[i].substr(PREFIX_EAST_LENGTH);
		}
		else if(splitted_line[i].size() > PREFIX_SOUTH_LENGTH && (! splitted_line[i].find(PREFIX_SOUTH)))
		{
			city_roads[DIRECTION_ID_SOUTH] = splitted_line[i].substr(PREFIX_SOUTH_LENGTH);
		}
		else if(splitted_line[i].size() > PREFIX_WEST_LENGTH && (! splitted_line[i].find(PREFIX_WEST)))
		{
			city_roads[DIRECTION_ID_WEST] = splitted_line[i].substr(PREFIX_WEST_LENGTH);
		}
	}

	return new City(city_name, city_roads);

}


bool Utils::loadMapFromFile(GameMap & game_map, const char* path)
{
	ifstream in;
	string line;
	City* new_city;

	if(! path)
	{
		cout << "Map file path is not specified!" << endl;
		return false;
	}

	// Try to open the given file path
	in.open(path, ifstream::in);
	
	// Fetch and parse all lines
	while(getline(in, line))
	{
		/*
		Add city to map, only if it is not NULL.
		If a line is corrupted, do NOT return fail for whole loading process 
		*/
		Utils::_parseMapLine(line);
		new_city = Utils::_parseMapLine(line);
		if (new_city)
		{
			game_map.addCity(new_city);
		}
	}
	
	if(!in.eof())
	{
		// In case of error, report it and directly exit
		cout << "Configuration could not be read from file " << path << " : " << strerror(errno) << endl;
		return false;
	}

	return true;
}