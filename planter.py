from utils import *


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


sunflowerList = []

def plantSunflower():
	global sunflowerList
 
	tiller(Grounds.Soil)

	if can_harvest():
		sunflowerList.append({"x":get_pos_x(), "y":get_pos_y(), "pet":measure()})

	
	if len(sunflowerList) >= 10:
		flowerToPick = sunflowerList[0]
		for petals in sunflowerList:
			if petals["pet"] > flowerToPick["pet"]:
				flowerToPick = petals
		quick_print(flowerToPick)
		sunflowerList = []

	plant(Entities.Sunflower)