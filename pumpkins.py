from utils import *
from planter import *
from cactus import *

count = 1
size = get_world_size()
totalSquares = size*size
pumpkinDict = {}



def plantPumpkin():
	global count
	#quick_print(count)
	if count >= totalSquares:
		harvest()
		count = 1
	if get_entity_type() == Entities.Pumpkin:
		count += 1
	else:
		plant(Entities.Pumpkin)
	
	
	

resetDrone()
while True:
	count = 1
	for i in range(size):
		for j in range(size):
			waterTile()
			plantPumpkin()
			goTo(i, j)
			#tiller(Grounds.Soil)
			