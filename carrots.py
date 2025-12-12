from utils import *

size = get_world_size()


def plantCol():
	while True:
		tiller(Grounds.Soil)
		waterTile()
		if can_harvest(): 
			harvest()
		plant(Entities.Carrot)
		
		move(East)

goTo(0,0)

for y in range(size+1):	
	if spawn_drone(plantCol):
		goTo(0, y)

