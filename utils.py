worldSize = get_world_size()

def resetDrone():
	while get_pos_x() != 0:
		move(West)
	while get_pos_y() != 0: 
		move(South)

def tiller(groundType):
	if groundType != get_ground_type():
			till()

def waterTile():
	if get_water() < 0.80:
			use_item(Items.Water)

def goTo(x, y):
	# if (x < 0 or x >= get_world_size() or y < 0 or y >= get_world_size()):
	# 	return print("Out of bounds")
	
	# if (x == get_pos_x() and y == get_pos_y()):
	# 	return 
    
	dx = x - get_pos_x()
	dy = y - get_pos_y()

	if abs(dx) > worldSize/2:
		if dx > 0:
			dx -= worldSize
		else:
			dx += worldSize
    
	if abs(dy) > worldSize/2:
		if dy > 0: 
			dy -= worldSize
		else:
			dy += worldSize

	while dx != 0:
		if dx > 0:
			move(East)
			dx -= 1
		else:
			move(West)
			dx += 1

	while dy != 0:
		if dy > 0:
			move(North)
			dy -= 1
		else:
			move(South)
			dy += 1

def fertilize():
	use_item(Items.Fertilizer)