from utils import *
from planter import *
from pumpkins import *

# resetDrone()

while True: 
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goTo(i, j)
			waterTile()
			plantPumpkin()
			# if i > 2:
			#     planter(Entities.Pumpkin) 
			# elif (j + i) % 2 == 0: 
			#     planter(Entities.Tree)
			# elif i <= 1:
			#     planter(Entities.Carrot)
			# else: 
			#     planter(Entities.Grass)


