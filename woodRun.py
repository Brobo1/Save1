from utils import *


x2,y2 = 0, 0
compDict = {}

while num_items(Items.Wood) <= 100000:
	if (x2+y2)%2 == 0:
		use_item(Items.Water)

	if (get_entity_type() != Entities.Tree):
		if (x2+y2)%2 == 0:
			harvest()
			plant(Entities.Tree)

	if can_harvest() and (x2+y2)%2 == 0:
		grow, (x1, y1) = get_companion()
		quick_print(x1, y1, grow)
		if (grow == Entities.Carrot):
			if num_items(Items.Wood) >= 12:

				if (x1,y1) not in compDict or compDict[x1,y1] != grow:
					goTo(x1,y1)
					harvest()
					tiller(Grounds.Soil)
					plant(grow)
					compDict[x1,y1] = grow
				else: 
					quick_print("Exists")
			else:
				harvest()
				plant(Entities.Tree)
		elif grow == Entities.Grass:
			if (x1,y1) not in compDict or compDict[x1,y1] != grow:
				goTo(x1,y1)
				harvest()
				tiller(Grounds.Grassland)
				compDict[x1,y1] = grow
			else: 
				quick_print("Exists") 
		else:
			if (x1,y1) not in compDict or compDict[x1,y1] != grow:
				goTo(x1,y1)
				harvest()
				plant(grow)
				compDict[x1,y1] = grow
			else: 
				quick_print("Exists")


		goTo(x2,y2)
		if can_harvest():
			harvest()
			plant(Entities.Tree)

	if y2 >=9:
		x2 = (x2 + 1) % 10
	y2 = (y2 + 1) % 10

	goTo(x2,y2)