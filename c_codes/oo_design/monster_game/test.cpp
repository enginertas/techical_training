#include <iostream>
#include <string>
#include <cassert>
#include "city.h"
#include "monster.h"
#include "utils.h"
#include "gamemap.h"

using namespace std;

class CityTest
{
public:
	void runCityTests()
	{
		cout << "-------- Running City Tests --------" << endl;

		string roads[4];
		roads[0] = "";
		roads[1] = "";
		roads[2] = "";
		roads[3] = "";
		
		// Empty City strings test
		City city1(string(""), roads);
		assert(city1.getName().compare(string("")) == 0);
		assert(city1.getNeighbour(0).compare(string("")) == 0);
		assert(city1.getNeighbour(1).compare(string("")) == 0);
		assert(city1.getNeighbour(2).compare(string("")) == 0);
		assert(city1.getNeighbour(3).compare(string("")) == 0);
		assert(city1.getNeighbour(4).compare(string("")) == 0);

		// Filled City strings test
		roads[0] = "neighbour0";
		roads[1] = "neighbour1";
		roads[2] = "neighbour2";
		roads[3] = "neighbour3";
		City city2(string("Yozgat"), roads);
		assert(city2.getName().compare(string("Yozgat")) == 0);
		assert(city2.getNeighbour(0).compare(string("neighbour0")) == 0);
		assert(city2.getNeighbour(1).compare(string("neighbour1")) == 0);
		assert(city2.getNeighbour(2).compare(string("neighbour2")) == 0);
		assert(city2.getNeighbour(3).compare(string("neighbour3")) == 0);
		assert(city2.getNeighbour(4).compare(string("")) == 0);
		city2.removeNeighbour(0);
		city2.removeNeighbour(1);
		city2.removeNeighbour(2);
		city2.removeNeighbour(3);
		city2.removeNeighbour(4);
		assert(city2.getName().compare(string("Yozgat")) == 0);
		assert(city2.getNeighbour(0).compare(string("")) == 0);
		assert(city2.getNeighbour(1).compare(string("")) == 0);
		assert(city2.getNeighbour(2).compare(string("")) == 0);
		assert(city2.getNeighbour(3).compare(string("")) == 0);
		assert(city2.getNeighbour(4).compare(string("")) == 0);

		cout << "Tests are OK" << endl;
	}

};


class MonsterTest
{
public:
	void runMonsterTests()
	{
		cout << "-------- Running Monster Tests --------" << endl;
	
		GameMap map;

		// Empty monster object
		Monster monster1;
		assert(monster1.getId() == -1);
		assert(monster1._game_map == NULL);
		assert(monster1.getCity() == NULL);
		assert(monster1.isAlive());
		assert(! monster1.isTrapped());

		// Monster object after set id
		assert(monster1.getId() == -1);
		monster1.setId(1231);
		assert(monster1.getId() == 1231);

		// Monster object after set game map
		assert(monster1._game_map == NULL);
		monster1.setGameMap(&map);
		assert(monster1._game_map == &map);

		// Monster object after kill
		assert(monster1.isAlive());
		monster1.kill();
		assert(! monster1.isAlive());

		// Try to place monster1 when map is empty. Monster needs to be set "trapped"
		monster1.placeRandomly();
		assert(monster1.getCity() == NULL);
		assert(monster1.isTrapped());

		// Try to move it. It cannot go anywere, and it is still trapped
		monster1.move();
		assert(monster1.getCity() == NULL);
		assert(monster1.isTrapped());

		// Try to move a monster which is not placed before. It needs to be set "trapped" after move.
		Monster monster2;
		assert(! monster2.isTrapped());
		monster2.move();
		assert(monster1.getCity() == NULL);
		assert(monster2.isTrapped());

		// Add a city to map. Create a monster. Place it. It will not be "trapped" first. Then, it will "trapped" after move
		string roads[4];
		roads[0] = "";
		roads[1] = "";
		roads[2] = "";
		roads[3] = "";
		City* city1 = new City("Yozgat", roads);
		map.addCity(city1);
		Monster monster3;
		monster3.setGameMap(&map);
		assert(monster3.getCity() == NULL);
		assert(! monster3.isTrapped());
		monster3.placeRandomly();
		assert(monster3.getCity() == city1);
		assert(! monster3.isTrapped());
		monster3.move();
		assert(monster3.getCity() == city1);
		assert(monster3.isTrapped());

		// Use a second map with two cities. Create a monster. It will not be "trapped" at all.
		GameMap map2;
		roads[0] = "Yozgat";
		City *city2 = new City("Cankiri", roads);
		map2.addCity(city2);
		Monster monster4;
		monster4.setGameMap(&map2);
		assert(monster4.getCity() == NULL);
		assert(! monster4.isTrapped());
		monster4.placeRandomly();
		assert(monster4.getCity() == city2);
		assert(! monster4.isTrapped());
		roads[0] = "";
		roads[2] = "Cankiri";
		City *city3 = new City("Yozgat", roads);
		map2.addCity(city3);
		monster4.move();
		assert(monster4.getCity() == city3);
		assert(! monster4.isTrapped());

		cout << "Tests are OK" << endl;
	}

};



