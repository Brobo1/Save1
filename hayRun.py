from utils import *


x2,y2 = 0, 0
compDict = {}

while num_items(Items.Hay) <= 100000:

	if (get_entity_type() != Entities.Grass):
		harvest()
		if get_ground_type() == Grounds.Soil:
			till()

	if can_harvest():
		grow, (x1, y1) = get_companion()
		quick_print(x1, y1, grow)
		if (grow == Entities.Carrot):
			if num_items(Items.Wood) >= 12:

				if (x1,y1) not in compDict:
					goTo(x1,y1)
					tiller(Grounds.Soil)
					plant(grow)
					compDict[x1,y1] = grow
				elif compDict[x1,y1] != grow:
					goTo(x1,y1)
					tiller(Grounds.Soil)
					plant(grow)
					compDict[x1,y1] = grow

			else:
				harvest()
				 
		else:
			if (x1,y1) not in compDict:
				goTo(x1,y1)
				plant(grow)
				compDict[x1,y1] = grow
			elif compDict[x1,y1] != grow:
				goTo(x1,y1)
				harvest()
				plant(grow)
				compDict[x1,y1] = grow


		goTo(x2,y2)
		harvest()

	if y2 >=9:
		x2 = (x2 + 1) % 10
	y2 = (y2 + 1) % 10

	goTo(x2,y2)