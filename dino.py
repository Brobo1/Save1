from utils import *


# def dinoBones():
# 	hDir = [East, West]
# 	vDir = [North, South]
# 	turn = True
# 	turnIndex = 0

# 	while True:

# 		while move(vDir[turnIndex % 2]):
# 			pass

# 		if turn:
# 			move(hDir[turnIndex % 2])
# 			turn = not turn
# 		else:
# 			move(hDir[(turnIndex+1) % 2])
# 			turn = not turn

# 		while move(vDir[(turnIndex+1) % 2]):
# 			pass

# 		turn = not turn

# 		if (get_pos_x() == get_world_size()-1 and get_pos_y() == get_world_size()-1
# 			or get_pos_x() == 0 and get_pos_y() == 0
# 			or get_pos_x() == get_world_size()-1 and get_pos_y() == 0
# 			or get_pos_x() == 0 and get_pos_y() == get_world_size()-1):
			# turnIndex += 1 

def dinoBones():
	hDir = [East, West]
	vDir = [North, South]
	turn = True
	turnIndex = 0
	size = get_world_size()-1


	change_hat(Hats.Dinosaur_Hat)
	goTo(0,0)
	change_hat(Hats.Dinosaur_Hat)

	while get_pos_y() != size:
		move(vDir[turnIndex])
		pass

	while move(hDir[turnIndex]):
		pass 

	while get_pos_x() == size and get_pos_y() == size:
		move(vDir[(turnIndex+1)%2])
	
	while get_pos_x() > 1 and get_pos_y() == size-1:
		move(hDir[(turnIndex+1)%2])
	
	while True:
		while move(vDir[(turnIndex+1)%2]):
			pass

		while  

# change_hat(Hats.Dinosaur_Hat)
dinoBones()

