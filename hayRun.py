from utils import *


x2,y2 = 0, 0


while num_items(Items.Hay) <= 100000:
	goTo(x2,y2)

	if (get_entity_type() != Entities.Grass):
		harvest()

	grow, (x1, y1) = get_companion()

	while grow == Entities.Carrot:
		harvest()
		grow, (x1, y1) = get_companion()

	goTo(x1,y1)
	harvest()
	plant(grow)


	goTo(x2,y2)
	
	# while not can_harvest() and get_entity_type() == Entities.Grass:
	# 	if num_items(Items.Fertilizer) > 0:
	# 		use_item(Items.Fertilizer)
	# 	pass
		
	if y2 >=9:
		x2 = (x2 + 1) % 10
	y2 = (y2 + 1) % 10

	if can_harvest():
		harvest()
	

	
	


