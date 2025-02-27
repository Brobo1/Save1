from utils import *

def sortCactus():


	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goTo(i,j)

			cactusUnder = measure()
			cactusRight = measure(East)

			if cactusUnder > cactusRight:
				swap(East)

	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goTo(i,j)

			cactusUnder = measure()
			cactusOver = measure(North)

			if cactusUnder > cactusOver:
				swap(North)
	quick_print(cactusUnder, cactusRight)

while True:
	sortCactus()