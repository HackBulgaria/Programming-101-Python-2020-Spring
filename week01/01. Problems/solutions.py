"""
Copyright (c) 2019 Hack Bulgaria

The project is released under MIT License
https://github.com/HackBulgaria/Programming-101-Python-2020-Spring
"""


def divisible_by_d(n: list, d: int) -> list:
	'''Returns a list of all numbers from n divislbe by d.'''
	return [i for i in n if i % d == 0]


def knight_moves(pos: tuple) -> int:
	'''Returns the count of all legal moves which the knight can make.'''
	offsets = ((-2, -1), (-2, 1), (-1, -2), (-1, 2),
			   (1, -2), (1, 2), (2, -1), (2, 1))

	return [ 0 <= (pos[0] + o[0]) < 8 and
			 0 <= (pos[1] + o[1]) < 8 
			for o in offsets].count(True)


	# valids = ((pos[0] - 2, pos[1] - 1),
	# 	(pos[0] - 2, pos[1] + 1),
	# 	(pos[0] + 2, pos[1] - 1),
	# 	(pos[0] + 2, pos[1] + 1),
	# 	(pos[1] - 2, pos[0] - 1),
	# 	(pos[1] - 2, pos[0] + 1),
	# 	(pos[1] + 2, pos[0] - 1),
	# 	(pos[1] + 2, pos[0] + 1))

	# return (
	# 	0 <= pos[0] - 2 <= 7 and 0 <= pos[1] - 1 <= 7,
	# 	0 <= pos[0] - 2 <= 7 and 0 <= pos[1] + 1 <= 7,
	# 	0 <= pos[0] + 2 <= 7 and 0 <= pos[1] - 1 <= 7,
	# 	0 <= pos[0] + 2 <= 7 and 0 <= pos[1] + 1 <= 7,

	# 	0 <= pos[1] - 2 <= 7 and 0 <= pos[0] - 1 <= 7,		
	# 	0 <= pos[1] - 2 <= 7 and 0 <= pos[0] + 1 <= 7,
	# 	0 <= pos[1] + 2 <= 7 and 0 <= pos[0] - 1 <= 7,
	# 	0 <= pos[1] + 2 <= 7 and 0 <= pos[0] + 1 <= 7
	# 	).count(True)
