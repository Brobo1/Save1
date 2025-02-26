from utils import *


def dinoBones():
	hDir = [East, West]
	vDir = [North, South]
	turn = True
	turnIndex = 0
	size = get_world_size()-1

	change_hat(Hats.Dinosaur_Hat)
	goTo(0,0)
	change_hat(Hats.Dinosaur_Hat)

	while True:

		while get_pos_y() < size and move(vDir[0]):
			pass

		while get_pos_x() < size and move(hDir[0]):
			pass

		move(vDir[1])

		while get_pos_x() != 0 and get_pos_y() !=0:
			
			while get_pos_x() > 1 and move(hDir[1]): 
				pass

			move(vDir[1])

			while get_pos_x() < size and move(hDir[0]):
				pass 

			move(vDir[1])

		while get_pos_x() != 0 and move(hDir[1]):
			pass





# change_hat(Hats.Dinosaur_Hat)
dinoBones()






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