class UtilsTest 
{
public:
	void runUtilsTests()
	{
		City *city_p;
		cout << "-------- Running Util Tests --------" << endl;

		// Parse Map Line Tests
		assert(Utils::_parseMapLine(string("")) == NULL);
		assert(Utils::_parseMapLine(string("      ")) == NULL);
		assert(Utils::_parseMapLine(string("       \t\n \t \n \r\n \r \n ")) == NULL);
		city_p = Utils::_parseMapLine(string("       \t\n \t \n \r\nali\r\n \r\n \r \n "));
		assert(city_p->getName().compare("ali") == 0);
		assert(city_p->getNeighbour(0).compare("") == 0);
		assert(city_p->getNeighbour(1).compare("") == 0);
		assert(city_p->getNeighbour(2).compare("") == 0);
		assert(city_p->getNeighbour(3).compare("") == 0);
		delete city_p;
		city_p = Utils::_parseMapLine(string("       \t\n \t \n \r\nali\r\n north=\r\n \r \n "));
		assert(city_p->getNeighbour(0).compare("") == 0);
		delete city_p;
		city_p = Utils::_parseMapLine(string("       \t\n \t \n \r\nali\r\n north=d\r\n east=\r \n "));
		assert(city_p->getNeighbour(0).compare("d") == 0);
		assert(city_p->getNeighbour(1).compare("") == 0);
		delete city_p;
		city_p = Utils::_parseMapLine(string("       \t\n \t \n \r\nali\r\n north=d\r\n east=x \r south=\n "));		
		assert(city_p->getNeighbour(0).compare("d") == 0);
		assert(city_p->getNeighbour(1).compare("x") == 0);
		assert(city_p->getNeighbour(2).compare("") == 0);
		delete city_p;
		city_p = Utils::_parseMapLine(string("       \t\n \t \n \r\nali\r\n north=d\r\n east=x \r south=asde\n west="));		
		assert(city_p->getNeighbour(0).compare("d") == 0);
		assert(city_p->getNeighbour(1).compare("x") == 0);
		assert(city_p->getNeighbour(2).compare("asde") == 0);
		assert(city_p->getNeighbour(3).compare("") == 0);
		delete city_p;
		city_p = Utils::_parseMapLine(string("       \t\n \t \n \r\nali\r\n north=d\r\n east=x \r south=asde\n west=dalida"));	
		assert(city_p->getNeighbour(0).compare("d") == 0);
		assert(city_p->getNeighbour(1).compare("x") == 0);
		assert(city_p->getNeighbour(2).compare("asde") == 0);
		assert(city_p->getNeighbour(3).compare("dalida") == 0);
		delete city_p;

		// Load Map From File Tests
		GameMap map;
		assert(! Utils::loadMapFromFile(map, NULL));
		assert(! Utils::loadMapFromFile(map, ""));
		assert(! Utils::loadMapFromFile(map, "map123131.txt"));
		assert(! Utils::loadMapFromFile(map, "/etc/shadow"));
		assert(Utils::loadMapFromFile(map, "./map.txt"));


		cout << "Tests are OK" << endl;
	}

};


