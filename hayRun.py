from utils import *

grow = None
x1, y1 = 0, 0
x2,y2 = 0, 0


while num_items(Items.Hay) <= 100000:

	goTo(x2,y2)
	if (get_entity_type() == Entities.Grass):
		grow, (x1, y1) = get_companion()
	else:
		harvest()

	quick_print(x2,y2)
	quick_print(x1, y1, grow)

	if (grow != Entities.Carrot):
		goTo(x1,y1)
		harvest()
		plant(grow)
	else:
		harvest()
		y2 = (y2 + 1) % 9

	goTo(x2,y2)
	
	while not can_harvest() and get_entity_type() == Entities.Grass:
		if num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)
		pass

	y2 = (y2 + 1) % 9
	if can_harvest():
		harvest()

	


