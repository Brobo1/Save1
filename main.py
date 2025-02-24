from utils import *
from planter import *

# resetDrone()

while True: 
	count = 0
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goTo(i, j)
			waterTile()
			plantPumpkin()
			# if count < get_world_size():
			# 	plantSunflower()
			# elif (i+j) % 2 == 0:
			# 	plantTree()
			# elif count < get_world_size()*4:
			# 	plantCactus()
			# else:
			# 	plantCarrot()

			count+= 1


