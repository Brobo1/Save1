from utils import *

x2,y2 = 0, 0
while num_items(Items.Hay) <= 100000:
	grow, (x1,y1) = get_companion()

	if (grow != Entities.Carrot and get_entity_type() == Entities.Grass ):
		goTo(x1,y1)
		plant(grow)
		goTo(x2,y2)
	else:
		goTo(x2,y2)
		
	
	

		quick_print(y2)
	
	if can_harvest():
		y2 = (y2 +1) % 9
		harvest()

