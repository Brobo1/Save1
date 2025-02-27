from utils import *

def sortCactus():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goTo(i,j)

			cactusCenter = measure()
			cactusRight = measure(East)
			cactusOver = measure(North)

			if cactusCenter > cactusRight:
				swap(East)
			
			if cactusCenter > cactusOver:
				swap(North)


# while True:
# 	sortCactus()

goTo(0,0)
harvest()