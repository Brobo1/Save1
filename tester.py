from utils import *
from planter import *

def makeMaze():
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, 3)

def pathFinder():
	dirs = [North, East, South, West]
	moveIndex = 0
	while get_entity_type() != Entities.Treasure:
		move(dirs[moveIndex])
	quick_print(move(dirs[1]))

# makeMaze()
pathFinder()

# goTo(0,0)