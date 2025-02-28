from utils import *

grow = None
x1, y1 = 0, 0
x2,y2 = 0, 0


while num_items(Items.Hay) <= 100000:
	goTo(x2,y2)

	if (get_entity_type() == Entities.Grass):
		grow, (x1, y1) = get_companion()

	quick_print(x2,y2)
	quick_print(x1, y1, grow)
	
	if (grow == Entities.Carrot):
		if (num_items(Items.Hay) < 12 and
			num_items(Items.Wood) < 12):
			y2 += 1
		else:
			goTo(x1,y1)
			tiller(Grounds.Soil)
			plant(grow)
	elif (grow != Entities.Carrot):
		goTo(x1,y1)
		plant(grow)

	goTo(x2,y2)
	
	while not can_harvest() and get_entity_type() == Entities.Grass:
		pass

	if can_harvest():
		y2 = (y2 + 1) % 9
		harvest()
	


