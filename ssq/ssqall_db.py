# -*- coding=utf-8 -*-

import itertools


if __name__ == "__main__":
	for i in itertools.product((itertools.combinations(range(1, 34), 6)), range(1, 17)):
		print(i)