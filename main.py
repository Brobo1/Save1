from utils import *
from planter import *
from cactus import *

# resetDrone()

# while True: 
# 	count = 0
# 	for i in range(get_world_size()):
# 		for j in range(get_world_size()):
# 			goTo(i, j)
# 			waterTile()
# 			plantCactus()
# 			count+= 1


while True:
	plantCactus()
	sortCactus()
	quick_print(get_tick_count())