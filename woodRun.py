from utils import *


x2,y2 = 0, 0
compDict = {}

while num_items(Items.Wood) <= 100000:
	if (x2 + y2) % 2 == 0:
		use_item(Items.Water)

	if (get_entity_type() != Entities.Tree):
		if (x2 + y2) % 2 == 0:
			harvest()
			plant(Entities.Tree)

	if (can_harvest() 
	and (x2 + y2) % 2 == 0 
	and get_entity_type() == Entities.Tree):
		grow, (x1, y1) = get_companion()
		
		if (x1,y1) not in compDict or compDict[x1,y1] != grow:
			goTo(x1,y1) 
			harvest()

			if (grow == Entities.Grass):
				plant(grow)

			if (grow == Entities.Carrot):
				if (num_items(Items.Wood) >= 12):
					tiller(Grounds.Soil)
					plant(grow) 
				else:  
					harvest()
					plant(Entities.Tree)

			else:
				plant(grow)

			compDict[x1,y1] = grow

		goTo(x2,y2)
		if can_harvest():
			harvest()
			plant(Entities.Tree)

	if y2 >=9:
		x2 = (x2 + 1) % 10
	y2 = (y2 + 1) % 10

	goTo(x2,y2)