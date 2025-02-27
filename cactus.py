from utils import *

def sortCactus():

	while True:
		sorts = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				goTo(i,j)

				cactusCenter = measure()
				cactusRight = measure(East)
				cactusOver = measure(North)
				cactusLeft = measure(West)
				cactusSouth = measure(South)

				if cactusCenter > cactusRight and get_pos_x() < get_world_size()-1:
					swap(East)
					sorts += 1
				
				if cactusCenter > cactusOver and get_pos_y() < get_world_size()-1:
					swap(North)
					sorts += 1

				if cactusCenter < cactusSouth and get_pos_y() > 0:
					swap(South)
					sorts += 1

				if cactusCenter < cactusLeft and get_pos_x() > 0:
					swap(West)
					sorts += 1

		if sorts == 0:
			break

	


def plantCactus():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goTo(i,j)
			tiller(Grounds.Soil)
			if can_harvest():
				harvest()
			plant(Entities.Cactus)