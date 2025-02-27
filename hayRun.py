from utils import *


while num_items(Items.Hay) <= 100000:
	for i in range(get_world_size()):
		grow, (x,y) = get_companion()
		quick_print(grow, x,y)
		harvest()
		move(North)
	move(East)

