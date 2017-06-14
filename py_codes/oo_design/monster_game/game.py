from monster import Monster

class Game:
	def __init__(self, game_map, monster_count, iteration_count):
		self._map = game_map
		self._mcount = monster_count
		self._icount = iteration_count
		self._monsters = []


	def _clearDeadMonsters(self):
		new_monsters = []
		for monster in self._monsters:
			if monster.isAlive():
				new_monsters.append(monster)
		self._monsters = new_monsters
		self._mcount = len(self._monsters)


	def _placeMonsters(self):
		# Set map for monsters
		Monster.setGameMap(self._map)

		# Place monsters one by one
		for i in xrange(self._mcount):
			self._monsters.append(Monster(i))

		# If two monsters end up the same place, kill them and destroy cities
		self._map.resolveConflicts()

		# Continue with only alive monsters
		self._clearDeadMonsters()

		# If all monsters are dead even in start-up :) , do not start
		if self._monsters:
			return True
		else:
			print "All monsters dead at start-up! Game is aborted."
			return False


	def _runGameLoop(self):
		'''
		In each iteration,
			1. Move each alive monsters one by one
			2. Resolve conflicts in city
			3. Clear dead monsters
			4. Check if all monsters dead. If it is so, terminate game
		'''
		for i in xrange(self._icount):
			for monster in self._monsters:
				monster.move()
			self._map.resolveConflicts()
			self._clearDeadMonsters()
			if self._mcount == 0:
				print "No monsters remained!"
				return

		print "Iteration limit %d is exceeded!" %self._icount
		print "Final monster count:", self._mcount



	def startGame(self):
		# If map is already empty, abort the game and report it
		if self._map.isMapEmpty():
			print "Map is empty! Game is aborted!"
			return

		# Place monsters and start the game
		self._placeMonsters()
		self._runGameLoop()
