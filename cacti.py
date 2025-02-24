from utils import *
from planter import *
from pumpkins import *

def waterTile():
	if get_water() < 0.90:
		use_item(Items.Water)


resetDrone()

while True: 
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			waterTile()
			tiller(Grounds.Soil)
			
			if can_harvest():
					harvest()

			if get_entity_type() != Entities.Cactus:
					plant(Entities.Cactus)

			goTo(i,j)


