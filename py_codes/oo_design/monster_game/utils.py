import traceback

DEFAULT_ASSIGNMENT_CHAR = '='

class Utils:
	@staticmethod
	def _parseMapLine(file_line):
		# If file line is empty, do not process it.
		if not file_line:
			return {}

		# Split line. If it is full of whitespaces, do not process it.
		splitted_line = [x.strip() for x in file_line.split()]
		if not splitted_line:
			return {}

		# Accept first element as city
		city_obj = {"city": splitted_line[0], "roads": {}}

		'''
		Traverse all remaining strings
		Only consider strings with assingment character
		Accept (key, value) as valid pair, only if they are not empty
		'''
		for i in xrange(1, len(splitted_line)):
			assign_index = splitted_line[i].find(DEFAULT_ASSIGNMENT_CHAR)
			if assign_index >= 0:
				key, value = splitted_line[i][:assign_index], splitted_line[i][assign_index + 1:]
				if key and value:
					city_obj["roads"][key] = value

		return city_obj


	@staticmethod
	def loadMapFromFile(game_map, map_file_path):
		if (not game_map) or (not map_file_path):
			return False

		try:
			with open(map_file_path, "r") as file_obj:
				for file_line in file_obj:
					'''
					Try to parse every map line
					Add line to map, only if it is successful.
					If a line is corrupted, do NOT return fail for whole loading process
					'''
					city_obj = Utils._parseMapLine(file_line)
					if city_obj:
						game_map.addCity(city_obj)
						pass

		except Exception, ex:
			# In total failure in reading of file, report and return fail
			traceback.print_exc()
			return False

		return True