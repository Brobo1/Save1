from utils import *
from planter import *
from cactus import *

		
#set_execution_speed(8)
#set_world_size(3)

size = get_world_size()
sizeSqrt = size * size
carrotsPerPumpkin = 32


		

 
while True: 
	resetDrone()
	
	while entityAmount(Items.Carrot) < 1000000:
		for x in range(2):
			for y in range(size):
				if can_harvest():
					harvest()
				goTo(x, y)
				waterTile()
				tiller(Grounds.Soil)
				plant(Entities.Carrot)

	pumpkinDict = {}
	for x in range(size):
		for y in range(size):
			pumpkinDict[x, y] = None
	while len(pumpkinDict) != 0:
		for (x, y) in list(pumpkinDict):
			goTo(x, y)
			waterTile()
			tiller(Grounds.Soil)
			if get_entity_type() == Entities.Pumpkin and can_harvest():
				pumpkinDict.pop((x,y))
				quick_print(pumpkinDict, len(pumpkinDict))
			else:
				plant(Entities.Pumpkin)
			
			
	while can_harvest() == False:
		print("Waiting...")
	harvest()