from __future__ import division

from itertools import combinations

# 等差数列
def arithProgress(aList):
	count = len(aList)
	step = aList[1] - aList[0]
	for i in range(1, count):
		if (aList[i] - aList[i-1] == step):
			continue
		else:
			return False
	return	True

# 等比数列
def GeomProgress(aList):
	count = len(aList)
	step = aList[1] / aList[0]
	for i in range(1, count):
		if (aList[i] / aList[i-1] == step):
			continue
		else:
			return False	
	return	True

# 全偶数
def allEven(aList):
	for i in aList:
		if (i % 2 != 0):
			return False
	return True

#全奇数 
def allOdd(aList):
	for i in aList:
		if (i % 2 == 0):
			return False
	return True

# 5连环
def connect5(aList):
	a1 = [aList[0], aList[1], aList[2], aList[3], aList[4]]
	a2 = [aList[1], aList[2], aList[3], aList[4], aList[5]]
	if (arithProgress(a1) or GeomProgress(a1) or
		arithProgress(a2) or GeomProgress(a2)):
		return True
	return False

# 4连环
def connect4(aList):
	a1 = [aList[0], aList[1], aList[2], aList[3]]
	a2 = [aList[1], aList[2], aList[3], aList[4]]
	a3 = [aList[2], aList[3], aList[4], aList[5]]
	
	if (arithProgress(a1) or GeomProgress(a1) or
		arithProgress(a2) or GeomProgress(a2) or
		arithProgress(a3) or GeomProgress(a3)):
		return True
	return False

# 3连环
def connect3(aList):
	a1 = [aList[0], aList[1], aList[2]]
	a2 = [aList[1], aList[2], aList[3]]
	a3 = [aList[2], aList[3], aList[4]]
	a4 = [aList[3], aList[4], aList[5]]
	
	if (arithProgress(a1) or GeomProgress(a1) or
		arithProgress(a2) or GeomProgress(a2) or
		arithProgress(a3) or GeomProgress(a3) or
		arithProgress(a4) or GeomProgress(a4)):
		return True
	return False

# 2连环
def connect2(aList):
	if ((aList[1] - aList[0] == 1) or
		(aList[2] - aList[1] == 1) or
		(aList[3] - aList[2] == 1) or
		(aList[4] - aList[3] == 1) or
		(aList[5] - aList[4] == 1)):
		return True
		
	return False

# 全大于10
def allBig10(aList):

	if (aList[0] > 10):
		return True
	else:
		return False

# 全小于10
def allSmall10(aList):
	if (aList[5] < 10):
		return True
	else:
		return False

fp = open("total.txt", 'w')

for i in combinations(range(1, 34), 6):
	if (arithProgress(i) or GeomProgress(i) or 
		allEven(i) or allOdd(i) or 
		connect5(i) or connect4(i) or connect3(i) or connect2(i)
		or allBig10(i) or allSmall10(i)):
		continue
	else:
		for ele in i:
			if ele < 10:
				fp.write("0")
			fp.write(str(ele))
			fp.write(" ")
		fp.write("\n")