from utils import *
from planter import *
from cactus import *

Size = get_world_size()
# resetDrone()
# while True: 
# 	for i in range(Size):
# 		for j in range(Size):
# 			goTo(i, j)
# 			tiller(Grounds.Soil)
# 			#harvest()


while True:
	plantCactus()
	sortCactus()
	# quick_print(get_tick_count())