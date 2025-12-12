from utils import *

size = get_world_size()

def plantRow():
	while True:
		waterTile()
		if can_harvest(): 
			harvest()
		if (get_pos_x() + get_pos_y())%2 == 0:
			plant(Entities.Tree)
		
		move(East)

goTo(0,0)
for y in range(size+1):
	
	if spawn_drone(plantRow):
		goTo(0, y)