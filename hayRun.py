from utils import *


x2,y2 = 0, 0


while num_items(Items.Hay) <= 100000:
	goTo(x2,y2)

	if (get_entity_type() != Entities.Grass):
		harvest()
		if get_ground_type() == Grounds.Soil:
			till()

	if can_harvest():
		grow, (x1, y1) = get_companion()
		if (grow == Entities.Carrot):
			if num_items(Items.Wood) >= 12:
				goTo(x1,y1)
				tiller(Grounds.Soil)
				plant(grow)
			else:	
				harvest()
		else:
			goTo(x1,y1)
			harvest()
			plant(grow)

		goTo(x2,y2)
		harvest()

	if y2 >=9:
		x2 = (x2 + 1) % 10
	y2 = (y2 + 1) % 10

	

	
	


