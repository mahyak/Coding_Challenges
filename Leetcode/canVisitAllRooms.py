class Solution:
	def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
		num = len(rooms)
		keys = [0]
		unlocked = set()
        
		def collectKeys(n):
			for key in rooms[n]:
				if key not in  keys:
					keys.append(key)

		i = 0
		while i < len(keys):
			unlocked.add(keys[i])
			collectKeys(keys[i])
			i += 1

		if len(unlocked) == num:
			return True
		else:
			return False
        
