from utils import *

pumpkinList = []

def plantPumpkin():
	global pumpkinList 
	if (get_entity_type() == Entities.Pumpkin):
		pumpkinList.append(get_entity_type())
	else:
		tiller(Grounds.Soil)
		plant(Entities.Pumpkin)

	if pumpkinList.len() == (get_world_size()**2):
		pumpkinList = []
		return True
	else: 
		return False  