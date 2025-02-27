from utils import *
from planter import *
from cactus import *

# resetDrone()
while num_items(Items.Hay) <= 100000: 
	for i in range(2):
		for j in range(get_world_size()):

			goTo(i, j)
			harvest()


# while True:
# 	plantCactus()
# 	sortCactus()
# 	quick_print(get_tick_count())