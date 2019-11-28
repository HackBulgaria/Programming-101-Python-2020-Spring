"""
Copyright (c) 2019 Hack Bulgaria

The project is released under MIT License
https://github.com/HackBulgaria/Programming-101-Python-2020-Spring
"""


def divisible_by_d(n: list, d: int) -> list:
	'''Returns a list of all numbers from n divislbe by d.'''
	return [i for i in n if i % d == 0]
