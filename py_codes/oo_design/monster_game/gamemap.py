from random import randint
from city import City

class GameMap:
	def __init__(self):
		self._graph = {}
		self._city_name_array = []
		self._cities_in_conflict = {}
		self._DIRECTION_COUNT = 4
		self._DIRECTION_INDEXES = {
			"north" : 0, 
			"east" : 1, 
			"south": 2, 
			"west": 3
			}


	@staticmethod
	def _calcOpposingDirectionIndex(direction_i):
		return direction_i ^ (1 << 1)


	def addCity(self, city_obj):
		# If city object or either of its related fields is None, directly return
		if (not city_obj) or ("city" not in city_obj) or ("roads" not in city_obj):
			return

		city_name = city_obj["city"]

		# Here, I accept only the first declaration
		if city_name in self._graph:
			return

		# Fill found & well-defined roads to empty road array 
		roads = [None, None, None, None]
		for direction in city_obj["roads"]:
			if direction in self._DIRECTION_INDEXES:
				roads[self._DIRECTION_INDEXES[direction]] = city_obj["roads"][direction]

		# Assign road array to city on graph
		self._graph[city_name] = City(city_name, roads)

		# Append city name to array
		# City array is for randomization purposes
		self._city_name_array.append(city_name)


	def _destroyCity(self, city_name, city):
		# If city is not defined, directly return
		if not city:
			return

		# Traverse all directions and remove connections to current city
		for direction_i in xrange(self._DIRECTION_COUNT):
			neighbour = city.getNeighbour(direction_i)
			if neighbour:
				opposing_direction_i = self._calcOpposingDirectionIndex(direction_i)
				self._graph[neighbour].removeNeighbour(opposing_direction_i)

		# Remove city from map
		del self._graph[city_name]


	def isMapEmpty(self):
		return len(self._city_name_array) == 0


	def moveMonster(self, monster):
		prev_city_name = monster.getCityName()

		# If previous city is unknown, do not do anything
		if prev_city_name not in self._graph:
			return

		prev_city = self._graph[prev_city_name]

		# Traverse all directions and find which ones a monster can move
		available_city_names = []
		for direction_i in xrange(self._DIRECTION_COUNT):
			neighbour = prev_city.getNeighbour(direction_i)
			if neighbour:
				available_city_names.append(neighbour)

		# If there are not any available cities, do not move
		if not available_city_names:
			return

		# If at least one city is available, pick a random one and move monster to it
		next_city_name = available_city_names[randint(0, len(available_city_names) - 1)]
		next_city = self._graph[next_city_name]
		monster.setCityName(next_city_name)
		prev_city.popMonster(monster)
		next_city.pushMonster(monster)

		# If previous city is not in trouble, drop it from conflict list
		if (prev_city_name in self._cities_in_conflict) and (not prev_city.inConflict()):
			del self._cities_in_conflict[prev_city_name]

		# If next city is in conflict, add it to conflict list
		if next_city.inConflict():
			self._cities_in_conflict[next_city_name] = True


	def placeMonsterRandomly(self, monster):
		# If city name array is empty, do not place a monster to a city
		if not self._city_name_array:
			return

		# Place monster to a random city
		city_index = randint(0, len(self._city_name_array) - 1)
		city_name = self._city_name_array[city_index]
		monster.setCityName(city_name)
		self._graph[city_name].pushMonster(monster)
		
		# If next city is in conflict, add it to conflict list
		if self._graph[city_name].inConflict():
			self._cities_in_conflict[city_name] = True


	def resolveConflicts(self):
		# For each city, kill monsters first and destroy the city
		for city_name in self._cities_in_conflict:
			city = self._graph[city_name]
			city.killMonsters()
			self._destroyCity(city_name, city)

		self._cities_in_conflict = {}