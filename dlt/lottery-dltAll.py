# -*- coding:utf-8 -*-

import itertools

if __name__ == "__main__":
	fp = open("dlt_total.txt", "w")
	redballs = [x for x in range(1, 10)]

	for x in itertools.combinations(redballs, 5):
		fp.write(str(x) + "\n")

	fp.close()
