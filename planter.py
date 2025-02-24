from utils import *

sunflowerList = []

def planter(plantType):
	if (get_ground_type() != Grounds.Soil 
		and (plantType == Entities.Carrot
		or plantType == Entities.Pumpkin)):
		till()

	if (get_ground_type() != Grounds.Grassland 
		and plantType == Entities.Grass):
		till()

	if can_harvest():
		harvest()

	if get_entity_type() != plantType:
		plant(plantType)


def plantCarrot(): 
	tiller(Grounds.Soil)

	if can_harvest():
		harvest()

	plant(Entities.Carrot)


def plantSunflower():
	global sunflowerList

	tiller(Grounds.Soil)

	if can_harvest():
		sunflowerList.append({"x":get_pos_x(), "y":get_pos_y(), "pet":measure()})
	quick_print(sunflowerList[sunflowerList.len()-1])
	plant(Entities.Sunflower)