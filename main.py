from utils import *
from planter import *

# resetDrone()

while True: 
	count = 0
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goTo(i, j)
			waterTile()
			plantBush()
			# fertilize()
			# if count < get_world_size():
			# 	plantSunflower()
			# elif count < get_world_size()*2:
			# 	plantCarrot()
			# else:
			# 	if (i+j) % 2 == 0:
			# 		plantTree()
			# 	else:
			# 		plantGrass()

			# elif count < get_world_size()*4:
			# 	if (i+j) % 2 == 0 and count < get_world_size()*3:
			# 		plantTree()
			# 	else:
			# 		plantCactus()
			# else:
			# 	plantPumpkin()


			count+= 1


