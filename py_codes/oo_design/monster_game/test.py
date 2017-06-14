#!/usr/bin/env python

from utils import Utils
from monster import Monster
from city import City
from gamemap import GameMap

def runUtilTests():
	print "--------------------------------------------"
	print "***** Running Util class tests *****"

	game_map = GameMap()

	assert not Utils.loadMapFromFile(None, None)
	assert not Utils.loadMapFromFile(None, "./map.txt")
	assert not Utils.loadMapFromFile(game_map, None)
	assert not Utils.loadMapFromFile(game_map, "/tmp/asd.txt")
	assert not Utils.loadMapFromFile(game_map, "/etc/shadow")

	assert Utils._parseMapLine(None) == {}
	assert Utils._parseMapLine("") == {}
	assert Utils._parseMapLine("    ") == {}
	assert Utils._parseMapLine("     =    ") == {"city": "=", "roads": {}}
	assert Utils._parseMapLine("     b      ") == {"city": "b", "roads": {}}
	assert Utils._parseMapLine("     b     = ") == {"city": "b", "roads": {}}
	assert Utils._parseMapLine("     b     a = b") == {"city": "b", "roads": {}}
	assert Utils._parseMapLine("     b     a= b") == {"city": "b", "roads": {}}
	assert Utils._parseMapLine("     b     a =b") == {"city": "b", "roads": {}}
	assert Utils._parseMapLine("     b     a=b") == {"city": "b", "roads":{"a": "b"}}
	assert Utils._parseMapLine("     b     a=b       c= 4") == {"city": "b", "roads":{"a": "b"}}
	assert Utils._parseMapLine("     b     a=b       c=4") == {"city": "b", "roads":{"a": "b", "c":"4"}}
	assert Utils._parseMapLine("     b     a=b       c=12    c=4") == {"city": "b", "roads":{"a": "b", "c":"4"}}
	assert Utils._parseMapLine("     b     a=b       c=4    c=12") == {"city": "b", "roads":{"a": "b", "c":"12"}}

	print "***** All tests are OK *****"


def runMonsterTests():
	print "--------------------------------------------"
	print "***** Running Monster class tests *****"

	game_map = GameMap()

	mons1, mons2 = Monster(3), Monster(4)
	assert mons1._map == None
	assert mons2._map == None
	mons1.setGameMap(game_map)
	assert mons1._map == game_map
	assert mons2._map == game_map

	mons3, mons4 = Monster(1), Monster(11)
	assert mons3._map == game_map
	assert mons3._map == game_map

	assert mons1.getId() == 3
	assert mons2.getId() == 4
	assert mons3.getId() == 1
	assert mons4.getId() == 11

	assert mons1.getCityName() == None
	assert mons2.getCityName() == None
	assert mons3.getCityName() == None
	assert mons4.getCityName() == None

	assert mons1.setCityName("Iskenderun") == None
	assert mons2.setCityName("Antakya") == None
	assert mons3.setCityName("Serinyol") == None
	assert mons4.setCityName("Ankara") == None

	assert mons1.getCityName() == "Iskenderun"
	assert mons2.getCityName() == "Antakya"
	assert mons3.getCityName() == "Serinyol"
	assert mons4.getCityName() == "Ankara"

	assert mons1.isAlive()
	assert mons2.isAlive()
	assert mons3.isAlive()
	assert mons4.isAlive()

	mons1.kill()
	mons2.kill()
	mons3.kill()
	mons4.kill()

	assert not mons1.isAlive()
	assert not mons2.isAlive()
	assert not mons3.isAlive()
	assert not mons4.isAlive()

	print "***** All tests are OK *****"


def runCityTests():
	print "--------------------------------------------"
	print "***** Running City class tests *****"

	city1 = City(None, None)
	assert city1._name == ""
	assert city1._roads == []
	assert city1._monsters == {}
	assert city1.getNeighbour(0) == None
	city1.removeNeighbour(0)
	assert city1._roads == []
	city1.pushMonster(None)
	assert city1._monsters == {}
	city1.popMonster(None)
	assert city1._monsters == {}
	assert not city1.inConflict()
	assert city1._monsters == {} 
	city1.killMonsters()
	assert city1._monsters == {} 

	city1 = City("Istanbul", [])
	assert city1._name == "Istanbul"
	assert city1._roads == []
	assert city1.getNeighbour(0) == None
	city1.removeNeighbour(0)
	assert city1._roads == []

	city1 = City("Ankara", ["Bolu"])
	assert city1._name == "Ankara"
	assert city1._roads == ["Bolu"]
	assert city1.getNeighbour(0) == "Bolu"
	assert city1.getNeighbour(1) == None
	city1.removeNeighbour(0)
	assert city1.getNeighbour(0) == None
	assert city1.getNeighbour(1) == None
	assert city1._roads == [None]

	city1 = City("Kirsehir", ["Yozgat", "Cankiri", "Kirikkale", "Ankara"])
	assert city1._name == "Kirsehir"
	assert city1._roads == ["Yozgat", "Cankiri", "Kirikkale", "Ankara"]
	assert city1.getNeighbour(4) == None
	assert city1.getNeighbour(0) == "Yozgat"
	city1.removeNeighbour(0)
	assert city1.getNeighbour(0) == None
	assert city1.getNeighbour(3) == "Ankara"
	city1.removeNeighbour(3)
	assert city1.getNeighbour(3) == None
	assert city1._roads == [None, "Cankiri", "Kirikkale", None]
	assert city1.getNeighbour(1) == "Cankiri"
	city1.removeNeighbour(1)
	assert city1.getNeighbour(1) == None
	assert city1.getNeighbour(2) == "Kirikkale"
	city1.removeNeighbour(2)
	assert city1.getNeighbour(2) == None
	assert city1._roads == [None, None, None, None]

	mons1, mons2, mons3 = Monster(3), Monster(32), Monster(1)

	city1 = City("Karadeniz", ["Tekirdag", "Kocaeli", None, None])
	assert city1._monsters == {}
	assert not city1.inConflict()

	city1.pushMonster(mons1)
	assert city1._monsters == {3: mons1}
	assert not city1.inConflict()

	city1.pushMonster(mons2)
	assert city1._monsters == {3: mons1, 32: mons2}
	assert city1.inConflict()

	city1.pushMonster(mons3)
	assert city1._monsters == {3: mons1, 32: mons2, 1: mons3}
	assert city1.inConflict()

	city1.popMonster(mons1)
	assert city1._monsters == {32: mons2, 1: mons3}
	assert city1.inConflict()

	city1.popMonster(mons2)
	assert city1._monsters == {1: mons3}
	assert not city1.inConflict()

	city1.popMonster(mons3)
	assert city1._monsters == {}
	assert not city1.inConflict()

	assert mons1.isAlive()
	assert mons2.isAlive()
	assert mons3.isAlive()
	city1.pushMonster(mons1)
	city1.pushMonster(mons2)
	city1.pushMonster(mons3)
	city1.killMonsters()
	assert city1._monsters == {}
	assert not mons1.isAlive()
	assert not mons2.isAlive()
	assert not mons3.isAlive()

	print "***** All tests are OK *****"


