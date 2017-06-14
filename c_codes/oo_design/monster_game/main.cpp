#include <iostream>
#include "utils.h"
#include "gamemap.h"
#include "game.h"
#include "config.h"

using namespace std;


void startProgram(int monster_count)
{
	bool success;
	GameMap game_map;

	// Fill empty map object from file
	success = Utils::loadMapFromFile(game_map, DEFAULT_MAP_PATH);
	cout << "File parsing completed. Success status: " << success << endl;

	// Start only if loading a map file is successful
	if(success)
	{
		cout << "Game is started!" << endl;
		Game game_obj(&game_map, monster_count, ITERATION_COUNT);
		game_obj.playGame();
		cout << "Game is ended!" << endl;
	}
	else
	{
		cout << "Not starting because loading map file is failed!" << endl;
	}
}


int main(int argc, char *argv[])
{
	int parsed_count;
	int monster_count = DEFAULT_MONSTER_COUNT;

	if(argc > 1)
	{
		parsed_count = atoi(argv[1]);
		if (parsed_count < 1)
		{
			cout << "Monster count must be a positive integer! Default value is used instead." << endl;
		}
		else
		{
			monster_count = parsed_count;
		}
	}

	cout << "Monster count is set as " << monster_count << endl;
	startProgram(monster_count);

	return 0;
}
	

