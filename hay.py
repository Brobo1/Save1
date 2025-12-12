from utils import *

size = get_world_size()


def plantCol():
	while True:
		waterTile()
		if can_harvest(): 
			harvest()
		
		move(East)

goTo(0,0)
clear()
for y in range(size+1):
	
	if spawn_drone(plantCol):
		goTo(0, y) 