class GameMapTest
{
public:
	void runGameMapTests()
	{
		cout << "-------- Running GameMap Tests --------" << endl;
		
		// Randomize tests. Tests may be run several times
		GameMap map1;
		assert(map1._randomize(6, 5) == 6);
		assert(map1._randomize(12, 12) == 12);
		assert(map1._randomize(44, 45) == 44);
		assert(map1._randomize(44, 45) == 44);
		assert(map1._randomize(44, 45) == 44);
		assert(map1._randomize(44, 45) == 44);
		assert(map1._randomize(342, 343) == 342);
		assert(map1._randomize(342, 343) == 342);
		assert(map1._randomize(342, 343) == 342);
		assert(map1._randomize(342, 343) == 342);
		assert(map1._randomize(342, 343) == 342);
		int result = map1._randomize(20, 22);
		assert(result == 20 || result == 21);
		result = map1._randomize(20, 22);
		assert(result == 20 || result == 21);
		result = map1._randomize(20, 22);
		assert(result == 20 || result == 21);
		result = map1._randomize(20, 22);
		assert(result == 20 || result == 21);
		result = map1._randomize(40, 43);
		assert(result == 40 || result == 41 || result == 42);
		result = map1._randomize(40, 43);
		assert(result == 40 || result == 41 || result == 42);
		result = map1._randomize(40, 43);
		assert(result == 40 || result == 41 || result == 42);
		result = map1._randomize(40, 43);
		assert(result == 40 || result == 41 || result == 42);

		// Empty check before and after empty add city request
		assert(map1.isEmpty());
		map1.addCity(NULL);
		assert(map1.isEmpty());

		// Try to place a monster when map is empty
		assert(map1.placeMonsterRandomly() == NULL);

		// Try to move with a null city
		assert(map1.moveMonster(NULL) == NULL);

		// Create test cities
		string roads[4];
		roads[0] = "Cankiri";
		roads[1] = "";
		roads[2] = "";
		roads[3] = "";
		City* city1 = new City("Yozgat", roads);
		roads[0] = "";
		roads[2] = "Yozgat";
		City *city2 = new City("Cankiri", roads);

		// Try to find the cities before addition
		assert(map1._city_graph.find("Yozgat") == map1._city_graph.end());
		assert(map1._city_graph.find("Cankiri") == map1._city_graph.end());

		// Try to find the cities after addition
		map1.addCity(city1);
		assert(! map1.isEmpty());
		assert(map1._city_graph.find("Yozgat")->second == city1);
		assert(map1._city_graph.find("Cankiri") == map1._city_graph.end());		

		// Try to place a monster and you will get the only city as response
		assert(map1.placeMonsterRandomly() == city1);

		// Try to move the monster in city 2 and make it fail
		assert(map1.moveMonster(city2) == NULL);

		// Add second city to map
		map1.addCity(city2);
		assert(! map1.isEmpty());
		assert(map1._city_graph.find("Yozgat")->second == city1);
		assert(map1._city_graph.find("Cankiri")->second == city2);		

		// Check if moves are correct
		assert(map1.moveMonster(city1) == city2);
		assert(map1.moveMonster(city2) == city1);
		
		// Check if conflicting city name is omitted
		City *city3 = new City("Cankiri", roads);
		map1.addCity(city3);
		assert(map1._city_graph.find("Cankiri")->second == city2);	
		delete city3;
		
		// Try to destroy city which is empty and see if any problem occurs
		map1.destroyCity(NULL);
		assert(! map1.isEmpty());
		assert(map1._city_graph.size() == 2);

		// Destroy city1 and make some checks
		map1.destroyCity(city1);
		assert(! map1.isEmpty());
		assert(map1._city_graph.size() == 1);
		assert(map1._city_graph.find("Yozgat") == map1._city_graph.end());
		assert(map1._city_graph.find("Cankiri")->second == city2);
		assert(map1.moveMonster(city2) == NULL);
		assert(city2->getNeighbour(0).compare("") == 0);
		assert(city2->getNeighbour(1).compare("") == 0);
		assert(city2->getNeighbour(2).compare("") == 0);
		assert(city2->getNeighbour(3).compare("") == 0);

		// Try to place a monster and you will get the only city as response
		assert(map1.placeMonsterRandomly() == city2);

		// Check if moves are not possible
		assert(map1.moveMonster(city2) == NULL);

		// Destroy city2 and make some checks
		map1.destroyCity(city2);
		assert(map1.isEmpty());
		assert(map1._city_graph.size() == 0);
		assert(map1._city_graph.find("Yozgat") == map1._city_graph.end());
		assert(map1._city_graph.find("Cankiri") == map1._city_graph.end());
		assert(map1.placeMonsterRandomly() == NULL);

		cout << "Tests are OK" << endl;
	}
};



int main(int argc, char *argv[])
{
	CityTest().runCityTests();
	MonsterTest().runMonsterTests();
	UtilsTest().runUtilsTests();
	GameMapTest().runGameMapTests();

	cout << "******* ALL TESTS ARE OK *******" << endl;
	
	return 0;
}