def runGameMapTests():
	print "--------------------------------------------"
	print "***** Running GameMap class tests *****"

	assert GameMap._calcOpposingDirectionIndex(0) == 2
	assert GameMap._calcOpposingDirectionIndex(2) == 0
	assert GameMap._calcOpposingDirectionIndex(1) == 3
	assert GameMap._calcOpposingDirectionIndex(3) == 1

	game_map1 = GameMap()
	game_map1.addCity(None)
	game_map1.addCity({})
	game_map1.addCity({"city": "A"})
	game_map1.addCity({"roads": {}})
	assert game_map1._city_name_array == []
	assert game_map1._graph == {}
	assert game_map1.isMapEmpty()

	# Try to place monster to map, when map is empty
	mons1 = Monster(10)
	assert mons1.getCityName() == None
	game_map1.placeMonsterRandomly(mons1)
	assert mons1.getCityName() == None

	game_map1.addCity({"city": "A", "roads":{}})
	assert game_map1._graph["A"]._roads == [None, None, None, None]
	assert game_map1._graph["A"]._name == "A"
	assert game_map1._city_name_array == ["A"]
	assert not game_map1.isMapEmpty()

	game_map1.addCity({"city": "B", "roads":{"south": "C", "north": "A"}})
	assert game_map1._graph["A"]._roads == [None, None, None, None]
	assert game_map1._graph["A"]._name == "A"
	assert game_map1._graph["B"]._roads == ["A", None, "C", None]
	assert game_map1._graph["B"]._name == "B"
	assert game_map1._city_name_array == ["A", "B"]
	assert not game_map1.isMapEmpty()

	game_map1.addCity({"city": "C", "roads":{"east": "D", "west": "E"}})
	assert game_map1._graph["A"]._roads == [None, None, None, None]
	assert game_map1._graph["A"]._name == "A"
	assert game_map1._graph["B"]._roads == ["A", None, "C", None]
	assert game_map1._graph["B"]._name == "B"
	assert game_map1._graph["C"]._roads == [None, "D", None, "E"]
	assert game_map1._graph["C"]._name == "C"
	assert game_map1._city_name_array == ["A", "B", "C"]
	assert not game_map1.isMapEmpty()


	mons1 = Monster(10)
	game_map1.placeMonsterRandomly(mons1)
	assert mons1.getCityName() in ["A", "B", "C"]
	
	# City is not in map at all
	mons1._city_name = "TTT"
	game_map1.moveMonster(mons1)
	assert mons1.getCityName() == "TTT"

	# City is not in map as node (it is located as vertex)
	mons1._city_name = "D"
	game_map1.moveMonster(mons1)
	assert mons1.getCityName() == "D"

	# City has not any neighbors
	mons1._city_name = "A"
	game_map1.moveMonster(mons1)
	assert mons1.getCityName() == "A"

	# City has neighbors
	mons1._city_name = "B"
	game_map1.moveMonster(mons1)
	assert mons1.getCityName() in ["A", "C"]

	# Move to make conflicts
	game_map2 = GameMap()
	game_map2.addCity({"city": "A", "roads":{"south": "B"}})
	game_map2.addCity({"city": "B", "roads":{"north": "A"}})
	mons1, mons2, mons3 = Monster(10), Monster(20), Monster(40)
	game_map2.placeMonsterRandomly(mons1)
	game_map2.placeMonsterRandomly(mons2)
	game_map2.placeMonsterRandomly(mons3)
	assert game_map2._cities_in_conflict != {}
	assert mons1.isAlive() and  mons2.isAlive() and mons3.isAlive() 
	assert len(game_map2._graph) == 2

	game_map2.resolveConflicts()
	assert game_map2._cities_in_conflict == {}	
	not_alive_count = 0
	if not mons1.isAlive():
		not_alive_count += 1
	if not mons2.isAlive():
		not_alive_count += 1
	if not mons3.isAlive():
		not_alive_count += 1
	assert not_alive_count >= 2

	assert len(game_map2._graph) == 1
	remaining_city_name = None
	for city in game_map2._graph:
		remaining_city_name = city
	assert game_map2._graph[remaining_city_name]._roads == [None, None, None, None]

	print "***** All tests are OK *****"



if __name__ == "__main__":
	runUtilTests()
	runMonsterTests()
	runCityTests()
	runGameMapTests()