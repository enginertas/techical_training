class Monster:
	'''
	I defined map here as static variable,
	Because the monsters are all created on a single map
	'''
	_map = None
	@staticmethod 
	def setGameMap(game_map):
		Monster._map = game_map

	def __init__(self, monster_id):
		self._id = monster_id
		self._alive = True
		self._city_name = None
		if not Monster._map:
			print "Static map object of monster must be set before initialization!"
			return
		Monster._map.placeMonsterRandomly(self)

	def getId(self):
		return self._id

	def getCityName(self):
		return self._city_name

	def setCityName(self, city_name):
		self._city_name = city_name

	def kill(self):
		self._alive = False

	def isAlive(self):
		return self._alive

	def move(self):
		Monster._map.moveMonster(self)
