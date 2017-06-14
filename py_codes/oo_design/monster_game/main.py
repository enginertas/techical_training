#!/usr/bin/env python

import sys
from utils import Utils
from game import Game
from gamemap import GameMap


ITERATION_COUNT = 10000
DEFAULT_MONSTER_COUNT = 100
DEFAULT_MAP_PATH = "./map.txt"


def startProgram(monster_count):
	# Create an empty map object
	game_map = GameMap()

	# Fill empty map object from file
	is_success= Utils.loadMapFromFile(game_map, DEFAULT_MAP_PATH)
	print "File parsing completed. Success status:", is_success

	# Start only if loading a map file is successful
	if is_success:
		print "Game is started!"
		game_obj = Game(game_map, monster_count, ITERATION_COUNT)
		game_obj.startGame()
		print "Game is ended!"
	else:
		print "Not starting because loading map file is failed"


if __name__ == "__main__":
	Monster_Count = DEFAULT_MONSTER_COUNT

	# Try to parse monster count as integer from Command Line
	# In case of fail, monster count is already set
	if len(sys.argv) > 1:
		try:
			Parsed_Value = int(sys.argv[1])
			if Parsed_Value < 1:
				print "Monster count cannot be zero or negative! Default value is used."
			else:
				Monster_Count = Parsed_Value
		except Exception, ex:
			print ex
			print "Cannot set monster count from command line! Default value is used."
		
	print "Monster count is set as", Monster_Count

	startProgram(Monster_Count)	
	

