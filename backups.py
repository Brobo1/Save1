def goTo(x, y):
	world_size = get_world_size()
	current_x = get_pos_x()
	current_y = get_pos_y()

	# Handle out-of-bounds cases (wrapping around)
	if x < 0:
		x += world_size
	elif x >= world_size:
		x -= world_size
	if y < 0:
		y += world_size
	elif y >= world_size:
		y -= world_size

	# Calculate shortest horizontal distance (handling wrap-around)
	dx = x - current_x
	if abs(dx) > world_size / 2:
		if dx > 0:
			dx -= world_size
		else:
			dx += world_size

	# Calculate shortest vertical distance (handling wrap-around)
	dy = y - current_y
	if abs(dy) > world_size / 2:
		if dy > 0:
			dy -= world_size
		else:
			dy += world_size

	# Move horizontally
	while dx != 0:
		if dx > 0:
			move(East)
			dx -= 1
		else:
			move(West)
			dx += 1

	# Move vertically
	while dy != 0:
		if dy > 0:
			move(North)
			dy -= 1
		else:
			move(South)
			dy += 1
