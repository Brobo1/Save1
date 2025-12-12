from utils import *


size = get_world_size()
totalSquares = size*size
pumpkinDict = {}




def plantRow():
	#quick_print(count)
	count = 1
	while count <= size:
		# if count >= size:
		# 	harvest()
		tiller(Grounds.Soil)
		waterTile()
		if get_entity_type() == Entities.Pumpkin:
			count += 1
		elif get_entity_type() == Entities.Dead_Pumpkin: 
			plant(Entities.Pumpkin)
			count = 1
		else: 
			count = 1
			harvest()
			plant(Entities.Pumpkin)
		move(East)
	
	
	

resetDrone()

# goTo(0,0)
while True:
	for y in range(size+1):
		
		if spawn_drone(plantRow):
			goTo(0, y)

	harvest()