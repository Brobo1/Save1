
def makeMaze():
	harvest()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size() * num_unlocked(Unlocks.Mazes))

def pathFinder():
	dirs = [North, East, South, West]
	curDirIndex = 0

	while get_entity_type() != Entities.Treasure:
		dirIndex = (curDirIndex-1)%4

		if move(dirs[dirIndex]):
			curDirIndex = dirIndex
		elif move(dirs[curDirIndex]):
			pass
		else:
			curDirIndex = (curDirIndex+1)%4
	
	if get_entity_type() == Entities.Treasure:
		harvest()

while True:
	makeMaze()
	pathFinder()

# goTo(0,0)