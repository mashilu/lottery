from __future__ import division

from itertools import combinations


# 等差数列
def arith_progress(alist):
	count = len(alist)
	step = alist[1] - alist[0]
	for i in range(1, count):
		if alist[i] - alist[i-1] == step:
			continue
		else:
			return False
	return True


# 等比数列
def geom_progress(alist):
	count = len(alist)
	step = alist[1] / alist[0]
	for i in range(1, count):
		if alist[i] / alist[i-1] == step:
			continue
		else:
			return False	
	return True


# 全偶数
def all_even(alist):
	for i in alist:
		if i % 2 != 0:
			return False
	return True


# 全奇数
def all_odd(alist):
	for i in alist:
		if i % 2 == 0:
			return False
	return True


# 5连环
def connect5(alist):
	a1 = [alist[0], alist[1], alist[2], alist[3], alist[4]]
	a2 = [alist[1], alist[2], alist[3], alist[4], alist[5]]
	if arith_progress(a1) or geom_progress(a1) or \
		arith_progress(a2) or geom_progress(a2):
		return True
	return False


# 4连环
def connect4(alist):
	a1 = [alist[0], alist[1], alist[2], alist[3]]
	a2 = [alist[1], alist[2], alist[3], alist[4]]
	a3 = [alist[2], alist[3], alist[4], alist[5]]
	
	if arith_progress(a1) or geom_progress(a1) or arith_progress(a2) or \
		geom_progress(a2) or arith_progress(a3) or geom_progress(a3):
		return True
	return False


# 3连环
def connect3(alist):
	a1 = [alist[0], alist[1], alist[2]]
	a2 = [alist[1], alist[2], alist[3]]
	a3 = [alist[2], alist[3], alist[4]]
	a4 = [alist[3], alist[4], alist[5]]
	
	if arith_progress(a1) or geom_progress(a1) or \
		arith_progress(a2) or geom_progress(a2) or \
		arith_progress(a3) or geom_progress(a3) or \
		arith_progress(a4) or geom_progress(a4):
		return True
	return False


# 2连环
def connect2(alist):
	if (alist[1] - alist[0] == 1) or (alist[2] - alist[1] == 1) or \
		(alist[3] - alist[2] == 1) or (alist[4] - alist[3] == 1) or \
		(alist[5] - alist[4] == 1):
		return True
		
	return False


# 全大于10
def all_big10(alist):

	if alist[0] > 10:
		return True
	else:
		return False


# 全小于10
def all_small10(alist):
	if alist[5] < 10:
		return True
	else:
		return False

fp = open("total.txt", 'w')

for i in combinations(range(1, 34), 6):
	if arith_progress(i) or geom_progress(i) or all_even(i) or all_odd(i) or \
		connect5(i) or connect4(i) or connect3(i) or connect2(i) or all_big10(i) or all_small10(i):
		continue
	else:
		for ele in i:
			if ele < 10:
				fp.write("0")
			fp.write(str(ele))
			fp.write(" ")
		fp.write("\n")
