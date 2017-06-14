import sys

class City:
	def __init__(self, name, roads):
		self._name = ""
		self._roads = []
		self._monsters = {}

		if name:
			self._name = name
		
		if roads:
			self._roads = roads


	def getNeighbour(self, direction_i):
		if direction_i >= len(self._roads):
			return None
		return self._roads[direction_i]


	def removeNeighbour(self, direction_i):
		if direction_i >= len(self._roads):
			return
		self._roads[direction_i] = None


	def pushMonster(self, monster):
		if monster:
			self._monsters[monster.getId()] = monster


	def popMonster(self, monster):
		if monster:
			monster_id = monster.getId()
			if monster_id in self._monsters:
				del self._monsters[monster_id]


	def inConflict(self):
		return len(self._monsters) > 1


	def killMonsters(self):
		is_any_monster_printed = False
		sys.stdout.write(self._name + " has been destroyed by")
		for monster_id in self._monsters:
			if is_any_monster_printed:
				sys.stdout.write(" and")
			else:
				is_any_monster_printed = True
			sys.stdout.write(" monster " + str(monster_id))
			self._monsters[monster_id].kill()
		self._monsters = {}
		sys.stdout.write("\n")