#ifndef _CONFIG_H_
#define _CONFIG_H_

#define ITERATION_COUNT				10000
#define DEFAULT_MONSTER_COUNT		100
#define DEFAULT_MAP_PATH			"./map.txt"

#define ROAD_COUNT 					4
#define DIRECTION_ID_NORTH 			0
#define DIRECTION_ID_EAST 			1
#define DIRECTION_ID_SOUTH 			2
#define DIRECTION_ID_WEST			3
#define PREFIX_NORTH 				"north="
#define PREFIX_EAST 				"east="
#define PREFIX_SOUTH 				"south="
#define PREFIX_WEST					"west="
#define PREFIX_NORTH_LENGTH 		6
#define PREFIX_EAST_LENGTH 			5
#define PREFIX_SOUTH_LENGTH			6
#define PREFIX_WEST_LENGTH			5

#define OPPPOSING_DIRECTION_ID(x)	(x ^ (1 << 1))

#endif