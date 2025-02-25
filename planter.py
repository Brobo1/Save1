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


def plantGrass():
	tiller(Grounds.Grassland)
	if can_harvest():
		harvest()

def plantBush():
	tiller(Grounds.Soil)
	if can_harvest():
		harvest()
	plant(Entities.Bush)

def plantTree(): 
	if can_harvest():
		harvest()
	plant(Entities.Tree)


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
	# 	sunflowerList.append({"x":get_pos_x(), "y":get_pos_y(), "pet":measure()})
	
	# if len(sunflowerList) >= 10:
	# 	flowerToPick = sunflowerList[0]
	# 	for petals in sunflowerList:
	# 		if petals["pet"] > flowerToPick["pet"]:
	# 			flowerToPick = petals
	# 	sunflowerList = []

	# 	goTo(flowerToPick["x"], flowerToPick["y"])
		harvest()

	plant(Entities.Sunflower)

def plantCactus(): 
	if can_harvest():
		harvest()
	plant(Entities.Cactus)

def plantPumpkin():
	if can_harvest():
		harvest()
	plant(Entities.Pumpkin)

