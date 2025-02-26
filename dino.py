from utils import *


def dinoBones():
	hDir = [East, West]
	vDir = [North, South]
	turn = True
	turnIndex = 0
	lapIndex = 0
	gridType = get_world_size() % 2 == 0
	size = get_world_size()-1
	apples = []


	change_hat(Hats.Dinosaur_Hat)
	goTo(0,0)
	change_hat(Hats.Dinosaur_Hat)

	while True:

		quick_print(len(apples))

		if gridType:
			while get_pos_y() < size and move(vDir[0]):
				addApples(apples)
		else:
			if lapIndex % 2 == 0:
				while get_pos_y() < size-1 and move(vDir[0]):
					addApples(apples)
			else: 
				while get_pos_y() < size and move(vDir[0]):
					addApples(apples)

		while get_pos_x() < size and move(hDir[0]):
			addApples(apples)

		if lapIndex % 2 == 0:
			move(vDir[1])
			addApples(apples)
		else:
			move(vDir[1])
			addApples(apples)
			move(vDir[1])
			addApples(apples)

		if not gridType:
			lapIndex += 1

		while get_pos_x() != 0 and get_pos_y() !=0 and len(apples) <= 32:
			quick_print(len(apples))

			while get_pos_x() > 1 and move(hDir[1]): 
				addApples(apples)

			move(vDir[1])
			addApples(apples)

			while get_pos_x() < size and move(hDir[0]):
				addApples(apples) 

			move(vDir[1])
			addApples(apples)

		while get_pos_x() != 0 and move(hDir[1]):
			addApples(apples)


def addApples(apples):
	if measure() != None:
		apples.append(measure())


# change_hat(Hats.Dinosaur_Hat)

while True:
	dinoBones()


