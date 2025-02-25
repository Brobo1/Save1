from utils import *


def dinoBones():
	hDir = [East, West]
	vDir = [North, South]
	turn = True
	turnIndex = 0

	while True:

		while move(vDir[turnIndex % 2]):
			pass

		if turn:
			move(hDir[turnIndex % 2])
			turn = not turn
		else:
			move(hDir[(turnIndex+1) % 2])
			turn = not turn

		while move(vDir[(turnIndex+1) % 2]):
			pass

		turn = not turn

		if (get_pos_x() == get_world_size()-1 and get_pos_y() == get_world_size()-1
			or get_pos_x() == 0 and get_pos_y() == 0
			or get_pos_x() == get_world_size()-1 and get_pos_y() == 0
			or get_pos_x() == 0 and get_pos_y() == get_world_size()-1):
			turnIndex += 1 


change_hat(Hats.Dinosaur_Hat)
dinoBones()