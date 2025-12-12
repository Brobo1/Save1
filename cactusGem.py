from utils import *

size = get_world_size()-1
sorts = 0

def sortCactus():
	global sorts 
	
	for x in range(size):
		if get_entity_type() != None:
			cactusCenter = measure()
			cactusRight = measure(East)
			cactusOver = measure(North)
			cactusLeft = measure(West)
			cactusSouth = measure(South)

			if cactusCenter > cactusRight and get_pos_x() < size:
				swap(East)
				sorts += 1
			
			if cactusCenter > cactusOver and get_pos_y() < size:
				swap(North)
				sorts += 1

			if cactusCenter < cactusSouth and get_pos_y() > 0:
				swap(South)
				sorts += 1

			if cactusCenter < cactusLeft and get_pos_x() > 0:
				swap(West)
				sorts += 1
		
		print(sorts)
		
		move(East)


def plantCactus():
	for x in range(size):

			if get_entity_type() != Entities.Cactus:
				harvest()
				plant(Entities.Cactus)
			move(East)
			
resetDrone()
while True:
	 
	for x in range(size):
		if spawn_drone(plantCactus):
			move(North) 

	while True:
		spawn_drone(sortCactus)
		move(North)
		if sorts == 0:
			break
	harvest()