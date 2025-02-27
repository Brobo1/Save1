from utils import *
from planter import *


while True: 
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			goTo(i,j)
			tiller(Grounds.Soil)
			plantBush()
			fertilize()
			if can_harvest():
				harvest()